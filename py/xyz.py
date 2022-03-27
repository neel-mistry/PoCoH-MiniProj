from PyQt5 import QtWidgets
from Login import Ui_Login
from register1 import Ui_Register1
from register2 import Ui_Register2
from homepage import Ui_homepage
from l_homepage import Ui_l_homepage
from db import DatabaseConnection

class Login(QtWidgets.QMainWindow,Ui_Login):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class Register1(QtWidgets.QMainWindow,Ui_Register1):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    def reg(self):
        n = self.tname.text()
        em = self.temail.text()
        ph = self.tphone.text()
        dob = self.dateEdit.text()
        un = self.tusername.text()
        pw = self.tpass.text()
        re = self.trepass.text()

        db = DatabaseConnection()
        cursor = db.cursor()
        cursor.execute("select * from userlist where username= '"+un+"' and password = '"+ pw +"' ")
        result = cursor.fetchone()

        if result:
            QMessageBox.information(self, "Login form", "User already exists!")
        else:
            cursor.execute("insert into register values('"+ n +"','"+ em +"','"+ ph +"','"+ dob +"','"+ un +"','"+ pw +"','"+ re +"')")

            db.commit()
            QMessageBox.information(self, "Login form", "Registered Successfully")

class Register2(QtWidgets.QMainWindow,Ui_Register2):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class Homepage(QtWidgets.QMainWindow,Ui_homepage):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class L_Homepage(QtWidgets.QMainWindow,Ui_l_homepage):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
