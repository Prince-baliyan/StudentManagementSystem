import sqlite3

class Auth:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("student_management.db")
            self.cursor = self.conn.cursor()
            query = """CREATE TABLE IF NOT EXISTS record(
                        who_is_using TEXT NOT NULL,
                        username TEXT PRIMARY KEY,
                        Email_id TEXT NOT NULL,
                        Mobile_number INTEGER NOT NULL,
                        Password TEXT NOT NULL,
                        Security_key INTEGER NOT NULL
            )"""
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during initialization: {e}")
        except Exception as ex:
            print(f"Unexpected error during initialization: {ex}")

    def saveUser(self, who_is_using, username, email_id, mobile_number, password, security_key):
        try:
            self.cursor.execute(
                "INSERT INTO record (who_is_using, username, Email_id, Mobile_number, Password, Security_key) VALUES (?, ?, ?, ?, ?, ?)",
                (who_is_using, username, email_id, mobile_number, password, security_key)
            )
            self.conn.commit()
            return 1
        except sqlite3.IntegrityError:
            return 2
        except sqlite3.Error as e:
            return 3 
        except Exception as ex:
            return 3
 
    def showAllUser(self):
        try:
            self.cursor.execute("SELECT * FROM record")
            result = self.cursor.fetchall()
            print(result)
            print("Data save successfully.")
        except sqlite3.Error as e:
            print(f"Database error during showAllUser: {e}")
        except Exception as ex:
            print(f"Unexpected error during showAllUser: {ex}")

    def validateUser(self, username, password):
        try:
            self.cursor.execute(
                "SELECT who_is_using FROM record WHERE username = ? AND Password = ?",
                (username, password)
            ) 
            result = self.cursor.fetchone()
            print("Data save successfully.")
            return result
        except sqlite3.Error as e:
            print(f"Database error during validateUser: {e}")
            return None
        except Exception as ex:
            print(f"Unexpected error during validateUser: {ex}")
            return None

    def forgetpass(self, Emailid, Securitykey, Newpassword):
        try:
            self.cursor.execute(
                "UPDATE record SET Password = ? WHERE Email_id = ? AND Security_key = ?",
                (Newpassword, Emailid, Securitykey)
            )
            if self.cursor.rowcount == 0:
                print("no matching user")
                return 1
            self.conn.commit()
            print("Data save successfully.")
        except sqlite3.Error as e:
            print(f"Database error during forgetpass: {e}")
            return 2
        except Exception as ex:
            print(f"Unexpected error during forgetpass: {ex}")
            return 2
        
class student:
    def __init__(self):
        try:
            self.conn=sqlite3.connect("student_management.db")
            self.cursor = self.conn.cursor()
            query = """CREATE TABLE IF NOT EXISTS coursetbl(
                    CourseName TEXT primary key   
            )"""
            self.cursor.execute(query)
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
            query="""CREATE TABLE IF NOT EXISTS Studenttbl(
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
            self.conn.commit()
        except sqlite3.IntegrityError:
            return 1
    
    def savecouse(self,coursename):
        try:
            self.cursor.execute(
                "INSERT INTO coursetbl (CourseName) VALUES (?)",(coursename,)
            )
            self.conn.commit()
        except sqlite3.Error:
            return 2        
    
    def ShowAllcourse(self):
        try:
            self.cursor.execute("SELECT CourseName FROM coursetbl")
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error:
            return 3
    
    def getTotalNumberOfCourse(self):
        self.cursor.execute("select count(*) from coursetbl")
        r = self.cursor.fetchone()
        d =  "".join(map(str, r))
        return d
        
    def updateCourse(self, oldCourse, newCourse):
        self.cursor.execute("update coursetbl set courseName=? where courseName =?", (newCourse, oldCourse))
        self.conn.commit()
        print("Course change successfully.")
    
    def addStudent(self,Student_Id,Student_Name,Date_Of_Birth,Gender,Address,Course_Stream,Email_Id,Contact_Number,Father_Name,Father_Contact_Number,Registration_Number):
        try:
            self.cursor.execute(
                    "INSERT INTO Studenttbl (Student_Id,Student_Name,Date_Of_Birth,Gender,Address,Course_Stream,Email_Id,Contact_Number,Father_Name,Father_Contact_Number,Registration_Number) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (Student_Id,Student_Name,Date_Of_Birth,Gender,Address,Course_Stream,Email_Id,Contact_Number,Father_Name,Father_Contact_Number,Registration_Number)
            )
            result=self.conn.commit()
            return result
        
    # print("Data save successfully..")
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")
            return 2
        except sqlite3.Error as e:
            print(f"Database error during saveUser: {e}")
            return 3 
        except Exception as ex:
            print(f"Unexpected error during saveUser: {ex}")
            return 3

    def showonestudent(self):
        self.cursor.execute("SELECT * FROM Studenttbl")
        result = self.cursor.fetchone()
        print(result)
        print("Data save successfully.")

    def showallstudent(self):
        self.cursor.execute("SELECT * FROM Studenttbl")
        result = self.cursor.fetchall()
        return result
    
    def getTotalNumberOfstudent(self):
        self.cursor.execute("select count(*) from Studenttbl")
        r = self.cursor.fetchone()
        d =  "".join(map(str, r))
        return d
    
    def addTeacher(self,Teacher_Id,Teacher_Name,Gender,Date_Of_Birth,Address,Contact_Number,Email_Id,Qualification_Experience,Department_Designation,Date_Of_Joining):
        self.cursor.execute(
            "INSERT INTO Teachertbl (Teacher_Id,Teacher_Name,Gender,Date_Of_Birth,Address,Contact_Number,Email_Id,Qualification_Experience,Department_Designation,Date_Of_Joining ) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (Teacher_Id,Teacher_Name,Gender,Date_Of_Birth,Address,Contact_Number,Email_Id,Qualification_Experience,Department_Designation,Date_Of_Joining)
        )
        self.conn.commit()
        print("Data save successfully.")
    
    def showoneteacher(self):
        self.cursor.execute("SELECT * FROM Teachertbl")
        result = self.cursor.fetchone()
        print(result)
        print("Data save successfully.")
    
    def getTotalNumberOfteacher(self):
        self.cursor.execute("select count(*) from Teachertbl")
        r = self.cursor.fetchone()
        d =  "".join(map(str, r))
        return d

    def showallteacher(self):
        self.cursor.execute("SELECT * FROM Teachertbl")
        result = self.cursor.fetchall()
        return result
    def showAllTeacherName(self):
        self.cursor.execute("SELECT teacher_id ,teacher_name FROM Teachertbl")
        result = self.cursor.fetchall()
        return result
    
    def updateSubject(self, tid, subject):
        self.cursor.execute("update teachertbl set subject=? where teacher_id = ?", (subject, tid))
        self.conn.commit()
        return True


    def studen(self,Student_Id):
        self.cursor.execute("SELECT * FROM Studenttbl WHERE Student_Id = ? ",(Student_Id,))
        r = self.cursor.fetchone()
        return r
    
    def teach(self,Teacher_Id):
        self.cursor.execute("SELECT * FROM Teachertbl WHERE Teacher_Id = ? ",(Teacher_Id,))
        r=self.cursor.fetchone()
        return r

    def updatestuden(self,Student_Id):
        self.cursor.execute("SELECT * FROM Studenttbl WHERE Student_Id = ?",(Student_Id,))
        r=self.cursor.fetchone()
        return r
    
    def updateteach(self,Teacher_Id):
        self.cursor.execute("SELECT *FROM Teachertbl WHERE Teacher_Id = ?",(Teacher_Id,))
        r=self.cursor.fetchone()
        return r
    
    def updateStudent(self,Student_Id,Student_Name, Father_Name , Contact_Number,Email_Id, Address, Date_Of_Birth, Gender, Course_Stream, Registration_Number, Father_Contact_Number):
        self.cursor.execute("update Studenttbl set Student_Name =?, Father_Name =?, Contact_Number=?,Email_Id=?, Address=?, Date_Of_Birth=?, Gender=?, Course_Stream=?, Registration_Number=?, Father_Contact_Number=? where student_id=?",(Student_Name, Father_Name , Contact_Number,Email_Id, Address, Date_Of_Birth, Gender, Course_Stream, Registration_Number, Father_Contact_Number, Student_Id))
        self.conn.commit()
        return True
    
    def updateteacher(self,Teacher_Id, Teacher_Name, Gender, Date_Of_Birth, Address, Contact_Number, Email_Id,Subject, Qualification_Experience, Department_Designation, Date_Of_Joining):
        self.cursor.execute("update Teachertbl set Teacher_Name =?, Gender =?, Date_Of_Birth =?, Address =?, Contact_Number =?, Email_Id =?,Subject=?, Qualification_Experience =?, Department_Designation =?, Date_Of_Joining =? where Teacher_Id =?",(Teacher_Name, Gender, Date_Of_Birth, Address, Contact_Number, Email_Id,Subject, Qualification_Experience, Department_Designation, Date_Of_Joining, Teacher_Id))
        self.conn.commit()
        return True
    
    def deleteteachers(self, teaid):
        self.cursor.execute("DELETE FROM Teachertbl WHERE Teacher_Id = ?", (teaid,))
        self.conn.commit()
        # Check if any row was deleted
        if self.cursor.rowcount > 0:
            return True
        else:
            return False
        
    def deletestudent(self, stdid):
        self.cursor.execute("DELETE FROM Studenttbl WHERE Student_Id = ?", (stdid,))
        self.conn.commit()
        # Check if any row was deleted
        if self.cursor.rowcount > 0:
            return True
        else:
            return False
    
    