from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import windows as ui
import handleDB as db
from PyQt5.QtWidgets import QMessageBox 
from courseController import CourseController, AttendanceApp, AttendanceAppTeacher
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class Control:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.db = db.Auth()
        self.st = db.student()
        self.courseController = CourseController(self.ui)
        self.attendanceController = AttendanceApp(self.ui)
        self.attendanceController1 = AttendanceAppTeacher(self.ui)

## ---------------------------------------------------------------- ALL TOTAL BUTTON OF PROGRAM ---------------------------------------------------------------------- ##
        
        self.ui.pushButton.clicked.connect(self.logindetail)
        self.ui.pushButton_2.clicked.connect(self.showSignup)
        self.ui.pushButton_3.clicked.connect(self.forget)
        self.ui.pushButton_4.clicked.connect(self.backbuttonLP)
        self.ui.pushButton_5.clicked.connect(self.saveUser)
        self.ui.pushButton_6.clicked.connect(self.forgetdetail)
        self.ui.pushButton_7.clicked.connect(self.backbutton)
        self.ui.pushButton_8.clicked.connect(self.home)
        self.ui.pushButton_9.clicked.connect(self.addstudent)
        self.ui.pushButton_10.clicked.connect(self.managestudent)
        self.ui.pushButton_11.clicked.connect(self.addteacher)
        self.ui.pushButton_12.clicked.connect(self.manageteacher)
        self.ui.pushButton_13.clicked.connect(self.course)
        self.ui.pushButton_13.clicked.connect(self.update)
        self.ui.pushButton_15.clicked.connect(self.logout)
        self.ui.pushButton_16.clicked.connect(self.addcourse)
        self.ui.pushButton_17.clicked.connect(self.updatecourse)
        self.ui.pushButton_21.clicked.connect(self.addstudentdetail)                    ## add student table ka submit button
        # self.ui.pushButton_21.clicked.connect(self.submitbutton)  
        self.ui.pushButton_20.clicked.connect(self.stbackbutton)                        ## add student table ka back button
        self.ui.pushButton_29.clicked.connect(self.addteacherdetail)                    ## add teacher table ka submit button
        # self.ui.pushButton_29.clicked.connect(self.submitbutton)   
        self.ui.pushButton_28.clicked.connect(self.backbuttonTB)                        ## add teacher ka back button  
        self.ui.pushButton_22.clicked.connect(self.viewallstudent) 
        self.ui.pushButton_24.clicked.connect(self.viewstudentprofile)
        self.ui.pushButton_26.clicked.connect(self.updatestudentdetail)
        self.ui.pushButton_27.clicked.connect(self.deletestudent)
        self.ui.pushButton_23.clicked.connect(self.attendancerecord)                      ## it is a student attendance table button
        self.ui.pushButton_36.clicked.connect(self.viewallteacher)
        self.ui.pushButton_32.clicked.connect(self.backSP)                                ## it is a back button of student profile
        self.ui.pushButton_25.clicked.connect(self.searchstudent)                         ##it is a search button of a student profile
        self.ui.pushButton_39.clicked.connect(self.backUS)                                ## it is a back  button of update student
        self.ui.pushButton_40.clicked.connect(self.searchUSD)                             ## it is a search button of update student detail
        # self.ui.pushButton_41.clicked.connect(self.updatedetail)                        ##it is a update button of update student detail
        self.ui.pushButton_48.clicked.connect(self.backDS)                                ##it is a back button of delete student
        self.ui.pushButton_47.clicked.connect(self.deleteStudent)                         ## it is a submit button of a delete student
        self.ui.pushButton_31.clicked.connect(self.searchteacherprofile)
        self.ui.pushButton_35.clicked.connect(self.editteacher)
        self.ui.pushButton_33.clicked.connect(self.deleteteacher)
        self.ui.pushButton_30.clicked.connect(self.assignsubject)
        self.ui.pushButton_34.clicked.connect(self.attendancerecordTB)                    ##it is a attendance of a teacher table
        self.ui.pushButton_37.clicked.connect(self.backSTP)                               ## it is a back button of a search teacher profile
        self.ui.pushButton_38.clicked.connect(self.searchteacher)                         ## it is a search button of a search teacher profile
        self.ui.pushButton_41.clicked.connect(self.updateStudent)
        self.ui.pushButton_42.clicked.connect(self.backET)                                ## it is a back button of a edit teacher
        self.ui.pushButton_43.clicked.connect(self.searchET)                              ## it is a search button of a edit teacher
        self.ui.pushButton_44.clicked.connect(self.updateteacher) 
        self.ui.pushButton_46.clicked.connect(self.backDT)                                ## it is a back button of a delete teacher 
        self.ui.pushButton_45.clicked.connect(self.deleteteachers)                        ## it is a submit button of a delete teacher
        self.ui.pushButton_50.clicked.connect(self.backAS)                                ## it is a back button of a assign subject
        # self.ui.pushButton_49.clicked.connect(self.assignsubjects)                      ## it is a submit button of a assign subject
        self.ui.pushButton_49.clicked.connect(self.assignsubjectteacher)
        MainWindow.show()
        sys.exit(app.exec_())

## ---------------------------------------------------------------------- L0GIN DETAIL ------------------------------------------------------------------------------- ##

    def logindetail(self):
        Username=self.ui.lineEdit.text()
        Password=self.ui.lineEdit_2.text() 
        if (Username == '' and Password ==''):
            QMessageBox(QMessageBox.Critical, "Warning","Username or Password Required!", QMessageBox.Ok).exec_()
        else:
            p =self.db.validateUser(Username,Password)
            if p == None:
                QMessageBox(QMessageBox.Critical, "Error","Invalid Details!", QMessageBox.Ok).exec_()
            else:
                self.gettotalcourse()
                self.gettotalteacher()
                self.gettotalstudent()
                self.showHome()
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        

## ------------------------------------------------------------------- SIGN UP DETAIL -------------------------------------------------------------------------------- ##

    def saveUser(self):
        name = self.ui.lineEdit_3.text()
        username=self.ui.lineEdit_4.text()
        EmailId=self.ui.lineEdit_5.text()
        mobilenumber=self.ui.lineEdit_6.text()
        Password=self.ui.lineEdit_7.text()
        securitykey=self.ui.lineEdit_8.text()
        if (name==''or username==''or EmailId==''or mobilenumber==''or Password==''or securitykey==''):
            QMessageBox(QMessageBox.Critical,"Warning","All Details Are Required!",QMessageBox.Ok).exec_()
        else:
            r=self.db.saveUser(name,username,EmailId,mobilenumber,Password,securitykey)
            if r==2:
                QMessageBox(QMessageBox.Critical,"Error","Username Already Exists!",QMessageBox.Ok).exec_()
            elif r == 3:
                QMessageBox(QMessageBox.Critical,"Error","Something Went Wrong to Save Data!",QMessageBox.Ok).exec_()
            else:
                self.showHome()
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.lineEdit_7.setText("")
        self.ui.lineEdit_8.setText("")

    def showSignup(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page)

## ------------------------------------------------------------------ FORGET PASSWORD  DETAIL ------------------------------------------------------------------------ ##

    def forgetdetail(self):
        Emailid=self.ui.lineEdit_9.text()
        Securitykey=self.ui.lineEdit_10.text()
        Newpassword=self.ui.lineEdit_11.text()
        if(Emailid=='' and Securitykey==''):
            QMessageBox(QMessageBox.Critical,"Warning","Email_id or Security_key Required!",QMessageBox.Ok).exec_()
        else:
            q=self.db.forgetpass(Emailid,Securitykey,Newpassword)
            if q==1:
                QMessageBox(QMessageBox.Critical,"Error","User not Found!",QMessageBox.Ok).exec()
            elif q == 2:
                QMessageBox(QMessageBox.Critical,"Warning","Unexpected Error!",QMessageBox.Ok).exec()
            else:
                self.showHome()
        self.ui.lineEdit_9.setText("")
        self.ui.lineEdit_10.setText("")
        self.ui.lineEdit_11.setText("")

    def forget(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_2)

## ------------------------------------------------------------------- ADD STUDENT DETAIL ---------------------------------------------------------------------------- ##

    def addstudentdetail(self):
        Student_Id=self.ui.lineEdit_14.text()
        Student_Name=self.ui.lineEdit_16.text()
        Date_Of_Birth=self.ui.lineEdit_20.text()
        Gender=self.ui.lineEdit_21.text()
        Address=self.ui.lineEdit_17.text()
        Course_Stream=self.ui.comboBox_3.currentText()
        Email_Id=self.ui.lineEdit_15.text() 
        Contact_Number=self.ui.lineEdit_19.text()
        Father_Name=self.ui.lineEdit_18.text()
        Father_Contact_Number=self.ui.lineEdit_24.text()
        Registration_Number=self.ui.lineEdit_23.text()
        if(Student_Id==''or Student_Name==''or Date_Of_Birth==''or Gender==''or Address==''or Course_Stream==''or Email_Id==''or Contact_Number==''or Father_Name==''or Father_Contact_Number==''or Registration_Number==''):
            QMessageBox(QMessageBox.Critical,"Warning","All Details Are Required!",QMessageBox.Ok).exec_()
        else:
            self.st.addStudent(Student_Id,Student_Name,Date_Of_Birth,Gender,Address,Course_Stream,Email_Id,Contact_Number,Father_Name,Father_Contact_Number,Registration_Number)
            print("Data save successfully:")
            self.st.showallstudent()
            self.showHome()
            QMessageBox(QMessageBox.Critical,"Information","Student Added SuccessFully.",QMessageBox.Ok).exec_()
        self.ui.lineEdit_14.setText("")
        self.ui.lineEdit_16.setText("")
        self.ui.lineEdit_20.setText("")
        self.ui.lineEdit_21.setText("")
        self.ui.lineEdit_17.setText("")
        self.ui.lineEdit_22.setText("")
        self.ui.lineEdit_15.setText("") 
        self.ui.lineEdit_19.setText("")
        self.ui.lineEdit_18.setText("")
        self.ui.lineEdit_24.setText("")
        self.ui.lineEdit_23.setText("")

    def addstudent(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_4)

## ----------------------------------------------------------------------- ALL STUDENT DETAIL TABLE ------------------------------------------------------------------ ##
    
    def viewallstudent(self):
        r=self.st.showallstudent()
        print(r)
    # --------------------- If No Teacher Found OR r is empty -----------------#

        if not r:
            QMessageBox(QMessageBox.Warning, "Warning", "No Student Add In Data Base!", QMessageBox.Ok).exec_()
            self.ui.tableWidget_2.setRowCount(0)
            return
   
    # ------------------ Table Setup --------------------------#
        self.ui.tableWidget.setRowCount(len(r))         # Number of rows
        self.ui.tableWidget.setColumnCount(len(r[0]))   # Number of columns

        self.ui.tableWidget.setHorizontalHeaderLabels(["Student_Id","Student_Name","Date_Of_Birth","Gender","Address","Course_Stream","Email_Id","Contact_Number","Father_Name","Father_Contact_Number","Registration_Number"])

        for row in range(len(r)):
            self.ui.tableWidget.setItem(row, 10, QTableWidgetItem(str(r[row][9])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(r[row][1])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(r[row][6])))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(r[row][7])))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(r[row][5])))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(r[row][8])))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(str(r[row][4])))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(str(r[row][3])))
            self.ui.tableWidget.setItem(row, 8, QTableWidgetItem(str(r[row][2])))
            self.ui.tableWidget.setItem(row, 9, QTableWidgetItem(str(r[row][10])))
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(r[row][0])))

        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_11)

## ----------------------------------------------------------------- SEARCH ONE STUDENT DETAIL ----------------------------------------------------------------------- ##
    
    def searchstudent(self):
        Student_Id=self.ui.lineEdit_45.text()

    # ----------- Condition: If Student_Id is empty -----------#

        if Student_Id == "":
            QMessageBox(QMessageBox.Warning, "Warning", "Please Enter Student_Id First!", QMessageBox.Ok).exec_()
            return

    # ----------- Fetch Record from DB -----------#

        r = self.st.studen(Student_Id)

    # ----------- Condition: If record not found -----------#

        if r is None or len(r) == 0:
            QMessageBox(QMessageBox.Critical, "Error", "Student Not Found!", QMessageBox.Ok).exec_()
            self.ui.lineEdit_45.setText("")
            return
        
        self.ui.lineEdit_45.setText("")                    # Clear search box
        print(r)
        Student_Id,Student_Name,Father_Name,Contact_Number,Email_Id,Address,Date_Of_Birth,Gender,Course,Registration_Number,Father_Contact_Number =  r
        self.ui.lineEdit_46.setText(Student_Id) 
        self.ui.lineEdit_26.setText(Student_Name)
        self.ui.lineEdit_37.setText(Father_Name)
        self.ui.lineEdit_39.setText(Date_Of_Birth)
        self.ui.lineEdit_40.setText(Gender)
        self.ui.lineEdit_41.setText(Address)
        self.ui.lineEdit_43.setText(Contact_Number)
        self.ui.lineEdit_48.setText(Father_Contact_Number)
        self.ui.lineEdit_42.setText(Email_Id)
        self.ui.lineEdit_49.setText(Course)
        self.ui.lineEdit_44.setText(Registration_Number)
        QMessageBox(QMessageBox.Critical,"Information","Searching Student is This.",QMessageBox.Ok).exec_()

## ---------------------- CLEAR THE DETAIL FOR SEACRHING STUDENT ----------------------------- ##

    def viewstudentprofile(self):
        self.ui.lineEdit_46.setText("") 
        self.ui.lineEdit_26.setText("")
        self.ui.lineEdit_37.setText("")
        self.ui.lineEdit_39.setText("")
        self.ui.lineEdit_40.setText("")
        self.ui.lineEdit_41.setText("")
        self.ui.lineEdit_43.setText("")
        self.ui.lineEdit_48.setText("")
        self.ui.lineEdit_42.setText("")
        self.ui.lineEdit_49.setText("")
        self.ui.lineEdit_44.setText("")
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_12)

## -------------------------------------------------------------------- UPDATE STUDENT DETAIL ------------------------------------------------------------------------ ##

##-------------------------------- SEARCH STUDENT -------------------------------- ##

    def searchUSD(self):
        Student_Id=self.ui.lineEdit_61.text()

        # ----------- Condition: If Student_Id is empty -----------#

        if Student_Id == "":
            QMessageBox(QMessageBox.Warning, "Warning", "Please Enter Student_Id First!", QMessageBox.Ok).exec_()
            return

    # ----------- Fetch Record from DB -----------#

        r=self.st.updatestuden(Student_Id)

    # ----------- Condition: If record not found -----------#

        if r is None or len(r) == 0:
            QMessageBox(QMessageBox.Critical, "Error", "Student Not Found!", QMessageBox.Ok).exec_()
            self.ui.lineEdit_61.setText("")
            return
        
        self.ui.lineEdit_61.setText("")
        print(r)
        Student_Id,Student_Name,Father_Name,Contact_Number,Email_Id,Address,Date_Of_Birth,Gender,Course_Stream,Registration_Number,Father_Contact_Number = r
        self.ui.lineEdit_63.setText(Student_Name)
        self.ui.lineEdit_64.setText(Father_Name)
        self.ui.lineEdit_65.setText(Date_Of_Birth)
        self.ui.lineEdit_67.setText(Address)
        self.ui.lineEdit_68.setText(Contact_Number)
        self.ui.lineEdit_70.setText(Father_Contact_Number)
        self.ui.lineEdit_69.setText(Email_Id)
        self.ui.lineEdit_71.setText(Course_Stream)
        self.ui.lineEdit_27.setText(Student_Id)
        self.ui.lineEdit_38.setText(Gender)
        self.ui.lineEdit_62.setText(Registration_Number)
        QMessageBox(QMessageBox.Critical,"Information","Searching Student is This.",QMessageBox.Ok).exec_()

## -------------------------------- UPDATE STUDENT ---------------------------------- ##

    def updateStudent(self):
        Student_Id = self.ui.lineEdit_27.text()
        Student_Name = self.ui.lineEdit_63.text()
        Father_Name = self.ui.lineEdit_64.text()
        Date_Of_Birth = self.ui.lineEdit_65.text()
        Address = self.ui.lineEdit_67.text()
        Contact_Number = self.ui.lineEdit_68.text()
        Father_Contact_Number = self.ui.lineEdit_70.text()
        Email_Id = self.ui.lineEdit_69.text()
        Course_Stream = self.ui.lineEdit_71.text()
        Gender = self.ui.lineEdit_38.text()
        Registration_Number = self.ui.lineEdit_62.text()
        self.st.updateStudent(Student_Id,Student_Name, Father_Name , Contact_Number,Email_Id, Address, Date_Of_Birth, Gender, Course_Stream, Registration_Number, Father_Contact_Number)
        QMessageBox(QMessageBox.Critical,"Information","Data Update SuccessFully.",QMessageBox.Ok).exec_()
        self.ui.lineEdit_27.setText("")
        self.ui.lineEdit_63.setText("")
        self.ui.lineEdit_64.setText("")
        self.ui.lineEdit_65.setText("")
        self.ui.lineEdit_67.setText("")
        self.ui.lineEdit_68.setText("")
        self.ui.lineEdit_70.setText("")
        self.ui.lineEdit_69.setText("")
        self.ui.lineEdit_71.setText("")
        self.ui.lineEdit_38.setText("")
        self.ui.lineEdit_62.setText("")

## ----------------------- CLEAR DETAIL FOR UPDATE STUDENT --------------------- ##

    def updatestudentdetail(self):
        self.ui.lineEdit_27.setText("")
        self.ui.lineEdit_63.setText("")
        self.ui.lineEdit_64.setText("")
        self.ui.lineEdit_65.setText("")
        self.ui.lineEdit_67.setText("")
        self.ui.lineEdit_68.setText("")
        self.ui.lineEdit_70.setText("")
        self.ui.lineEdit_69.setText("")
        self.ui.lineEdit_71.setText("")
        self.ui.lineEdit_38.setText("")
        self.ui.lineEdit_62.setText("")
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_13)


## --------------------------------------------------------------------- DELETE STUDENT DETAIL ----------------------------------------------------------------------- ##
  
    def deleteStudent(self):
        Student_Id=self.ui.lineEdit_82.text()

        # ----------- Condition: If Student_Id is empty -----------#

        if Student_Id == "":
            QMessageBox(QMessageBox.Warning, "Warning", "Please Enter Student_Id First!", QMessageBox.Ok).exec_()
            return

        # ----------- Fetch Record from DB -----------#PePrP

        r=self.st.deletestudent(Student_Id)
        
        # ----------- Condition: If record not found -----------#
        print(r)
        if r!=True:
            QMessageBox(QMessageBox.Critical, "Error", "Student Not Found!", QMessageBox.Ok).exec_()
            self.ui.lineEdit_82.setText("")
            return
        else:
            QMessageBox(QMessageBox.Critical,"Information","Student Delete SuccessFully.",QMessageBox.Ok).exec_()
            self.ui.lineEdit_82.setText("")
       

    def deletestudent(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_14)


## ------------------------------------------------------------------ ADD TEACHER DETAIL ----------------------------------------------------------------------------- ##
    
    def addteacherdetail(self):
        Teacher_Id=self.ui.lineEdit_25.text()
        Teacher_Name=self.ui.lineEdit_36.text()
        Gender=self.ui.lineEdit_35.text()
        Date_Of_Birth=self.ui.lineEdit_29.text()
        Address=self.ui.lineEdit_31.text()
        Contact_Number=self.ui.lineEdit_33.text()
        Email_Id=self.ui.lineEdit_34.text()
        Qualification_Experience=self.ui.lineEdit_28.text()
        Department_Designation=self.ui.lineEdit_32.text()
        Date_of_Joining=self.ui.lineEdit_30.text()
        if(Teacher_Id==''or Teacher_Name==''or Gender==''or Date_Of_Birth==''or Address==''or Contact_Number==''or Email_Id==''or Qualification_Experience==''or Department_Designation==''or Date_of_Joining==''):
            QMessageBox(QMessageBox.Critical,"Warning","All Details Are Required!",QMessageBox.Ok).exec_()
        else:
            s=self.st.addTeacher(Teacher_Id,Teacher_Name,Gender,Date_Of_Birth,Address,Contact_Number,Email_Id,Qualification_Experience,Department_Designation,Date_of_Joining)
            print("s is", s)
            self.st.showallteacher()
            self.showHome()
            QMessageBox(QMessageBox.Critical,"Information","Teacher Added SuccessFully.",QMessageBox.Ok).exec_()
        self.ui.lineEdit_25.setText("")
        self.ui.lineEdit_36.setText("")
        self.ui.lineEdit_35.setText("")
        self.ui.lineEdit_29.setText("")
        self.ui.lineEdit_31.setText("")
        self.ui.lineEdit_33.setText("")
        self.ui.lineEdit_34.setText("")
        self.ui.lineEdit_28.setText("")
        self.ui.lineEdit_32.setText("")
        self.ui.lineEdit_30.setText("")

    def addteacher(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_6)

## ---------------------------------------------------------------- ALL TEACHER DETAIL TABLE ------------------------------------------------------------------------- ##

    def viewallteacher(self):
        r=self.st.showallteacher()
        print(r)
        
    # --------------------- If No Teacher Found OR r is empty -----------------#

        if not r:
            QMessageBox(QMessageBox.Warning, "Warning", "No Teacher Add In Data Base!", QMessageBox.Ok).exec_()
            self.ui.tableWidget_2.setRowCount(0)
            return
   
    # ------------------ Table Setup --------------------------#

        self.ui.tableWidget_2.setRowCount(len(r))         # Number of rows
        self.ui.tableWidget_2.setColumnCount(11)   # Number of columns

        # Set column headers
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Teacher_Id","Teacher_Name","Gender","Date_Of_Birth","Address","Contact_Number","Email_Id","Subject","Qualification_Experience","Department_Designation","Date_Of_Joining"])

        for row in range(len(r)):
                self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(r[row][0])))
                self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(r[row][1])))
                self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(r[row][2])))
                self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(r[row][3])))
                self.ui.tableWidget_2.setItem(row, 4, QTableWidgetItem(str(r[row][4])))
                self.ui.tableWidget_2.setItem(row, 5, QTableWidgetItem(str(r[row][5])))
                self.ui.tableWidget_2.setItem(row, 6, QTableWidgetItem(str(r[row][6])))
                self.ui.tableWidget_2.setItem(row, 7, QTableWidgetItem(str(r[row][9])))
                self.ui.tableWidget_2.setItem(row, 8, QTableWidgetItem(str(r[row][8])))
                self.ui.tableWidget_2.setItem(row, 9, QTableWidgetItem(str(r[row][7])))
                self.ui.tableWidget_2.setItem(row, 10, QTableWidgetItem(str(r[row][10])))

        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_16)
    
## ------------------------------------------------------------------ SEARCH ONE TEACHER DETAIL ---------------------------------------------------------------------- ##

    def searchteacher(self):
        Teacher_Id=self.ui.lineEdit_47.text()
    # ----------- Condition: If Student_Id is empty -----------#

        if Teacher_Id == "":
            QMessageBox(QMessageBox.Warning, "Warning", "Please Enter Teacher_Id First!", QMessageBox.Ok).exec_()
            return

    # ----------- Fetch Record from DB -----------#

        r=self.st.teach(Teacher_Id)

    # ----------- Condition: If record not found -----------#

        if r is None or len(r) == 0:
            QMessageBox(QMessageBox.Critical, "Error", "Teacher Not Found!", QMessageBox.Ok).exec_()
            self.ui.lineEdit_47.setText("")
            return
        
        self.ui.lineEdit_47.setText("")
        print(r)
        Teacher_Id,Teacher_Name,Gender,Date_Of_Birth,Address,Contact_Number,Email_Id,Subject,Qualification_Experience,Department_Designation,Date_of_Joining =r    
        self.ui.lineEdit_51.setText(Teacher_Id)
        self.ui.lineEdit_52.setText(Teacher_Name)
        self.ui.lineEdit_53.setText(Date_Of_Birth)
        self.ui.lineEdit_54.setText(Address)
        self.ui.lineEdit_55.setText(Gender)
        self.ui.lineEdit_56.setText(Contact_Number)
        self.ui.lineEdit_57.setText(Email_Id)
        self.ui.lineEdit_22.setText(Subject)
        self.ui.lineEdit_58.setText(Qualification_Experience)
        self.ui.lineEdit_59.setText(Department_Designation)
        self.ui.lineEdit_60.setText(Date_of_Joining)
        QMessageBox(QMessageBox.Critical,"Information","Searching Teacher is This.",QMessageBox.Ok).exec_()

## --------------- CLEAR DETAIL FOR SEARCHING TEACHER --------------- ##

    def searchteacherprofile(self):
        self.ui.lineEdit_51.setText("")
        self.ui.lineEdit_52.setText("")
        self.ui.lineEdit_53.setText("")
        self.ui.lineEdit_54.setText("")        
        self.ui.lineEdit_55.setText("")
        self.ui.lineEdit_56.setText("")
        self.ui.lineEdit_57.setText("")
        self.ui.lineEdit_22.setText("")
        self.ui.lineEdit_58.setText("")
        self.ui.lineEdit_59.setText("")
        self.ui.lineEdit_60.setText("")
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_17)

## -------------------------------------------------------------------- UPDATE TEACHER DETAIL ------------------------------------------------------------------------ ##

## --------------------------------------- SEARCH TEACHER ----------------------------------------------- ##

    def searchET(self):
        Teacher_Id=self.ui.lineEdit_66.text()
    
    # ----------- Condition: If Student_Id is empty -----------#

        if Teacher_Id == "":
            QMessageBox(QMessageBox.Warning, "Warning", "Please Enter Teacher_Id First!", QMessageBox.Ok).exec_()
            return

    # ----------- Fetch Record from DB -----------#

        r=self.st.updateteach(Teacher_Id)

    # ----------- Condition: If record not found -----------#

        if r is None or len(r) == 0:
            QMessageBox(QMessageBox.Critical, "Error", "Teacher Not Found!", QMessageBox.Ok).exec_()
            self.ui.lineEdit_66.setText("")
            return
        
        self.ui.lineEdit_66.setText("")
        print(r)
        Teacher_Id,Teacher_Name,Gender,Date_Of_Birth,Address,Contact_Number,Email_Id,Subject,Qualification_Experience,Department_Designation,Date_Of_Joining =r    
        self.ui.lineEdit_72.setText(Teacher_Id)
        self.ui.lineEdit_73.setText(Teacher_Name)
        self.ui.lineEdit_76.setText(Date_Of_Birth)
        self.ui.lineEdit_74.setText(Contact_Number)
        self.ui.lineEdit_75.setText(Address)
        self.ui.lineEdit_50.setText(Gender)
        self.ui.lineEdit_79.setText(Email_Id)
        self.ui.lineEdit_83.setText(Subject)
        self.ui.lineEdit_80.setText(Qualification_Experience)
        self.ui.lineEdit_78.setText(Department_Designation)
        self.ui.lineEdit_77.setText(Date_Of_Joining)
        QMessageBox(QMessageBox.Critical,"Information","Searching Teacher is This.",QMessageBox.Ok).exec_()


## ---------------------------------- UPDATE TEACHER --------------------------------------------------- ##

    def updateteacher(self):
        Teacher_Id = self.ui.lineEdit_72.text()
        Teacher_Name = self.ui.lineEdit_73.text()
        Date_Of_Birth = self.ui.lineEdit_76.text()
        Contact_Number = self.ui.lineEdit_74.text()
        Address = self.ui.lineEdit_75.text()
        Gender = self.ui.lineEdit_50.text()
        Email_Id = self.ui.lineEdit_79.text()
        Subject=self.ui.lineEdit_83.text()
        Qualification_Experience = self.ui.lineEdit_80.text()
        Department_Designation = self.ui.lineEdit_78.text()
        Date_Of_Joining = self.ui.lineEdit_77.text()
        self.st.updateteacher(Teacher_Id, Teacher_Name, Gender, Date_Of_Birth, Address, Contact_Number, Email_Id,Subject, Qualification_Experience, Department_Designation, Date_Of_Joining)
        QMessageBox(QMessageBox.Critical,"Information","Data Update SuccessFully.",QMessageBox.Ok).exec_()
        self.ui.lineEdit_72.setText("")
        self.ui.lineEdit_73.setText("")
        self.ui.lineEdit_76.setText("")
        self.ui.lineEdit_74.setText("")
        self.ui.lineEdit_75.setText("")
        self.ui.lineEdit_50.setText("")
        self.ui.lineEdit_79.setText("")
        self.ui.lineEdit_83.setText("")
        self.ui.lineEdit_80.setText("")
        self.ui.lineEdit_78.setText("")
        self.ui.lineEdit_77.setText("")

## -------------------------- CLEAR DETAIL FOR UPDATE TEACHER -------------------------------- ##

    def editteacher(self):
        self.ui.lineEdit_72.setText("")
        self.ui.lineEdit_73.setText("")
        self.ui.lineEdit_76.setText("")
        self.ui.lineEdit_74.setText("")
        self.ui.lineEdit_75.setText("")
        self.ui.lineEdit_50.setText("")
        self.ui.lineEdit_79.setText("")
        self.ui.lineEdit_83.setText("")
        self.ui.lineEdit_80.setText("")
        self.ui.lineEdit_78.setText("")
        self.ui.lineEdit_77.setText("")
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_19)

## --------------------------------------------------------------------- DELETE TEACHER DETAIL ----------------------------------------------------------------------- ##
 
    def deleteteachers(self):
        Teacher_Id=self.ui.lineEdit_81.text()
    
    # ----------- Condition: If Student_Id is empty -----------#

        if Teacher_Id == "":
            QMessageBox(QMessageBox.Warning, "Warning", "Please Enter Teacher_Id First!", QMessageBox.Ok).exec_()
            return

    # ----------- Fetch Record from DB -----------#
        
        r=self.st.deleteteachers(Teacher_Id)
        
    # ----------- Condition: If record not found -----------#
        print(r)

        if r != True:
            QMessageBox(QMessageBox.Critical, "Error", "Teacher Not Found!", QMessageBox.Ok).exec_()
            self.ui.lineEdit_81.setText("")
            return
        else:
            QMessageBox(QMessageBox.Critical,"Information","Teacher Delete SuccessFully.",QMessageBox.Ok).exec_()
            self.ui.lineEdit_81.setText("")
            

    def deleteteacher(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_20)
    
## -------------------------------------------------------------- ASSIGN SUBJECT FOR TEACHER ------------------------------------------------------------------------- ##    

    def assignsubject(self):
        self.courseController.updateCombobox()
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_18)

    def assignsubjectteacher(self):
        Teacher_Name=self.ui.comboBox_4.currentText()
        subject=self.ui.comboBox_2.currentText()
        tid = Teacher_Name.split("-")[0]
        self.st.updateSubject(tid, subject)
        QMessageBox(QMessageBox.Critical,"Information","Assign Subject SuccessFully.",QMessageBox.Ok).exec_()

## ------------------------------------------------------------------ FUNCTION OF LOGOUT ------------------------------------------------------##

    def logout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stackedWidgetPage1)

## ----------------------------------------------------------------- FUNCTION OF TOTAL COURSE -------------------------------------------------##

    def gettotalcourse(self):
        r=self.st.getTotalNumberOfCourse()
        print(r)
        self.ui.lineEdit_86.setText(r)

## ----------------------------------------------------------------- FUNCTION OF TOTAL TEACHER ------------------------------------------------##
 
    def gettotalteacher(self):
        r=self.st.getTotalNumberOfteacher()
        print(r)
        self.ui.lineEdit_85.setText(r)

## ----------------------------------------------------------------- FUNCTION OF TOTAL STUDENT ------------------------------------------------##
 
    def gettotalstudent(self):
        r=self.st.getTotalNumberOfstudent()
        print(r)
        self.ui.lineEdit_84.setText(r)

## -------------------------------------------------------------- FUNCTIONS OF BUTTONS ------------------------------------------------------- ##     


    def attendancerecordTB(self):
        self.attendanceController1.ref_teacherable()
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_21)
    
    def backSTP(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_7)

    def backET(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_7)
        
    def backDT(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_7)

    def backAS(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_7)    

    def backbuttonLP(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_page1to2)

    def backbutton(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_page1to2)

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def home(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.stackedWidget_7Page1)
    
    def managestudent(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_5)
    
    def manageteacher(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_7)

    def course(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_8)

    def addcourse(self):
        self.ui.stackedWidget_9.setCurrentWidget(self.ui.stackedWidget_9Page1)

    def updatecourse(self):
        self.ui.stackedWidget_9.setCurrentWidget(self.ui.page_10)

    def update(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_10)
        
    def attendance(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_9)
    
    def stbackbutton(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.stackedWidget_7Page1)       ## add student table ka backbutton 
    
    def submitbutton(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.widget_9)                   ## add student table ka submitbutton 
    
    def submitbutton(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_4)                     ## add teacher table ka submitbutton 

    def backbuttonTB(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.stackedWidget_7Page1)       ## add teacher table ka back button
        
    def attendancerecord(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_15)
    
    def backSP(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_5)
        
    def backUS(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_5)

    def backDS(self):
        self.ui.stackedWidget_7.setCurrentWidget(self.ui.page_5)


if __name__ == '__main__':
    Control()