# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/ProceduresProcessingForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProceduresProcessingForm(object):
    def setupUi(self, ProceduresProcessingForm):
        ProceduresProcessingForm.setObjectName("ProceduresProcessingForm")
        ProceduresProcessingForm.resize(1003, 418)
        self.centralwidget = QtWidgets.QWidget(ProceduresProcessingForm)
        self.centralwidget.setObjectName("centralwidget")
        self.nonIncludedProceduresTW = QtWidgets.QTableWidget(self.centralwidget)
        self.nonIncludedProceduresTW.setGeometry(QtCore.QRect(10, 50, 441, 301))
        self.nonIncludedProceduresTW.setObjectName("nonIncludedProceduresTW")
        self.nonIncludedProceduresTW.setColumnCount(0)
        self.nonIncludedProceduresTW.setRowCount(0)
        self.unincludeProcedureBut = QtWidgets.QToolButton(self.centralwidget)
        self.unincludeProcedureBut.setEnabled(True)
        self.unincludeProcedureBut.setGeometry(QtCore.QRect(460, 190, 61, 41))
        self.unincludeProcedureBut.setObjectName("unincludeProcedureBut")
        self.includeProcedureBut = QtWidgets.QToolButton(self.centralwidget)
        self.includeProcedureBut.setEnabled(True)
        self.includeProcedureBut.setGeometry(QtCore.QRect(460, 140, 61, 41))
        self.includeProcedureBut.setObjectName("includeProcedureBut")
        self.includedProceduresTW = QtWidgets.QTableWidget(self.centralwidget)
        self.includedProceduresTW.setGeometry(QtCore.QRect(530, 50, 461, 301))
        self.includedProceduresTW.setObjectName("includedProceduresTW")
        self.includedProceduresTW.setColumnCount(0)
        self.includedProceduresTW.setRowCount(0)
        self.nonIncludedLB = QtWidgets.QLabel(self.centralwidget)
        self.nonIncludedLB.setGeometry(QtCore.QRect(530, 20, 201, 16))
        self.nonIncludedLB.setObjectName("nonIncludedLB")
        self.includedLB = QtWidgets.QLabel(self.centralwidget)
        self.includedLB.setGeometry(QtCore.QRect(20, 20, 201, 16))
        self.includedLB.setObjectName("includedLB")
        self.backToCasesListBut = QtWidgets.QPushButton(self.centralwidget)
        self.backToCasesListBut.setGeometry(QtCore.QRect(460, 300, 61, 41))
        self.backToCasesListBut.setObjectName("backToCasesListBut")
        ProceduresProcessingForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProceduresProcessingForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 24))
        self.menubar.setObjectName("menubar")
        ProceduresProcessingForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProceduresProcessingForm)
        self.statusbar.setObjectName("statusbar")
        ProceduresProcessingForm.setStatusBar(self.statusbar)

        self.retranslateUi(ProceduresProcessingForm)
        QtCore.QMetaObject.connectSlotsByName(ProceduresProcessingForm)

    def retranslateUi(self, ProceduresProcessingForm):
        _translate = QtCore.QCoreApplication.translate
        ProceduresProcessingForm.setWindowTitle(_translate("ProceduresProcessingForm", "Изменение дела"))
        self.unincludeProcedureBut.setText(_translate("ProceduresProcessingForm", "<="))
        self.includeProcedureBut.setText(_translate("ProceduresProcessingForm", "=>"))
        self.nonIncludedLB.setText(_translate("ProceduresProcessingForm", "Включенные процедуры"))
        self.includedLB.setText(_translate("ProceduresProcessingForm", "Невключенные процедуры"))
        self.backToCasesListBut.setText(_translate("ProceduresProcessingForm", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProceduresProcessingForm = QtWidgets.QMainWindow()
    ui = Ui_ProceduresProcessingForm()
    ui.setupUi(ProceduresProcessingForm)
    ProceduresProcessingForm.show()
    sys.exit(app.exec_())
