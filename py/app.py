import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from xyz import Login, Homepage, L_Homepage, N_Register, Precautions 
from quotes import Quotes

app = QApplication(sys.argv)
login = Login()
home = Homepage()
l_home = L_Homepage()
register =  N_Register()
precautions = Precautions()
quotes = Quotes()

def registerButtonAction():
    login.hide()
    register.show()

def okayButtonAction():
    precautions.hide()

def signupButtonAction():
    home.hide()
    register.show()

def loginButtonAction():
    login.hide()
    l_home.show()
    precautions.show()

def loginButton1Action():
    home.hide()
    login.show()

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

def logoutButtonAction():
    l_home.hide()
    login.show()


home.bsignup.clicked.connect(signupButtonAction)
home.blogin.clicked.connect(loginButton1Action)
login.bregister.clicked.connect(registerButtonAction)
login.blogin.clicked.connect(loginButtonAction)
home.bexercise.clicked.connect(warning_dialog)
home.bdiet.clicked.connect(warning_dialog)
home.bremedies.clicked.connect(warning_dialog)
home.bprofile.clicked.connect(warning_dialog)
l_home.bprofile.clicked.connect(showProfile)
l_home.bremedies.clicked.connect(showRemedies)
l_home.bexercise.clicked.connect(showExercises)
l_home.bdiet.clicked.connect(showDiet)
l_home.bhome.clicked.connect(showHome)
l_home.blogout.clicked.connect(logoutButtonAction)
precautions.bok.clicked.connect(okayButtonAction)
l_home.label_2.setText(quotes.selected)
home.label_2.setText(quotes.selected)

home.show()

sys.exit(app.exec_())
