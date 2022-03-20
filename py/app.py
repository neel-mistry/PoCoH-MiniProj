import sys
from tkinter import dialog
from PyQt5.QtWidgets import QApplication, QMessageBox
from xyz import Login, Register1, Register2, Homepage, L_Homepage 

app = QApplication(sys.argv)
login = Login()
register1 = Register1()
register2 = Register2()
home = Homepage()
l_home = L_Homepage()

def registerButtonAction():
    login.hide()
    register1.show()

def signupButtonAction():
    home.hide()
    register1.show()

def loginButtonAction():
    login.hide()
    l_home.show()

def loginButton1Action():
    home.hide()
    login.show()

def nextButtonAction():
    register1.hide()
    register2.show()

def backButtonAction():
    register2.hide()
    register1.show()

def backButtonAction():
    register2.hide()
    register1.show()

def warning_dialog():
    dialog = QMessageBox()
    dialog.setText('Please login to continue')
    dialog.setWindowTitle('Attention')
    dialog.setIcon(QMessageBox.Warning)
    dialog.exec_()

def showProfile():
    l_home.stackedWidget.setCurrentWidget(l_home.profile)

def showPrecautions():
    l_home.stackedWidget.setCurrentWidget(l_home.precautions)

def showRemedies():
    l_home.stackedWidget.setCurrentWidget(l_home.homeremedies)

def showExercises():
    l_home.stackedWidget.setCurrentWidget(l_home.exercises)

def showDiet():
    l_home.stackedWidget.setCurrentWidget(l_home.diet)

def showHome():
    l_home.stackedWidget.setCurrentWidget(l_home.home)


home.bsignup.clicked.connect(signupButtonAction)
home.blogin.clicked.connect(loginButton1Action)
login.bregister.clicked.connect(registerButtonAction)
login.blogin.clicked.connect(loginButtonAction)
register1.bnext.clicked.connect(nextButtonAction)
register2.bback.clicked.connect(backButtonAction)
home.bprecautions.clicked.connect(warning_dialog)
home.bexercise.clicked.connect(warning_dialog)
home.bdiet.clicked.connect(warning_dialog)
home.bremedies.clicked.connect(warning_dialog)
home.bprofile.clicked.connect(warning_dialog)
l_home.bprofile.clicked.connect(showProfile)
l_home.bprecautions.clicked.connect(showPrecautions)
l_home.bremedies.clicked.connect(showRemedies)
l_home.bexercise.clicked.connect(showExercises)
l_home.bdiet.clicked.connect(showDiet)
l_home.bhome.clicked.connect(showHome)

home.show()

sys.exit(app.exec_())
