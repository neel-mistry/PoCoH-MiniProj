from PyQt5 import QtWidgets
from Login import Ui_Login
from register1 import Ui_Register1
from register2 import Ui_Register2
from homepage import Ui_homepage
from l_homepage import Ui_l_homepage
from register_new import Ui_register_new

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