from PyQt5 import QtWidgets
from Login import Ui_Login
from homepage import Ui_homepage
from l_homepage import Ui_l_homepage
from register_new import Ui_register_new
from precautions import Ui_Precautions
from chickenpox import Ui_chickenpox
from covid_diet import Ui_covid_diet
from covid import Ui_covid
from edit_profile import Ui_edit_profile
from PyQt5 import QtCore, QtGui
from dengue import Ui_dengue
from PyQt5 import QtCore
from db import DatabaseConnection
from PyQt5.QtWidgets import QMessageBox

class Login(QtWidgets.QMainWindow,Ui_Login):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('PoCoH icon.jpg'))
 
    def login(self):
        usern = self.tusername.text()
        passw = self.tpass.text()

        dc = DatabaseConnection()
        cursor = dc.cursor()
        cursor.execute("select * from register where Username= '%s' and Pwd = '%s'",(usern,passw))
        a = cursor.fetchone #store data retrieved in result
        if a:
            QMessageBox.information(self,"You have logged in successfully")
            return 1
        else:
            QMessageBox.information(self,"Invalid User")   
            

class Homepage(QtWidgets.QMainWindow,Ui_homepage):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class EditProfile(QtWidgets.QMainWindow,Ui_edit_profile):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class L_Homepage(QtWidgets.QMainWindow,Ui_l_homepage):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class ChickenPox(QtWidgets.QMainWindow,Ui_chickenpox):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setupUi(self)

class Covid(QtWidgets.QMainWindow,Ui_covid):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setupUi(self)

class Dengue(QtWidgets.QMainWindow,Ui_dengue):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setupUi(self)

class N_Register(QtWidgets.QMainWindow,Ui_register_new):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        # self.bsubmit.clicked.connect(self.reg)

    # def reg(self):
    #     n = self.tname.text()
    #     em = self.temail.text()
    #     ph = self.tphone.text()
    #     dob = self.dateEdit.text()
    #     un = self.tusername.text()
    #     pw = self.tpass.text()
    #     re = self.trepass.text()

    #     db = DatabaseConnection()
    #     cursor = db.cursor()
    #     cursor.execute("select * from register where username= '"+un+"' and Pwd = '"+ pw +"' ")
    #     result = cursor.fetchone()

    #     if result:
    #         QtWidgets.QMessageBox.information(self, "Login form", "User already exists!")
    #     else:
    #         cursor.execute("insert into register values('"+ n +"','"+ em +"','"+ ph +"','"+ dob +"','"+ un +"','"+ pw +"','"+ re +"')")

    #         db.commit()
    #         QtWidgets.QMessageBox.information(self, "Login form", "Registered Successfully")

class Precautions(QtWidgets.QMainWindow,Ui_Precautions):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setupUi(self)
        self.setupUi(self)
