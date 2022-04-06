# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'precautions.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Precautions(object):
    def setupUi(self, Precautions):
        Precautions.setObjectName("Precautions")
        Precautions.resize(833, 556)
        self.centralwidget = QtWidgets.QWidget(Precautions)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_6)
        self.frame.setStyleSheet("background-color: rgb(88, 116, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("font: 700 22pt \"Poppins\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(18, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setStyleSheet("font: 600 16pt \"Poppins\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignVCenter)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(18, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 500 12pt \"Poppins\";")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bok = QtWidgets.QPushButton(self.frame_5)
        self.bok.setStyleSheet("QPushButton#bok{\n"
"font: 10pt \"Poppins\";\n"
"padding-top: 0.25em;\n"
"padding-bottom: 0.25em;\n"
"padding-right: 1em;\n"
"padding-left: 1em;\n"
" color: #090909;\n"
" border-radius: 0.5em;\n"
" background: #e8e8e8;\n"
" border: 1px solid #e8e8e8;\n"
"}\n"
"\n"
"QPushButton#bok:hover {\n"
"font: 10pt \"Poppins\";\n"
" border: 1px solid white;\n"
"}")
        self.bok.setObjectName("bok")
        self.verticalLayout_4.addWidget(self.bok)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        Precautions.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Precautions)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 22))
        self.menubar.setObjectName("menubar")
        Precautions.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Precautions)
        self.statusbar.setObjectName("statusbar")
        Precautions.setStatusBar(self.statusbar)

        self.retranslateUi(Precautions)
        QtCore.QMetaObject.connectSlotsByName(Precautions)

    def retranslateUi(self, Precautions):
        _translate = QtCore.QCoreApplication.translate
        Precautions.setWindowTitle(_translate("Precautions", "MainWindow"))
        self.label.setText(_translate("Precautions", "Precautions for COVID - 19"))
        self.label_2.setText(_translate("Precautions", "To prevent the spread of COVID-19:"))
        self.label_3.setText(_translate("Precautions", "1. Maintain a safe distance from others (at least 1 metre), even if they don’t appear to be sick.\n"
"2. Wear a mask in public, especially indoors or when physical distancing is not possible.\n"
"3. Choose open, well-ventilated spaces over closed ones. Open a window if indoors.\n"
"4. Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n"
"5. Get vaccinated when it’s your turn. Follow local guidance about vaccination.\n"
"6. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
"7. Stay home if you feel unwell."))
        self.bok.setText(_translate("Precautions", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Precautions = QtWidgets.QMainWindow()
    ui = Ui_Precautions()
    ui.setupUi(Precautions)
    Precautions.show()
    sys.exit(app.exec_())
