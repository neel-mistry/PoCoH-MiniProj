from msilib.schema import SelfReg
import sys, time
from Login import Ui_Login
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication, QMessageBox
import xyz
from xyz import *
from quotes import Quotes
from db import DatabaseConnection
from PyQt5.Qt import QApplication, QUrl, QDesktopServices

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
    # if xyz.Login.login == 1:
    #     l_home.show()
    #     login.hide()
    # else: 
    #     dialog = QMessageBox()
    #     dialog.setText('Please login to continue')
    #     dialog.setWindowTitle('Attention')
    #     dialog.setIcon(QMessageBox.Warning)
    #     dialog.exec_()
    usern = login.tusername.text()
    passw = login.tpass.text()
    print(usern)
    print(passw)
    dc = DatabaseConnection()
    cursor = dc.cursor()
    cursor.execute("select * from register where Username= %s and Pwd = %s",(usern,passw))
    a = cursor.fetchone #store data retrieved in result
    if a:
        login.hide()
        l_home.show()
        precautions.show()
    else:
        dialog = QMessageBox()
        dialog.setText('Please login to continue')
        dialog.setWindowTitle('Attention')
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()

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

def submitButtonAction():
    login.show()

def backButtonAction():
    register.hide()
    login.show()

def url1ButtonAction():
    url = QUrl("https://www.youtube.com/watch?v=zUFS_SAkovc")
    QDesktopServices.openUrl(url)

def url2ButtonAction():
    url = QUrl("https://youtu.be/6QXqnNDI-uo")
    QDesktopServices.openUrl(url)

def url3ButtonAction():
    url = QUrl("https://youtu.be/omZATEKkl-I")
    QDesktopServices.openUrl(url)

def url4ButtonAction():
    url = QUrl("https://youtu.be/DYVXSBTtY9c")
    QDesktopServices.openUrl(url)

def url5ButtonAction():
    url = QUrl("https://youtu.be/JhHn5PI82oU")
    QDesktopServices.openUrl(url)

def url6ButtonAction():
    url = QUrl("https://youtu.be/-jd;ok")
    QDesktopServices.openUrl(url)                

l_home.url1.clicked.connect(url1ButtonAction)
l_home.url2.clicked.connect(url2ButtonAction)
l_home.url3.clicked.connect(url3ButtonAction)
l_home.url4.clicked.connect(url4ButtonAction)
l_home.url5.clicked.connect(url5ButtonAction)
l_home.url6.clicked.connect(url6ButtonAction)

home.setWindowTitle("PoCoH: Please login or register to continue")
login.setWindowTitle("PoCoH: Login")
register.setWindowTitle("PoCoH: Register")
l_home.setWindowTitle("Welcome to PoCoH")

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
l_home.blogout_2.clicked.connect(logoutButtonAction)
precautions.bok.clicked.connect(okayButtonAction)
register.bback.clicked.connect(backButtonAction)
l_home.label_2.setText(quotes.selected)
home.label_2.setText(quotes.selected)

# for i in range(2):
#     img = "E:\1. College\SE\Sem 4\proj materials"
#     iter = str(i)
#     con = img + iter
#     l_home.label_21.setPixmap(qtg.QPixmap(img))
#     time.sleep(10)

home.show()

sys.exit(app.exec_())
