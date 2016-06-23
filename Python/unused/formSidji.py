# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import *
import sys
from PyQt4.QtGui import QMainWindow
from Tkinter import *
import easygui


print (sys.version)
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
        MainWindow.resize(800, 550)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 40, 181, 311))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(226, 20, 511, 331))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        #self.labelImage = QtGui.QLabel(self.tab)
        #myPixmap = QtGui.QPixmap("F:/Downloads/coverImage.jpg")
        #self.labelImage.height=365
        #self.labelImage.width=511
        #myScaledPixmap = myPixmap.scaled(511,365, QtCore.Qt.KeepAspectRatio)
        #self.labelImage.setPixmap(myScaledPixmap)

        self.tabWidget.addTab(self.tab,_fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))



        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 370, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 370, 381, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #toolbar 

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))

        exitActionToolbar=QtGui.QAction(QtGui.QIcon('exitIcon.png'),'Exit application',self)
        exitActionToolbar.triggered.connect(self.closeApplication)

        self.toolBar.addAction(exitActionToolbar)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        #####################################################################

        #Exit application menu item
        #self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit=QtGui.QAction(QtGui.QIcon('exitIcon.png'),'Exit application',self)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut("Ctrl+E")

        #####################################################################


        # About author menu item
        self.actionAboutAuthor=QtGui.QAction(MainWindow)
        self.actionAboutAuthor.setObjectName(_fromUtf8("actionAboutAuthor"))
        self.actionAboutAuthor.setShortcut("Ctrl+A")
        #####################################################################


        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAboutAuthor)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Processed image", None))
        self.pushButton.setText(_translate("MainWindow", "Choose image", None))
        self.label.setText(_translate("MainWindow", "Detected signs", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAboutAuthor.setText(_translate("MainWindow","About author",None))

        # setting actions

        self.pushButton.clicked.connect(self.chooseImageFunction)
        self.actionExit.triggered.connect(self.closeApplication)

        self.pushButton.setToolTip('Open image which you want to process')

        ##################################################################


    #functions
    def chooseImageFunction(self):
        path = easygui.fileopenbox()
        myPixmap = QtGui.QPixmap(path)
        myScaledPixmap = myPixmap.scaled(511,365, QtCore.Qt.KeepAspectRatio)
        self.labelImage.setPixmap(myScaledPixmap)
        self.lineEdit.setText(path)

    def closeApplication(self):

        choise=QtGui.QMessageBox.question(self,"Message","Do you want to close application?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choise == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    ###########################################################################
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    ex= Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())