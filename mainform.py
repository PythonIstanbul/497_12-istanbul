# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'işaret_dili_arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(QtCore.QSize(900, 650))
        MainWindow.setMaximumSize(QtCore.QSize(900, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(260, 70, 631, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Tekrarla = QtWidgets.QPushButton(self.centralwidget)
        self.Tekrarla.setGeometry(QtCore.QRect(20, 530, 230, 40))
        self.Tekrarla.setMinimumSize(QtCore.QSize(230, 40))
        self.Tekrarla.setMaximumSize(QtCore.QSize(230, 40))
        self.Tekrarla.setObjectName("Tekrarla")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 70, 231, 58))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Ara = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Ara.setMinimumSize(QtCore.QSize(40, 40))
        self.Ara.setMaximumSize(QtCore.QSize(40, 40))
        self.Ara.setObjectName("Ara")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Ara)
        self.ara = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.ara.setMinimumSize(QtCore.QSize(0, 40))
        self.ara.setMaximumSize(QtCore.QSize(16777215, 40))
        self.ara.setObjectName("ara")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ara)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 110, 231, 401))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 231, 331))
        self.listWidget.setObjectName("listWidget")
        self.Geri = QtWidgets.QPushButton(self.frame_3)
        self.Geri.setGeometry(QtCore.QRect(0, 0, 231, 31))
        self.Geri.setObjectName("Geri")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 140, 231, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 274))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.harfler = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.harfler.setContentsMargins(0, 0, 0, 0)
        self.harfler.setSpacing(3)
        self.harfler.setObjectName("harfler")
        self.V = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.V.setMinimumSize(QtCore.QSize(40, 40))
        self.V.setMaximumSize(QtCore.QSize(40, 40))
        self.V.setObjectName("V")
        self.harfler.addWidget(self.V, 5, 1, 1, 1)
        self.U_ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.U_.setMinimumSize(QtCore.QSize(40, 40))
        self.U_.setMaximumSize(QtCore.QSize(40, 40))
        self.U_.setObjectName("U_")
        self.harfler.addWidget(self.U_, 5, 0, 1, 1)
        self.Y = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Y.setMinimumSize(QtCore.QSize(40, 40))
        self.Y.setMaximumSize(QtCore.QSize(40, 40))
        self.Y.setObjectName("Y")
        self.harfler.addWidget(self.Y, 5, 2, 1, 1)
        self.Z = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Z.setMinimumSize(QtCore.QSize(40, 40))
        self.Z.setMaximumSize(QtCore.QSize(40, 40))
        self.Z.setObjectName("Z")
        self.harfler.addWidget(self.Z, 5, 3, 1, 1)
        self.Yardim = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Yardim.setMinimumSize(QtCore.QSize(40, 40))
        self.Yardim.setMaximumSize(QtCore.QSize(40, 40))
        self.Yardim.setObjectName("Yardim")
        self.harfler.addWidget(self.Yardim, 5, 4, 1, 1)
        self.S_ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.S_.setMinimumSize(QtCore.QSize(40, 40))
        self.S_.setMaximumSize(QtCore.QSize(40, 40))
        self.S_.setObjectName("S_")
        self.harfler.addWidget(self.S_, 4, 2, 1, 1)
        self.U = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.U.setMinimumSize(QtCore.QSize(40, 40))
        self.U.setMaximumSize(QtCore.QSize(40, 40))
        self.U.setObjectName("U")
        self.harfler.addWidget(self.U, 4, 4, 1, 1)
        self.G = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G.setMinimumSize(QtCore.QSize(40, 40))
        self.G.setMaximumSize(QtCore.QSize(40, 40))
        self.G.setObjectName("G")
        self.harfler.addWidget(self.G, 1, 2, 1, 1)
        self.H = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.H.setMinimumSize(QtCore.QSize(40, 40))
        self.H.setMaximumSize(QtCore.QSize(40, 41))
        self.H.setObjectName("H")
        self.harfler.addWidget(self.H, 1, 4, 1, 1)
        self.P = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.P.setMinimumSize(QtCore.QSize(40, 40))
        self.P.setMaximumSize(QtCore.QSize(40, 40))
        self.P.setObjectName("P")
        self.harfler.addWidget(self.P, 3, 4, 1, 1)
        self.A = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.A.setMinimumSize(QtCore.QSize(40, 40))
        self.A.setMaximumSize(QtCore.QSize(40, 40))
        self.A.setObjectName("A")
        self.harfler.addWidget(self.A, 0, 0, 1, 1)
        self.G_ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.G_.setMinimumSize(QtCore.QSize(40, 40))
        self.G_.setMaximumSize(QtCore.QSize(40, 40))
        self.G_.setObjectName("G_")
        self.harfler.addWidget(self.G_, 1, 3, 1, 1)
        self.I = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.I.setMinimumSize(QtCore.QSize(40, 40))
        self.I.setMaximumSize(QtCore.QSize(40, 40))
        self.I.setObjectName("I")
        self.harfler.addWidget(self.I, 2, 0, 1, 1)
        self.I_ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.I_.setMinimumSize(QtCore.QSize(40, 40))
        self.I_.setMaximumSize(QtCore.QSize(40, 40))
        self.I_.setObjectName("I_")
        self.harfler.addWidget(self.I_, 2, 1, 1, 1)
        self.E = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.E.setMinimumSize(QtCore.QSize(40, 40))
        self.E.setMaximumSize(QtCore.QSize(40, 40))
        self.E.setObjectName("E")
        self.harfler.addWidget(self.E, 1, 0, 1, 1)
        self.K = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.K.setMinimumSize(QtCore.QSize(40, 40))
        self.K.setMaximumSize(QtCore.QSize(40, 40))
        self.K.setObjectName("K")
        self.harfler.addWidget(self.K, 2, 3, 1, 1)
        self.M = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.M.setMinimumSize(QtCore.QSize(40, 40))
        self.M.setMaximumSize(QtCore.QSize(40, 40))
        self.M.setObjectName("M")
        self.harfler.addWidget(self.M, 3, 0, 1, 1)
        self.R = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.R.setMinimumSize(QtCore.QSize(40, 40))
        self.R.setMaximumSize(QtCore.QSize(40, 40))
        self.R.setObjectName("R")
        self.harfler.addWidget(self.R, 4, 0, 1, 1)
        self.D = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.D.setMinimumSize(QtCore.QSize(40, 40))
        self.D.setMaximumSize(QtCore.QSize(40, 40))
        self.D.setObjectName("D")
        self.harfler.addWidget(self.D, 0, 4, 1, 1)
        self.F = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.F.setMinimumSize(QtCore.QSize(40, 40))
        self.F.setMaximumSize(QtCore.QSize(40, 40))
        self.F.setObjectName("F")
        self.harfler.addWidget(self.F, 1, 1, 1, 1)
        self.N = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.N.setMinimumSize(QtCore.QSize(40, 40))
        self.N.setMaximumSize(QtCore.QSize(40, 40))
        self.N.setObjectName("N")
        self.harfler.addWidget(self.N, 3, 1, 1, 1)
        self.O_ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.O_.setMinimumSize(QtCore.QSize(40, 40))
        self.O_.setMaximumSize(QtCore.QSize(40, 40))
        self.O_.setObjectName("O_")
        self.harfler.addWidget(self.O_, 3, 3, 1, 1)
        self.J = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.J.setMinimumSize(QtCore.QSize(40, 40))
        self.J.setMaximumSize(QtCore.QSize(40, 40))
        self.J.setObjectName("J")
        self.harfler.addWidget(self.J, 2, 2, 1, 1)
        self.C = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C.setMinimumSize(QtCore.QSize(40, 40))
        self.C.setMaximumSize(QtCore.QSize(40, 40))
        self.C.setObjectName("C")
        self.harfler.addWidget(self.C, 0, 2, 1, 1)
        self.B = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B.setMinimumSize(QtCore.QSize(40, 40))
        self.B.setMaximumSize(QtCore.QSize(40, 40))
        self.B.setObjectName("B")
        self.harfler.addWidget(self.B, 0, 1, 1, 1)
        self.L = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.L.setMinimumSize(QtCore.QSize(40, 40))
        self.L.setMaximumSize(QtCore.QSize(40, 40))
        self.L.setObjectName("L")
        self.harfler.addWidget(self.L, 2, 4, 1, 1)
        self.S = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.S.setMinimumSize(QtCore.QSize(40, 40))
        self.S.setMaximumSize(QtCore.QSize(40, 40))
        self.S.setObjectName("S")
        self.harfler.addWidget(self.S, 4, 1, 1, 1)
        self.T = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.T.setMinimumSize(QtCore.QSize(40, 40))
        self.T.setMaximumSize(QtCore.QSize(40, 40))
        self.T.setObjectName("T")
        self.harfler.addWidget(self.T, 4, 3, 1, 1)
        self.C_ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.C_.setMinimumSize(QtCore.QSize(40, 40))
        self.C_.setMaximumSize(QtCore.QSize(40, 40))
        self.C_.setObjectName("C_")
        self.harfler.addWidget(self.C_, 0, 3, 1, 1)
        self.O = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.O.setMinimumSize(QtCore.QSize(40, 40))
        self.O.setMaximumSize(QtCore.QSize(40, 40))
        self.O.setObjectName("O")
        self.harfler.addWidget(self.O, 3, 2, 1, 1)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 270, 241, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Rastgele = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.Rastgele.setMinimumSize(QtCore.QSize(230, 40))
        self.Rastgele.setMaximumSize(QtCore.QSize(230, 40))
        self.Rastgele.setObjectName("Rastgele")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Rastgele)
        self.Hepsi = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.Hepsi.setMinimumSize(QtCore.QSize(230, 40))
        self.Hepsi.setMaximumSize(QtCore.QSize(234, 40))
        self.Hepsi.setObjectName("Hepsi")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Hepsi)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.A.clicked.connect(self.frame_2.hide)
        self.A.clicked.connect(self.frame_3.show)
        self.Geri.clicked.connect(self.frame_2.show)
        self.Geri.clicked.connect(self.frame_3.hide)
        self.B.clicked.connect(self.frame_3.show)
        self.B.clicked.connect(self.frame_2.hide)
        self.C.clicked.connect(self.frame_3.show)
        self.C.clicked.connect(self.frame_2.hide)
        self.C_.clicked.connect(self.frame_3.show)
        self.C_.clicked.connect(self.frame_2.hide)
        self.D.clicked.connect(self.frame_3.show)
        self.D.clicked.connect(self.frame_2.hide)
        self.E.clicked.connect(self.frame_3.show)
        self.E.clicked.connect(self.frame_2.hide)
        self.F.clicked.connect(self.frame_3.show)
        self.F.clicked.connect(self.frame_2.hide)
        self.G.clicked.connect(self.frame_3.show)
        self.G.clicked.connect(self.frame_2.hide)
        self.G_.clicked.connect(self.frame_3.show)
        self.G_.clicked.connect(self.frame_2.hide)
        self.H.clicked.connect(self.frame_3.show)
        self.H.clicked.connect(self.frame_2.hide)
        self.I.clicked.connect(self.frame_3.show)
        self.I.clicked.connect(self.frame_2.hide)
        self.I_.clicked.connect(self.frame_3.show)
        self.I_.clicked.connect(self.frame_2.hide)
        self.J.clicked.connect(self.frame_3.show)
        self.J.clicked.connect(self.frame_2.hide)
        self.K.clicked.connect(self.frame_3.show)
        self.K.clicked.connect(self.frame_2.hide)
        self.L.clicked.connect(self.frame_3.show)
        self.L.clicked.connect(self.frame_2.hide)
        self.M.clicked.connect(self.frame_3.show)
        self.M.clicked.connect(self.frame_2.hide)
        self.N.clicked.connect(self.frame_3.show)
        self.N.clicked.connect(self.frame_2.hide)
        self.O.clicked.connect(self.frame_3.show)
        self.O.clicked.connect(self.frame_2.hide)
        self.O_.clicked.connect(self.frame_3.show)
        self.O_.clicked.connect(self.frame_2.hide)
        self.P.clicked.connect(self.frame_3.show)
        self.R.clicked.connect(self.frame_2.hide)
        self.R.clicked.connect(self.frame_3.show)
        self.P.clicked.connect(self.frame_2.hide)
        self.S.clicked.connect(self.frame_3.show)
        self.S.clicked.connect(self.frame_2.hide)
        self.S_.clicked.connect(self.frame_2.hide)
        self.T.clicked.connect(self.frame_2.hide)
        self.T.clicked.connect(self.frame_3.show)
        self.U.clicked.connect(self.frame_3.show)
        self.U.clicked.connect(self.frame_2.hide)
        self.S_.clicked.connect(self.frame_3.show)
        self.U_.clicked.connect(self.frame_3.show)
        self.U_.clicked.connect(self.frame_2.hide)
        self.V.clicked.connect(self.frame_3.show)
        self.V.clicked.connect(self.frame_2.hide)
        self.Y.clicked.connect(self.frame_3.show)
        self.Y.clicked.connect(self.frame_2.hide)
        self.Z.clicked.connect(self.frame_3.show)
        self.Z.clicked.connect(self.frame_2.hide)
        self.Hepsi.clicked.connect(self.frame_3.show)
        self.Rastgele.clicked.connect(self.frame_3.show)
        self.Hepsi.clicked.connect(self.frame_2.hide)
        self.Rastgele.clicked.connect(self.frame_2.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 70, 421, 241))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tekrarla.setText(_translate("MainWindow", "TEKRARLA"))
        self.Ara.setText(_translate("MainWindow", "Ara"))
        self.Geri.setText(_translate("MainWindow", "Geri"))
        self.V.setText(_translate("MainWindow", "V"))
        self.U_.setText(_translate("MainWindow", "Ü"))
        self.Y.setText(_translate("MainWindow", "Y"))
        self.Z.setText(_translate("MainWindow", "Z"))
        self.Yardim.setText(_translate("MainWindow", "?"))
        self.S_.setText(_translate("MainWindow", "Ş"))
        self.U.setText(_translate("MainWindow", "U"))
        self.G.setText(_translate("MainWindow", "G"))
        self.H.setText(_translate("MainWindow", "H"))
        self.P.setText(_translate("MainWindow", "P"))
        self.A.setText(_translate("MainWindow", "A"))
        self.G_.setText(_translate("MainWindow", "Ğ"))
        self.I.setText(_translate("MainWindow", "I"))
        self.I_.setText(_translate("MainWindow", "İ"))
        self.E.setText(_translate("MainWindow", "E"))
        self.K.setText(_translate("MainWindow", "K"))
        self.M.setText(_translate("MainWindow", "M"))
        self.R.setText(_translate("MainWindow", "R"))
        self.D.setText(_translate("MainWindow", "D"))
        self.F.setText(_translate("MainWindow", "F"))
        self.N.setText(_translate("MainWindow", "N"))
        self.O_.setText(_translate("MainWindow", "Ö"))
        self.J.setText(_translate("MainWindow", "J"))
        self.C.setText(_translate("MainWindow", "C"))
        self.B.setText(_translate("MainWindow", "B"))
        self.L.setText(_translate("MainWindow", "L"))
        self.S.setText(_translate("MainWindow", "S"))
        self.T.setText(_translate("MainWindow", "T"))
        self.C_.setText(_translate("MainWindow", "Ç"))
        self.O.setText(_translate("MainWindow", "O"))
        self.Rastgele.setText(_translate("MainWindow", "RASTGELE"))
        self.Hepsi.setText(_translate("MainWindow", "HEPSİ"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
def Ui_MainWindow_open(self):
    if MainWindow.exec_()==True:
        Frame_3.hide()

    Ui_MainWindow_open()
