# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName("DialogAbout")
        DialogAbout.resize(368, 232)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source/img/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAbout.setWindowIcon(icon)
        DialogAbout.setStyleSheet("background-color: rgb(255, 255, 255);")
        DialogAbout.setModal(True)
        self.label = QtWidgets.QLabel(DialogAbout)
        self.label.setGeometry(QtCore.QRect(20, 10, 194, 52))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DialogAbout)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 90, 241, 91))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet("")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(DialogAbout)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        _translate = QtCore.QCoreApplication.translate
        DialogAbout.setWindowTitle(_translate("DialogAbout", "About"))
        self.label.setText(_translate("DialogAbout", "<html><head/><body><p><img src=\":/source/img/ico.png\" width=\"40\" height=\"40\"/><span style=\" font-size:16pt; font-weight:600;color:rgb(0, 0, 150)\">ScopeModbus</span></p></body></html>"))
        self.plainTextEdit.setPlainText(_translate("DialogAbout", "Version:"))
import pyimg_rc
