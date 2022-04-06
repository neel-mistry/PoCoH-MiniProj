# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_profile(object):
    def setupUi(self, edit_profile):
        edit_profile.setObjectName("edit_profile")
        edit_profile.resize(1106, 936)
        self.centralwidget = QtWidgets.QWidget(edit_profile)
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
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/PoCoH.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_3.setStyleSheet("padding-bottom: 1em;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setStyleSheet("padding-top: 1em;\n"
"font: 500 12pt \"Poppins\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.name = QtWidgets.QLineEdit(self.frame_3)
        self.name.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:4px;\n"
"padding-left: 5px;")
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.verticalLayout_3.addWidget(self.name)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("padding-top: 1em;\n"
"font: 500 12pt \"Poppins\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignBottom)
        self.username = QtWidgets.QLineEdit(self.frame_3)
        self.username.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:4px;\n"
"padding-left: 5px;")
        self.username.setReadOnly(True)
        self.username.setObjectName("username")
        self.verticalLayout_3.addWidget(self.username)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setStyleSheet("padding-top: 1em;\n"
"font: 500 12pt \"Poppins\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignBottom)
        self.email = QtWidgets.QLineEdit(self.frame_3)
        self.email.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:4px;\n"
"padding-left: 5px;")
        self.email.setReadOnly(False)
        self.email.setObjectName("email")
        self.verticalLayout_3.addWidget(self.email)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setStyleSheet("padding-top: 1em;\n"
"font: 500 12pt \"Poppins\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignBottom)
        self.phone = QtWidgets.QLineEdit(self.frame_3)
        self.phone.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:4px;\n"
"padding-left: 5px;")
        self.phone.setObjectName("phone")
        self.verticalLayout_3.addWidget(self.phone)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setStyleSheet("padding-top: 1em;\n"
"font: 500 12pt \"Poppins\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.password = QtWidgets.QLineEdit(self.frame_3)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 12pt \"Poppins\";\n"
"border-bottom:2px solid #2a2a2a;\n"
"border-radius: 30px;\n"
"color:#2a2a2a;\n"
"padding-bottom:4px;\n"
"padding-left: 5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_3.addWidget(self.password)
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox.setStyleSheet("font: 300 11pt \"Poppins\";")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bsave = QtWidgets.QPushButton(self.frame_4)
        self.bsave.setStyleSheet("border-radius: 0.5em;\n"
"background-color: rgb(255, 174, 13);\n"
"padding-top: 0.30em;\n"
"padding-bottom: 0.30em;\n"
"padding-left: 1.7em;\n"
"padding-right: 1.7em;\n"
"font: 500 11pt \"Poppins\";")
        self.bsave.setObjectName("bsave")
        self.horizontalLayout.addWidget(self.bsave)
        self.bcancel = QtWidgets.QPushButton(self.frame_4)
        self.bcancel.setStyleSheet("QPushButton#bcancel{\n"
"border-radius: 0.5em;\n"
"border: 1px solid #e8e8e8;\n"
"padding-top: 0.30em;\n"
"padding-bottom: 0.30em;\n"
"padding-left: 1.7em;\n"
"padding-right: 1.7em;\n"
"font: 500 11pt \"Poppins\";\n"
"}\n"
"\n"
"QPushButton#bcancel:hover {\n"
"color:#090909;\n"
"background: #e8e8e8;\n"
"}")
        self.bcancel.setObjectName("bcancel")
        self.horizontalLayout.addWidget(self.bcancel)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        edit_profile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(edit_profile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 22))
        self.menubar.setObjectName("menubar")
        edit_profile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(edit_profile)
        self.statusbar.setObjectName("statusbar")
        edit_profile.setStatusBar(self.statusbar)

        self.retranslateUi(edit_profile)
        QtCore.QMetaObject.connectSlotsByName(edit_profile)

    def retranslateUi(self, edit_profile):
        _translate = QtCore.QCoreApplication.translate
        edit_profile.setWindowTitle(_translate("edit_profile", "MainWindow"))
        self.label_2.setText(_translate("edit_profile", "Name"))
        self.label_3.setText(_translate("edit_profile", "Username"))
        self.label_4.setText(_translate("edit_profile", "Email"))
        self.label_5.setText(_translate("edit_profile", "Phone Number"))
        self.label_6.setText(_translate("edit_profile", "Password"))
        self.checkBox.setText(_translate("edit_profile", "Show Password"))
        self.bsave.setText(_translate("edit_profile", "Save"))
        self.bcancel.setText(_translate("edit_profile", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_profile = QtWidgets.QMainWindow()
    ui = Ui_edit_profile()
    ui.setupUi(edit_profile)
    edit_profile.show()
    sys.exit(app.exec_())
