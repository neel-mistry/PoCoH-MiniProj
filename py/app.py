import sys
import re
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox
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
chickenpox = ChickenPox()
covid = Covid()
dengue = Dengue()
editprofile = EditProfile()

# ----------------- NAMING WINDOWS ----------------- 
home.setWindowTitle("PoCoH: Please login or register to continue")
login.setWindowTitle("PoCoH: Login")
register.setWindowTitle("PoCoH: Register")
l_home.setWindowTitle("Welcome to PoCoH")

# ----------------- VALIDATIONS -----------------
def email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return 1
        else:
            return 2

def phone(phone):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    if(re.fullmatch(Pattern, phone)):
        return 1
    else:
        return 2

def password(password_check):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compiling regex
    pat = re.compile(reg)
      
    # searching regex                 
    mat = re.search(pat, password_check)
      
    # validating conditions
    if mat:
        return 1
    else:
        return 2

# ----------------- START WINDOW CODES -----------------
def signupButtonAction():
    home.hide()
    register.show()

def loginButton1Action():
    home.hide()
    login.show()

# ----------------- HOMEPAGE WINDOW CODES -----------------
def okayButtonAction():
    precautions.hide()

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
    login.tusername.setText("")
    login.tpass.setText("")
    login.show()

def editprof():
    editprofile.show()

def canceButtonAction():
    editprofile.hide()

# def saveButtonAction():
#     usern = editprofile.username.text()
#     phno = editprofile.phone.text()
#     passwd = editprofile.password.text()
#     emailid = editprofile.email.text()
#     dc = DatabaseConnection()
#     cursor = dc.cursor()
#     cursor.execute(f"update register set email = '{emailid}', mobile = '{phno}', Pwd = '{passwd}' from register where Username='{usern}';")

# ----------------- LOGIN WINDOW CODES -----------------
def registerButtonAction():
    login.hide()
    register.show()

def loginButtonAction():
    flag = 0
    # if xyz.Login.login == 1:
    #     l_home.show()
    #     login.hide()
    # else: 
    #     dialog = QMessageBox()
    #     dialog.setText('Please login to continue')
    #     dialog.setWindowTitle('Attention')
    #     dialog.setIcon(QMessageBox.Warning)
    #     dialog.exec_()
    if login.tusername.text() == "" or login.tpass.text() == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Enter userid and pass!")
        msg.setWindowTitle("Error")
        msg.exec_()
    
    else:
        flag = 1

    if flag == 1:
        usern = login.tusername.text()
        passw = login.tpass.text()
        dc = DatabaseConnection()
        cursor = dc.cursor()
        cursor.execute(f"select * from register where Username='{usern}' and Pwd ='{passw}';")
        result = cursor.fetchone()
        if result:
            l_home.name.setText(result[0])
            l_home.email.setText(result[1])
            l_home.mobile.setText(str(result[2]))
            l_home.dob.setText(result[3])
            l_home.username.setText(result[4]) 
            editprofile.name.setText(result[0])
            editprofile.email.setText(result[1])
            editprofile.phone.setText(str(result[2]))
            editprofile.username.setText(result[4]) 
            editprofile.password.setText(result[5]) 
            login.hide()
            l_home.show()
            precautions.show()
            
        else:
            dialog = QMessageBox()
            dialog.setText('Invalid login id or pass')
            dialog.setWindowTitle('Attention!')
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()



def warning_dialog():
    dialog = QMessageBox()
    dialog.setText('Please login to continue')
    dialog.setWindowTitle('Attention')
    dialog.setIcon(QMessageBox.Warning)
    dialog.exec_()


# ----------------- DIET WINDOW CODES -----------------
def viewdiet1ButtonAction():
    covid.show()
    
def viewdiet2ButtonAction():
    chickenpox.show()

def viewdiet3ButtonAction():
    dengue.show() 

def cbackButtonAction():
    chickenpox.hide()
    dengue.hide()
    covid.hide()

   
# ----------------- WORKOUT WINDOW CODES -----------------
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
# ----------------- REMEDIES WINDOW CODES -----------------



# ----------------- REGISTRATION WINDOW CODES -----------------

def submitButtonAction():
    flag_s = 0
    n = register.tname.text()
    em = register.temail.text()
    ph = register.tphone.text()
    dob = register.dateEdit.text()
    un = register.tusername.text()
    pw = register.tpass.text()
    re = register.trepass.text()

    if register.tname.text() == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Enter name!")
        msg.setWindowTitle("Error")
        msg.exec_()
        # flag_s = False
    elif register.temail.text() == "":
        print("email empty")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Enter Email!")
        msg.setWindowTitle("Error")
        msg.exec_()
        #flag_s = False

    elif email(register.temail.text()) == 2:
        dialog = QMessageBox()
        dialog.setText('Invalid email!!')
        dialog.setWindowTitle('Attention!')
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()
        #flag_s = False
    
    elif phone(register.tphone.text()) == 2:
        dialog = QMessageBox()
        dialog.setText('Invalid phone!!')
        dialog.setWindowTitle('Attention!')
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()
        #flag_s = False
    
    elif register.tpass.text() != register.trepass.text():
        dialog = QMessageBox()
        dialog.setText("Passwords don't match")
        #dialog.setInformativeText('shdfls')
        dialog.setWindowTitle('Attention!')
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()
    
    elif password(register.tpass.text()) == 2:
        dialog = QMessageBox()
        dialog.setText('Password criteria not met!')
        dialog.setInformativeText("1. Should have at least one number.\n"
        "2. Should have at least one uppercase and one lowercase character.\n" 
        "3. Should have at least one special symbol.\n" 
        "4. Should be between 6 to 20 characters long.")
        dialog.setWindowTitle('Attention!')
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()
        #flag_s = False
        
    else:
        flag_s = 1


    if flag_s == 1:
        db = DatabaseConnection()
        cursor = db.cursor()
        cursor.execute("select * from register where username= '"+un+"' and Pwd = '"+ pw +"' ")
        result = cursor.fetchone()

        if result:
            dialog = QMessageBox()
            dialog.setText("Username already exists")
            dialog.setWindowTitle('Attention!')
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()    
        else:
            cursor.execute("insert into register values('"+ n +"','"+ em +"','"+ ph +"','"+ dob +"','"+ un +"','"+ pw +"','"+ re +"')")
            db.commit()
            #QtWidgets.QMessageBox.information("Login form", "Registered Successfully")
            login.show()
            register.hide()

def backButtonAction():
    register.tname.setText("")
    register.temail.setText("")
    register.tphone.setText("")
    #register.dateEdit.setText("")
    register.tusername.setText("")
    register.tpass.setText("")
    register.trepass.setText("")
    register.hide()
    login.show()


# ----------------- SHOW PASSWORD -----------------     

def checkBoxChangedAction():
        if (login.checkBox.isChecked()):
            login.tpass.setEchoMode(login.tpass.EchoMode.Normal)
        else:
            login.tpass.setEchoMode(login.tpass.EchoMode.Password)

def checkBoxChangedAction2():
        if (register.checkBox.isChecked()):
            register.tpass.setEchoMode(register.tpass.EchoMode.Normal)
            register.trepass.setEchoMode(register.trepass.EchoMode.Normal)
        else:
            register.tpass.setEchoMode(register.tpass.EchoMode.Password)
            register.trepass.setEchoMode(register.trepass.EchoMode.Password)

def checkBoxChangedAction3():
        if (editprofile.checkBox.isChecked()):
            editprofile.password.setEchoMode(login.tpass.EchoMode.Normal)
        else:
            editprofile.password.setEchoMode(login.tpass.EchoMode.Password)


# ----------------- FUNCTION CALLING -----------------     
         
login.checkBox.stateChanged.connect(checkBoxChangedAction)
register.checkBox.stateChanged.connect(checkBoxChangedAction2)
editprofile.checkBox.stateChanged.connect(checkBoxChangedAction3)
#editprofile.bsave.clicked.connect(saveButtonAction)
home.bsignup.clicked.connect(signupButtonAction)
home.blogin.clicked.connect(loginButton1Action)
login.bregister.clicked.connect(registerButtonAction)
login.blogin.clicked.connect(loginButtonAction)
home.bexercise.clicked.connect(warning_dialog)
home.bdiet.clicked.connect(warning_dialog)
home.bremedies.clicked.connect(warning_dialog)
home.bprofile.clicked.connect(warning_dialog)
home.label_2.setText(quotes.selected)
l_home.bprofile.clicked.connect(showProfile)
l_home.bremedies.clicked.connect(showRemedies)
l_home.bexercise.clicked.connect(showExercises)
l_home.bdiet.clicked.connect(showDiet)
l_home.bhome.clicked.connect(showHome)
l_home.blogout.clicked.connect(logoutButtonAction)
l_home.blogout_2.clicked.connect(logoutButtonAction)
l_home.url1.clicked.connect(url1ButtonAction)
l_home.url2.clicked.connect(url2ButtonAction)
l_home.url3.clicked.connect(url3ButtonAction)
l_home.url4.clicked.connect(url4ButtonAction)
l_home.url5.clicked.connect(url5ButtonAction)
l_home.url6.clicked.connect(url6ButtonAction)
l_home.viewdiets2.clicked.connect(viewdiet2ButtonAction)
l_home.beditprof.clicked.connect(editprof)
editprofile.bcancel.clicked.connect(canceButtonAction)
chickenpox.cbokay.clicked.connect(cbackButtonAction)
chickenpox.cbback.clicked.connect(cbackButtonAction)
dengue.cbokay.clicked.connect(cbackButtonAction)
dengue.cbback.clicked.connect(cbackButtonAction)
covid.cbokay.clicked.connect(cbackButtonAction)
covid.cbback.clicked.connect(cbackButtonAction)
l_home.viewdiets1.clicked.connect(viewdiet1ButtonAction)
l_home.viewdiets3.clicked.connect(viewdiet3ButtonAction)
l_home.label_2.setText(quotes.selected)
precautions.bok.clicked.connect(okayButtonAction)
register.bback.clicked.connect(backButtonAction)
register.bsubmit.clicked.connect(submitButtonAction)


# for i in range(2):
#     img = "E:\1. College\SE\Sem 4\proj materials"
#     iter = str(i)
#     con = img + iter
#     l_home.label_21.setPixmap(qtg.QPixmap(img))
#     time.sleep(10)

home.show()

sys.exit(app.exec_())
