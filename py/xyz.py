from PyQt5 import QtWidgets
from Login import Ui_Login
from register1 import Ui_Register1
from register2 import Ui_Register2
from homepage import Ui_homepage
from l_homepage import Ui_l_homepage
from register_new import Ui_register_new
from precautions import Ui_Precautions
from db import DatabaseConnection

class Login(QtWidgets.QMainWindow,Ui_Login):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class Register1(QtWidgets.QMainWindow,Ui_Register1):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

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

class N_Register(QtWidgets.QMainWindow,Ui_register_new):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.bsubmit.clicked.connect(self.reg)

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
        cursor.execute("select * from register where username= '"+un+"' and Pwd = '"+ pw +"' ")
        result = cursor.fetchone()

        if result:
            QtWidgets.QMessageBox.information(self, "Login form", "User already exists!")
        else:
            cursor.execute("insert into register values('"+ n +"','"+ em +"','"+ ph +"','"+ dob +"','"+ un +"','"+ pw +"','"+ re +"')")

            db.commit()
            QtWidgets.QMessageBox.information(self, "Login form", "Registered Successfully")

class Precautions(QtWidgets.QMainWindow,Ui_Precautions):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
