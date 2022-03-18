import sys
from PyQt5.QtWidgets import QApplication, QWidget
from xyz import Login, Register1, Register2, Homepage

app = QApplication(sys.argv)
login = Login()
register1 = Register1()
register2 = Register2()
home = Homepage()


def registerButtonAction():
    login.hide()
    register1.show()

def loginButtonAction():
    login.hide()
    home.show()

def nextButtonAction():
    register1.hide()
    register2.show()

def backButtonAction():
    register2.hide()
    register1.show()

def backButtonAction():
    register2.hide()
    register1.show()

login.bregister.clicked.connect(registerButtonAction)
login.blogin.clicked.connect(loginButtonAction)
register1.bnext.clicked.connect(nextButtonAction)
register2.bback.clicked.connect(backButtonAction)

login.show()

sys.exit(app.exec_())
