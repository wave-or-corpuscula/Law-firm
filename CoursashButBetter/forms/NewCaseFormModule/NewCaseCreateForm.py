# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/NewCaseCreateForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewCaseForm(object):
    def setupUi(self, NewCaseForm):
        NewCaseForm.setObjectName("NewCaseForm")
        NewCaseForm.resize(612, 453)
        self.centralwidget = QtWidgets.QWidget(NewCaseForm)
        self.centralwidget.setObjectName("centralwidget")
        self.caseDataSW = QtWidgets.QStackedWidget(self.centralwidget)
        self.caseDataSW.setGeometry(QtCore.QRect(10, 10, 591, 421))
        self.caseDataSW.setObjectName("caseDataSW")
        self.clientChoicePage = QtWidgets.QWidget()
        self.clientChoicePage.setObjectName("clientChoicePage")
        self.clientsTable = QtWidgets.QTableWidget(self.clientChoicePage)
        self.clientsTable.setGeometry(QtCore.QRect(0, 20, 591, 331))
        self.clientsTable.setObjectName("clientsTable")
        self.clientsTable.setColumnCount(0)
        self.clientsTable.setRowCount(0)
        self.label = QtWidgets.QLabel(self.clientChoicePage)
        self.label.setGeometry(QtCore.QRect(20, 0, 141, 16))
        self.label.setObjectName("label")
        self.continueBut = QtWidgets.QPushButton(self.clientChoicePage)
        self.continueBut.setGeometry(QtCore.QRect(470, 360, 121, 31))
        self.continueBut.setObjectName("continueBut")
        self.backToMainBut = QtWidgets.QPushButton(self.clientChoicePage)
        self.backToMainBut.setGeometry(QtCore.QRect(340, 360, 121, 31))
        self.backToMainBut.setObjectName("backToMainBut")
        self.caseDataSW.addWidget(self.clientChoicePage)
        self.dateChoicePage = QtWidgets.QWidget()
        self.dateChoicePage.setObjectName("dateChoicePage")
        self.calendarCW = QtWidgets.QCalendarWidget(self.dateChoicePage)
        self.calendarCW.setGeometry(QtCore.QRect(10, 40, 321, 241))
        self.calendarCW.setObjectName("calendarCW")
        self.nominalPriceLE = QtWidgets.QLineEdit(self.dateChoicePage)
        self.nominalPriceLE.setGeometry(QtCore.QRect(20, 320, 231, 31))
        self.nominalPriceLE.setObjectName("nominalPriceLE")
        self.addCaseBut = QtWidgets.QPushButton(self.dateChoicePage)
        self.addCaseBut.setGeometry(QtCore.QRect(420, 320, 141, 31))
        self.addCaseBut.setObjectName("addCaseBut")
        self.backToClientChoiceBut = QtWidgets.QPushButton(self.dateChoicePage)
        self.backToClientChoiceBut.setGeometry(QtCore.QRect(290, 320, 101, 31))
        self.backToClientChoiceBut.setObjectName("backToClientChoiceBut")
        self.label_2 = QtWidgets.QLabel(self.dateChoicePage)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 19))
        self.label_2.setObjectName("label_2")
        self.caseDescrLe = QtWidgets.QTextEdit(self.dateChoicePage)
        self.caseDescrLe.setGeometry(QtCore.QRect(340, 40, 231, 241))
        self.caseDescrLe.setObjectName("caseDescrLe")
        self.caseDataSW.addWidget(self.dateChoicePage)
        NewCaseForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewCaseForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 24))
        self.menubar.setObjectName("menubar")
        NewCaseForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewCaseForm)
        self.statusbar.setObjectName("statusbar")
        NewCaseForm.setStatusBar(self.statusbar)

        self.retranslateUi(NewCaseForm)
        self.caseDataSW.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NewCaseForm)

    def retranslateUi(self, NewCaseForm):
        _translate = QtCore.QCoreApplication.translate
        NewCaseForm.setWindowTitle(_translate("NewCaseForm", "Новое дело"))
        self.label.setText(_translate("NewCaseForm", "Выберите клиента:"))
        self.continueBut.setText(_translate("NewCaseForm", "Далее"))
        self.backToMainBut.setText(_translate("NewCaseForm", "Назад"))
        self.nominalPriceLE.setPlaceholderText(_translate("NewCaseForm", "Номинальная цена улуги"))
        self.addCaseBut.setText(_translate("NewCaseForm", "Добавить дело"))
        self.backToClientChoiceBut.setText(_translate("NewCaseForm", "Назад"))
        self.label_2.setText(_translate("NewCaseForm", "Дата начала дела:"))
        self.caseDescrLe.setPlaceholderText(_translate("NewCaseForm", "Описание дела"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewCaseForm = QtWidgets.QMainWindow()
    ui = Ui_NewCaseForm()
    ui.setupUi(NewCaseForm)
    NewCaseForm.show()
    sys.exit(app.exec_())