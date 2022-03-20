# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homepage(object):
    def setupUi(self, homepage):
        homepage.setObjectName("homepage")
        homepage.resize(919, 638)
        self.centralwidget = QtWidgets.QWidget(homepage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(88, 116, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.blogin = QtWidgets.QPushButton(self.frame_6)
        self.blogin.setStyleSheet("QPushButton#blogin{\n"
"font: 14pt \"Poppins\";\n"
" color: #090909;\n"
" border-radius: 0.5em;\n"
" background: #e8e8e8;\n"
" border: 1px solid #e8e8e8;\n"
" padding-left: 0.5em;\n"
" padding-right: 0.5em;\n"
"}\n"
"\n"
"\n"
"QPushButton#blogin:hover {\n"
"font: 14pt \"Poppins\";\n"
" border: 1px solid white;\n"
"}")
        self.blogin.setObjectName("blogin")
        self.horizontalLayout_4.addWidget(self.blogin)
        self.bsignup = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.bsignup.setFont(font)
        self.bsignup.setStyleSheet("QPushButton#bsignup{\n"
" font: 14pt \"Poppins\";\n"
" color: #ffffff;\n"
" border-radius: 0.5em;\n"
" border: 1px solid #e8e8e8;\n"
" padding-left: 0.5em;\n"
" padding-right: 0.5em;\n"
"}\n"
"\n"
"QPushButton#bsignup:hover {\n"
"font: 14pt \"Poppins\";\n"
" border: 1px solid white;\n"
"color:#090909;\n"
" background: #e8e8e8;\n"
"}\n"
"")
        self.bsignup.setObjectName("bsignup")
        self.horizontalLayout_4.addWidget(self.bsignup)
        self.horizontalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.home)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_11)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/PoCoH.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.horizontalLayout_6.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_9)
        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.home)
        self.precautions = QtWidgets.QWidget()
        self.precautions.setObjectName("precautions")
        self.stackedWidget.addWidget(self.precautions)
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.stackedWidget.addWidget(self.profile)
        self.exercises = QtWidgets.QWidget()
        self.exercises.setObjectName("exercises")
        self.stackedWidget.addWidget(self.exercises)
        self.diet = QtWidgets.QWidget()
        self.diet.setObjectName("diet")
        self.stackedWidget.addWidget(self.diet)
        self.homeremedies = QtWidgets.QWidget()
        self.homeremedies.setObjectName("homeremedies")
        self.stackedWidget.addWidget(self.homeremedies)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: #f6f6f6;\n"
"border-radius: 1.5em;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bhome = QtWidgets.QPushButton(self.frame_4)
        self.bhome.setMinimumSize(QtCore.QSize(0, 50))
        self.bhome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icons/c-home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bhome.setIcon(icon)
        self.bhome.setIconSize(QtCore.QSize(35, 35))
        self.bhome.setObjectName("bhome")
        self.horizontalLayout_5.addWidget(self.bhome)
        self.bprecautions = QtWidgets.QPushButton(self.frame_4)
        self.bprecautions.setMinimumSize(QtCore.QSize(0, 50))
        self.bprecautions.setStyleSheet("")
        self.bprecautions.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/icons/c-precautions.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bprecautions.setIcon(icon1)
        self.bprecautions.setIconSize(QtCore.QSize(35, 35))
        self.bprecautions.setObjectName("bprecautions")
        self.horizontalLayout_5.addWidget(self.bprecautions)
        self.bexercise = QtWidgets.QPushButton(self.frame_4)
        self.bexercise.setMinimumSize(QtCore.QSize(0, 50))
        self.bexercise.setStyleSheet("border: none;")
        self.bexercise.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/icons/c-exercise.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bexercise.setIcon(icon2)
        self.bexercise.setIconSize(QtCore.QSize(35, 35))
        self.bexercise.setObjectName("bexercise")
        self.horizontalLayout_5.addWidget(self.bexercise)
        self.bdiet = QtWidgets.QPushButton(self.frame_4)
        self.bdiet.setMinimumSize(QtCore.QSize(0, 50))
        self.bdiet.setStyleSheet("border: none;")
        self.bdiet.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/icons/c-diet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bdiet.setIcon(icon3)
        self.bdiet.setIconSize(QtCore.QSize(35, 35))
        self.bdiet.setObjectName("bdiet")
        self.horizontalLayout_5.addWidget(self.bdiet)
        self.bremedies = QtWidgets.QPushButton(self.frame_4)
        self.bremedies.setMinimumSize(QtCore.QSize(0, 50))
        self.bremedies.setStyleSheet("border: none;")
        self.bremedies.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/icons/c-home-remedies.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bremedies.setIcon(icon4)
        self.bremedies.setIconSize(QtCore.QSize(35, 35))
        self.bremedies.setObjectName("bremedies")
        self.horizontalLayout_5.addWidget(self.bremedies)
        self.bprofile = QtWidgets.QPushButton(self.frame_4)
        self.bprofile.setMinimumSize(QtCore.QSize(0, 50))
        self.bprofile.setStyleSheet("border: none;")
        self.bprofile.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/icons/profile-black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bprofile.setIcon(icon5)
        self.bprofile.setIconSize(QtCore.QSize(35, 35))
        self.bprofile.setObjectName("bprofile")
        self.horizontalLayout_5.addWidget(self.bprofile)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        homepage.setCentralWidget(self.centralwidget)

        self.retranslateUi(homepage)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(homepage)

    def retranslateUi(self, homepage):
        _translate = QtCore.QCoreApplication.translate
        homepage.setWindowTitle(_translate("homepage", "MainWindow"))
        self.blogin.setText(_translate("homepage", "Login"))
        self.bsignup.setText(_translate("homepage", "Sign Up"))
        self.label_2.setText(_translate("homepage", "An apple a day keeps the doctor away!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homepage = QtWidgets.QMainWindow()
    ui = Ui_homepage()
    ui.setupUi(homepage)
    homepage.show()
    sys.exit(app.exec_())
