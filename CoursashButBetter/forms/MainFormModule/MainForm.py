# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 333)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newCaseBut = QtWidgets.QPushButton(self.centralwidget)
        self.newCaseBut.setGeometry(QtCore.QRect(60, 40, 181, 41))
        self.newCaseBut.setAutoFillBackground(False)
        self.newCaseBut.setObjectName("newCaseBut")
        self.casesListBut = QtWidgets.QPushButton(self.centralwidget)
        self.casesListBut.setGeometry(QtCore.QRect(60, 90, 181, 41))
        self.casesListBut.setObjectName("casesListBut")
        self.exitBut = QtWidgets.QPushButton(self.centralwidget)
        self.exitBut.setGeometry(QtCore.QRect(60, 190, 181, 41))
        self.exitBut.setObjectName("exitBut")
        self.changeDataBut = QtWidgets.QPushButton(self.centralwidget)
        self.changeDataBut.setGeometry(QtCore.QRect(60, 140, 181, 41))
        self.changeDataBut.setObjectName("changeDataBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.newCaseBut.setText(_translate("MainWindow", "Новое дело"))
        self.casesListBut.setText(_translate("MainWindow", "Список дел"))
        self.exitBut.setText(_translate("MainWindow", "Выход"))
        self.changeDataBut.setText(_translate("MainWindow", "Изменить данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
