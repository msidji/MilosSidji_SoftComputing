# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\MainFrame.ui'
#
# Created: Wed Jan 20 22:44:04 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import notebookOperacije

#*****************************************************
import sys
from PyQt4 import QtCore, QtGui
from PyQt4 import*
from PyQt4.QtGui import QMainWindow
from Tkinter import *
import easygui

print(sys.version)
print(sys.executable)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 470)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        #tab prostor
        self.tabMainTab = QtGui.QTabWidget(self.centralwidget)
        self.tabMainTab.setGeometry(QtCore.QRect(0, 40, 581, 351))
        self.tabMainTab.setObjectName(_fromUtf8("tabMainTab"))
        self.tabMainTab.setStyleSheet('QTabBar::tab {background-color: red;}')       
    
        #tab1 ->
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))        
        self.tabMainTab.addTab(self.tab, _fromUtf8(""))
        
        #image unutar tab1
        self.labelImage = QtGui.QLabel(self.tab)
        self.labelImage.setGeometry(10, 10, 400, 100)
        myPixmap = QtGui.QPixmap(_fromUtf8('coverImage.gif'))
        #self.labelImage.width=100
       # self.labelImage.height=100
       # myScaledPixmap = QtGui.QPixmap()
        #myScaledPixmap = myPixmap.scaled(self.labelImage.size(), QtCore.Qt.KeepAspectRatio)
        self.labelImage.setPixmap(myPixmap)  
        print('pixmap', self.labelImage.pixmap())
        #self.labelImage.show()
        
        #tab2 ->
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))        
        self.tabMainTab.addTab(self.tab_2, _fromUtf8(""))
        
        #labela sa opisom teme projekta
        self.labelTema = QtGui.QLabel(self.centralwidget)
        self.labelTema.setGeometry(QtCore.QRect(0, 0, 241, 16))
        self.labelTema.setObjectName(_fromUtf8("labelTema"))
        
        #labela za ispis testova
        self.labelTest = QtGui.QLabel(self.centralwidget)
        self.labelTest.setGeometry(QtCore.QRect(0, 20, 241, 16))
        self.labelTest.setObjectName(_fromUtf8("labelTest"))        
        
        #buton za otvaranje odabrane slike
        self.btnChooseImage = QtGui.QPushButton(self.centralwidget)
        self.btnChooseImage.setGeometry(QtCore.QRect(0, 400, 81, 23))
        self.btnChooseImage.setObjectName(_fromUtf8("btnChooseImage"))
        
        #menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        
        #menuitem help
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        
        MainWindow.setMenuBar(self.menubar)
        
        #statusbar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #ACTIONS - begin **************************************************
        
        #About author menu item
        self.actionAboutAuthor=QtGui.QAction(MainWindow)
        self.actionAboutAuthor.setObjectName(_fromUtf8("actionAboutAuthor"))
        self.actionAboutAuthor.setShortcut("Ctrl+A")
        
        self.menuHelp.addAction(self.actionAboutAuthor)
        self.menubar.addAction(self.menuHelp.menuAction())
        #ACTIONS - end **************************************************

        self.retranslateUi(MainWindow)
        self.tabMainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Miloš Siđi RA 184/2012", None))
        self.tabMainTab.setTabText(self.tabMainTab.indexOf(self.tab), _translate("MainWindow", "1: Original", None))
        self.tabMainTab.setTabText(self.tabMainTab.indexOf(self.tab_2), _translate("MainWindow", "2: Grayscale", None))
        self.labelTema.setText(_translate("MainWindow", "Tema: Detekcija ivica puta i saobraćajnih znakova", None))
        self.labelTest.setText(_translate("MainWindow", "test", None))
        self.btnChooseImage.setText(_translate("MainWindow", "Choose Image", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAboutAuthor.setText(_translate("MainWindow", "About author", None))
       
       # setting actions
        self.btnChooseImage.clicked.connect(self.chooseImageFunction)
        self.btnChooseImage.setToolTip('Open image which you want to process')


    #functions
    def chooseImageFunction(self):
        path = easygui.fileopenbox()
        if path != '.':
            print('imagePath', path)
            myPixmap = QtGui.QPixmap(path)
            #myScaledPixmap = myPixmap.scaled(self.labelImage.size(), QtCore.Qt.KeepAspectRatio)
            self.labelImage.setPixmap(myPixmap)
            #self.tab.setPixmap(myScaledPixmap)
            print('OTVORENA SLIKA')
            self.labelTest.setText(_translate("MainWindow", "opened image", None))
            self.tabMainTab.setStyleSheet('QTabBar::tab {background-color: green;}')       

if  __name__ == '__main__':
    app=QtGui.QApplication(sys.argv) 
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    