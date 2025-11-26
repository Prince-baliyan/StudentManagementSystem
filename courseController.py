# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# import windows as ui
import handleDB as db
from PyQt5.QtWidgets import QMessageBox

import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QColor
from calendar import monthrange


## ------------------------------------------------------------- CLASS OF A COURSE CONTROLLER ---------------------------------------------------------------------- ##

class CourseController:
    def __init__(self, ui):
        self.ui = ui
        self.connectSignals()
        self.db = db.student()
        self.updateCombobox()
        
    
    def updateCombobox(self):
        course = self.db.ShowAllcourse()
        lst = list(map(lambda x : x[0] , course))
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(lst)
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(lst)
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(lst)
        teachers = self.db.showAllTeacherName()
        print(teachers)
        lst = list(map(lambda x : str(x[0]) + "-" + str(x[1]) , teachers))
        self.ui.comboBox_4.clear()
        self.ui.comboBox_4.addItems(lst)


    def connectSignals(self):
        self.ui.pushButton_18.clicked.connect(self.saveCourse)
        self.ui.pushButton_19.clicked.connect(self.updatecourse)

## ----------------------------------------------- ADD COURSE NAME ------------------------------------------------- ##

    def saveCourse(self):
        self.CourseName=self.ui.lineEdit_12.text()
        self.db.savecouse(self.CourseName)
        self.ui.lineEdit_12.setText("")
        QMessageBox(QMessageBox.Critical,"Information","Course Added SuccessFully.",QMessageBox.Ok).exec_()
        print("Saved")
        self.updateCombobox()

## ---------------------------------------------- UPDATE COURSE NAME ------------------------------------------------ ##

    def updatecourse(self):
        self.SelectCourse=self.ui.comboBox.currentText()
        self.NewCourseName=self.ui.lineEdit_13.text()
        self.db.updateCourse(self.SelectCourse, self.NewCourseName)
        self.ui.lineEdit_13.setText("")
        QMessageBox(QMessageBox.Critical,"Information","Course Change SuccessFully.",QMessageBox.Ok).exec_()

## ------------------------------------------------------------------- CLASS FOR ATTENDANCE TABLE FOR STUDENT -------------------------------------------------------- ##

class AttendanceApp:
    def __init__(self, ui):
        self.ui = ui
        self.current_date = QDate.currentDate()
        self.current_year = self.current_date.year()
        self.current_month = self.current_date.month()

        self.initUI()
        self.initDB()
        self.load_attendance()

    def initUI(self):
        self.update_month_label()
        self.ui.prev_button.clicked.connect(self.prev_month)
        self.ui.next_button.clicked.connect(self.next_month)
        self.ui.table.cellChanged.connect(self.cell_edited)
        self.ui.pushButton_14.clicked.connect(self.ref_studenttable)

    def initDB(self):
        self.conn = sqlite3.connect("student_management.db")
        self.cursor = self.conn.cursor()

    # -------------------------- Create student table ----------------------------#
        
        query = """CREATE TABLE IF NOT EXISTS Studenttbl(
                    Student_Id TEXT NOT NULL primary key,
                    Student_Name TEXT,
                    Father_Name TEXT,
                    Contact_Number TEXT NOT NULL,
                    Email_Id TEXT NOT NULL,
                    Address TEXT NOT NULL,
                    Date_Of_Birth TEXT NOT NULL,
                    Gender TEXT NOT NULL,
                    Course_Stream TEXT NOT NULL,
                    Registration_Number TEXT NOT NULL,
                    Father_Contact_Number TEXT NOT NULL
            )"""
        self.cursor.execute(query)

    # -------------------------- Create attendance table --------------------------#
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendanceStudent (
                student TEXT,
                date TEXT,
                status TEXT,
                PRIMARY KEY (student, date)
            )
        """)
        
        self.conn.commit()
        self.load_students()

    def update_month_label(self):
        self.ui.month_label.setText(f"{QDate(self.current_year,self.current_month, 1).toString('MMMM yyyy')}")

    def populate_table(self):
        self.ui.table.blockSignals(True)
        days = monthrange(self.current_year, self.current_month)[1]
        self.ui.table.setRowCount(len(self.students))
        self.ui.table.setColumnCount(days + 1)

        headers = ["Name"] + [str(day) for day in range(1, days + 1)]
        self.ui.table.setHorizontalHeaderLabels(headers)

        for row, student in enumerate(self.students):
            self.ui.table.setItem(row, 0, QTableWidgetItem(student))
            for col in range(1, days + 1):
                item = QTableWidgetItem("")
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(row, col, item)
        self.ui.table.blockSignals(False)

    def load_students(self):
        self.cursor.execute("SELECT Student_Name FROM Studenttbl")
        result = self.cursor.fetchall()
        self.students = [row[0] for row in result]


    def ref_studenttable(self):
        self.initDB()
        self.load_attendance()

    def load_attendance(self):
        self.populate_table()
        self.ui.table.blockSignals(True)
        for row, student in enumerate(self.students):
            for col in range(1, self.ui.table.columnCount()):
                date_str = f"{self.current_year}-{self.current_month:02d}-{col:02d}"
                self.cursor.execute("SELECT status FROM attendance WHERE student=? AND date=?", (student, date_str))
                result = self.cursor.fetchone()
                if result:
                    item = self.ui.table.item(row, col)
                    item.setText(result[0])
                    self.set_cell_color(item)
        self.ui.table.blockSignals(False)
  
    def cell_edited(self, row, col):
        if col == 0:
            return                                                           # Skip name column
        student = self.ui.table.item(row, 0).text()
        date_str = f"{self.current_year}-{self.current_month:02d}-{col:02d}"
        item = self.ui.table.item(row, col)

        # Force uppercase and update cell
        status = item.text().strip().upper()
        self.ui.table.blockSignals(True)                                     # Prevent recursion
        item.setText(status)
        self.ui.table.blockSignals(False)

        self.set_cell_color(item)

        self.cursor.execute("""
            INSERT OR REPLACE INTO attendance (student, date, status)
            VALUES (?, ?, ?)
        """, (student, date_str, status))
        self.conn.commit()

    def set_cell_color(self, item):
        status = item.text().strip().upper()
        if status == "P":
            item.setBackground(QColor("lightgreen"))
        elif status == "A":
            item.setBackground(QColor("lightcoral"))
        else:
            item.setBackground(QColor("white"))

    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.update_month_label()
        self.load_attendance()

    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.update_month_label()
        self.load_attendance()

    def closeEvent(self, event):
        self.conn.close()
        event.accept()

## ---------------------------------------------------------- CLASS FOR ATTENDANCE TABLE FOR TEACHER ---------------------------------------------------------------- ##

class AttendanceAppTeacher:
    def __init__(self, ui):
        self.ui = ui
        self.current_date = QDate.currentDate()
        self.current_year = self.current_date.year()
        self.current_month = self.current_date.month()

        self.initUI()
        self.initDB()
        self.load_attendance()

    def initUI(self):
        self.update_month_label_2()
        self.ui.prev_button_2.clicked.connect(self.prev_month)
        self.ui.next_button_2.clicked.connect(self.next_month)
        self.ui.tables.cellChanged.connect(self.cell_edited)

    def initDB(self):
        self.conn = sqlite3.connect("student_management.db")
        self.cursor = self.conn.cursor()

    # ------------------------- Create teacher table -------------------------#

        query ="""CREATE TABLE IF NOT EXISTS Teachertbl(
                    Teacher_Id TEXT NOT NULL,
                    Teacher_Name TEXT PRIMARY KEY,
                    Gender TEXT NOT NULL,
                    Date_Of_Birth TEXT NOT NULL,
                    Address TEXT NOT NULL,
                    Contact_Number TEXT NOT NULL,
                    Email_Id TEXT NOT NULL,
                    Subject text,
                    Qualification_Experience TEXT NOT NULL,
                    Department_Designation TEXT NOT NULL,
                    Date_Of_Joining TEXT NOT NULL
                )"""
        self.cursor.execute(query)

    # ------------------------- Create attendance table -------------------------#
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendanceTeacher (
                student TEXT,
                date TEXT,
                status TEXT,
                PRIMARY KEY (student, date)
            )
        """)
        
        self.conn.commit()
        self.load_teachers()

    def update_month_label_2(self):
        self.ui.month_label_2.setText(f"{QDate(self.current_year,self.current_month, 1).toString('MMMM yyyy')}")

    def populate_table(self):
        self.ui.tables.blockSignals(True)
        days = monthrange(self.current_year, self.current_month)[1]
        self.ui.tables.setRowCount(len(self.students))
        self.ui.tables.setColumnCount(days + 1)

        headers = ["Name"] + [str(day) for day in range(1, days + 1)]
        self.ui.tables.setHorizontalHeaderLabels(headers)

        for row, student in enumerate(self.students):
            self.ui.tables.setItem(row, 0, QTableWidgetItem(student))
            for col in range(1, days + 1):
                item = QTableWidgetItem("")
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tables.setItem(row, col, item)
        self.ui.tables.blockSignals(False)

    def load_teachers(self):
        self.cursor.execute("SELECT Teacher_Name FROM Teachertbl")
        result = self.cursor.fetchall()
        self.students = [row[0] for row in result]

    def ref_teacherable(self):
        self.initDB()
        self.load_attendance()

    def load_attendance(self):
        self.populate_table()
        self.ui.tables.blockSignals(True)
        for row, student in enumerate(self.students):
            for col in range(1, self.ui.tables.columnCount()):
                date_str = f"{self.current_year}-{self.current_month:02d}-{col:02d}"
                self.cursor.execute("SELECT status FROM attendance WHERE student=? AND date=?", (student, date_str))
                result = self.cursor.fetchone()
                if result:
                    item = self.ui.tables.item(row, col)
                    item.setText(result[0])
                    self.set_cell_color(item)
        self.ui.tables.blockSignals(False)

    def cell_edited(self, row, col):
        if col == 0:
            return                                                           # Skip name column
        student = self.ui.tables.item(row, 0).text()
        date_str = f"{self.current_year}-{self.current_month:02d}-{col:02d}"
        item = self.ui.tables.item(row, col)

        # Force uppercase and update cell
        status = item.text().strip().upper()
        self.ui.tables.blockSignals(True)                                     # Prevent recursion
        item.setText(status)
        self.ui.tables.blockSignals(False)

        self.set_cell_color(item)

        self.cursor.execute("""
            INSERT OR REPLACE INTO attendance (student, date, status)
            VALUES (?, ?, ?)
        """, (student, date_str, status))
        self.conn.commit()

    def set_cell_color(self, item):
        status = item.text().strip().upper()
        if status == "P":
            item.setBackground(QColor("lightgreen"))
        elif status == "A":
            item.setBackground(QColor("lightcoral"))
        else:
            item.setBackground(QColor("white"))

    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.update_month_label_2()
        self.load_attendance()

    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.update_month_label_2()
        self.load_attendance()

    def closeEvent(self, event):
        self.conn.close()
        event.accept()