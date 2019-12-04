# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\guessnumber.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GuessNumberWindow(object):
    def setupUi(self, GuessNumberWindow):
        GuessNumberWindow.setObjectName("GuessNumberWindow")
        GuessNumberWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(GuessNumberWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.AnswerInputArea = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.AnswerInputArea.setInputMask("")
        self.AnswerInputArea.setAlignment(QtCore.Qt.AlignCenter)
        self.AnswerInputArea.setObjectName("AnswerInputArea")
        self.gridLayout.addWidget(self.AnswerInputArea, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.SubmitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SubmitButton.setObjectName("SubmitButton")
        self.gridLayout.addWidget(self.SubmitButton, 5, 1, 1, 1)
        self.GameDescription = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.GameDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.GameDescription.setObjectName("GameDescription")
        self.gridLayout.addWidget(self.GameDescription, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 5, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        GuessNumberWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GuessNumberWindow)
        self.SubmitButton.clicked.connect(self.AnswerInputArea.copy)
        QtCore.QMetaObject.connectSlotsByName(GuessNumberWindow)
        GuessNumberWindow.setTabOrder(self.AnswerInputArea, self.SubmitButton)

    def retranslateUi(self, GuessNumberWindow):
        _translate = QtCore.QCoreApplication.translate
        GuessNumberWindow.setWindowTitle(_translate("GuessNumberWindow", "MainWindow"))
        self.SubmitButton.setText(_translate("GuessNumberWindow", "提交"))
        self.GameDescription.setText(_translate("GuessNumberWindow", "猜数字：0-100"))
