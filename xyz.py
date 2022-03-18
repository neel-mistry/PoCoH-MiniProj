from PyQt5 import QtWidgets
from Login import Ui_Login
from register1 import Ui_Register1
from register2 import Ui_Register2
from homepage import Ui_homepage

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