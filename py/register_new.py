# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register-new.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_new(object):
    def setupUi(self, register_new):
        register_new.setObjectName("register_new")
        register_new.resize(960, 818)
        self.centralwidget = QtWidgets.QWidget(register_new)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(88, 116, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_7)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/PoCoH.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 600 18pt \"Poppins SemiBold\";")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("padding-top: 0.65em;\n"
"font: 14pt \"Poppins\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tname = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tname.setFont(font)
        self.tname.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:7px;\n"
"padding-left:5px;")
        self.tname.setObjectName("tname")
        self.verticalLayout_2.addWidget(self.tname)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("padding-top: 0.65em;\n"
"font: 14pt \"Poppins\";")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.temail = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.temail.setFont(font)
        self.temail.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-bottom:2px solid #2a2a2a;\n"
"font: 12pt \"Poppins\";\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:7px;\n"
"padding-left:5px;")
        self.temail.setObjectName("temail")
        self.verticalLayout_2.addWidget(self.temail)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("padding-top: 0.65em;\n"
"font: 14pt \"Poppins\";")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.tphone = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tphone.setFont(font)
        self.tphone.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:7px;\n"
"padding-left:5px;")
        self.tphone.setObjectName("tphone")
        self.verticalLayout_2.addWidget(self.tphone)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("padding-top: 0.65em;\n"
"padding-bottom: 0.2em;\n"
"font: 14pt \"Poppins\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("font: 12pt \"Poppins\";")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMaximumSize(QtCore.QSize(2, 16777215))
        self.frame_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 600 18pt \"Poppins SemiBold\";")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.tusername = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tusername.setFont(font)
        self.tusername.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:7px;")
        self.tusername.setObjectName("tusername")
        self.verticalLayout_3.addWidget(self.tusername)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.tpass = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tpass.setFont(font)
        self.tpass.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:7px;")
        self.tpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tpass.setObjectName("tpass")
        self.verticalLayout_3.addWidget(self.tpass)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.trepass = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.trepass.setFont(font)
        self.trepass.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-bottom:2px solid #2a2a2a;\n"
"font: 12pt \"Poppins\";\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:7px;")
        self.trepass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.trepass.setObjectName("trepass")
        self.verticalLayout_3.addWidget(self.trepass)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.bsubmit = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.bsubmit.setFont(font)
        self.bsubmit.setStyleSheet("QPushButton#bsubmit{\n"
"padding-top: 0.25em;\n"
"padding-bottom: 0.25em;\n"
"padding-right: 0.95em;\n"
"padding-left: 0.95em;\n"
"font: 14pt \"Poppins\";\n"
" color: #090909;\n"
" font-size: 18px;\n"
" border-radius: 0.5em;\n"
" background: #e8e8e8;\n"
" border: 1px solid #e8e8e8;\n"
"}\n"
"\n"
"QPushButton#bsubmit:hover {\n"
" border: 1px solid white;\n"
"}\n"
"")
        self.bsubmit.setObjectName("bsubmit")
        self.verticalLayout_6.addWidget(self.bsubmit)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        register_new.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(register_new)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 22))
        self.menubar.setObjectName("menubar")
        register_new.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(register_new)
        self.statusbar.setObjectName("statusbar")
        register_new.setStatusBar(self.statusbar)

        self.retranslateUi(register_new)
        QtCore.QMetaObject.connectSlotsByName(register_new)

    def retranslateUi(self, register_new):
        _translate = QtCore.QCoreApplication.translate
        register_new.setWindowTitle(_translate("register_new", "MainWindow"))
        self.label_9.setText(_translate("register_new", "REGISTER"))
        self.label_13.setText(_translate("register_new", "Section 1: Personal Information"))
        self.label_6.setText(_translate("register_new", "Name"))
        self.tname.setPlaceholderText(_translate("register_new", "Enter your name"))
        self.label_11.setText(_translate("register_new", "Email"))
        self.temail.setPlaceholderText(_translate("register_new", "Enter your email"))
        self.label_12.setText(_translate("register_new", "Phone Number"))
        self.tphone.setPlaceholderText(_translate("register_new", "Enter your phone number"))
        self.label_10.setText(_translate("register_new", "Date of Birth"))
        self.label_2.setText(_translate("register_new", "TextLabel"))
        self.label_14.setText(_translate("register_new", "Section 2: Login Credentials"))
        self.label_5.setText(_translate("register_new", "Username"))
        self.tusername.setPlaceholderText(_translate("register_new", "  Create username"))
        self.label_7.setText(_translate("register_new", "Password"))
        self.tpass.setPlaceholderText(_translate("register_new", "  Create password"))
        self.label_8.setText(_translate("register_new", "Re-Enter Password"))
        self.trepass.setPlaceholderText(_translate("register_new", "  Re-Enter password"))
        self.bsubmit.setText(_translate("register_new", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_new = QtWidgets.QMainWindow()
    ui = Ui_register_new()
    ui.setupUi(register_new)
    register_new.show()
    sys.exit(app.exec_())