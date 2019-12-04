# PyQt5 如何利用 Qt Designer

当使用 QtDesigner 编辑了界面后，有三种方式将它加载到代码

## 1. 使用 PyQt5.uic.loadUi

loadUi 接收两个参数：ui 文件路径和代码中的基类对象，用于将 ui 文件中的配置加载到传入的对象上。

1. 基类对象要求与 ui 文件中的基类拥有相同的类型
2. ui 文件中定义的子对象会被创建并赋值为基类对象的属性

这种方法可以做到 界面-逻辑 分离，但由于 Python 为解释性语言，如果 ui 文件保存为独立的文件，
那么在打包时可能会带来麻烦，需要对打包工具进行特殊的设置，将 ui 文件包含在包内；同时也需要将
代码中 loadUi 传入的路径修改为相对于包的路径，否则会从运行程序的当前工作目录开始寻找，这可能和
预期想法不一致。

对于本项目使用的猜数字游戏，从代码文件 `guessnumber1.py` 可以看到使用了这种方法。

```py
# guessnumber1.py
import sys
from random import randint

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic import loadUi


# Qt Designer 中的基类为 QMainWindow，
# 则我们要使用的对象必须是 QMainWindow 或它的子类
class GuessNumberMainWindow(QMainWindow):
    # 为了方便IDE提供代码自动补全，在这里添加属性的类型标注
    # 这些对象在 Qt Designer 中拥有相同的命名
    GameDescription: QLabel
    SubmitButton: QPushButton
    AnswerInputArea: QLineEdit

    ANSWER: int

    def __init__(self):
        super().__init__()
        # 使用 loadUi 将 ui 文件中的属性加载到 self 上
        loadUi("ui/guessnumber.ui", self)
        # 由于 QtDesigner 中编辑信号-槽不方便
        # 所以在这里手动编辑
        self.SubmitButton.clicked.connect(self.AnswerInputArea.copy)
        self.SubmitButton.clicked.connect(self.check_answer)
        self.init_answer()

    def init_answer(self):
        "准备好答案"
        self.ANSWER = randint(0, 100)
        print(f"{self.ANSWER=}")

    def check_answer(self):
        "检查答案"
        guess = int(self.AnswerInputArea.text().strip())
        if guess < self.ANSWER:
            QMessageBox.about(self, "检查答案", f"{guess} 小了")
        elif guess > self.ANSWER:
            QMessageBox.about(self, "检查答案", f"{guess} 大了")
        else:
            QMessageBox.about(self, "恭喜", "回答正确，进入下一轮！")
            self.AnswerInputArea.clear()
            self.init_answer()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GuessNumberMainWindow()
    w.show()
    sys.exit(app.exec())

```

## 2. 用 PyQt5.uic 将 ui 文件转换成 Python 代码

PyQt5 提供了 pyuic5 这个命令行工具用于将 Designer 编辑的 ui 文件转换成 Python 代码。
会根据 ui 文件中的内容产生一个名为 `Ui_*` 的类。

```sh
pyuic5 -o guessnumber_ui.py
```

```py
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

```

`Ui_*` 类拥有 `setupUi` 方法，在使用时将需要被设置的基类传入。实际上 loadUi 方法和这个方法做了相类似的事。
只不过 `Ui_` 的 setupUi 方法将子对象绑定到 `Ui_` 类的实例上了，而 loadUi 是绑定到传入的对象上。

这导致要引用界面上的子控件，需要引用 `Ui_` 实例。一般在代码中绑定为基类的 .ui 属性。

```py
# guessnumber1.py
import sys
from random import randint

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton

from guessnumber_ui import Ui_GuessNumberWindow

# Qt Designer 中的基类为 QMainWindow，
# 则我们要使用的对象必须是 QMainWindow 或它的子类


# 为了方便IDE自动补全，定义一个子类并添加类型标注
class UI_GuessNumberWindow(Ui_GuessNumberWindow):
    GameDescription: QLabel
    SubmitButton: QPushButton
    AnswerInputArea: QLineEdit


class GuessNumberWindow(QMainWindow):
    ANSWER: int

    def __init__(self):
        super().__init__()
        # 由于 Ui_* 将子对象加载到它身上了，
        # 因此为了引用这些子对象，也得将 Ui_* 实例挂载
        # 为基类的属性
        self.ui = UI_GuessNumberWindow()
        self.ui.setupUi(self)
        # 由于 QtDesigner 中编辑信号-槽不方便
        # 所以在这里手动编辑
        # 注意， SubmitButton 等对象是 Ui_GuessNumberWindow 的属性
        self.ui.SubmitButton.clicked.connect(self.ui.AnswerInputArea.copy)
        self.ui.SubmitButton.clicked.connect(self.check_answer)
        self.init_answer()

    def init_answer(self):
        "准备好答案"
        self.ANSWER = randint(0, 100)
        print(f"{self.ANSWER=}")

    def check_answer(self):
        "检查答案"
        guess = int(self.ui.AnswerInputArea.text().strip())
        if guess < self.ANSWER:
            QMessageBox.about(self, "检查答案", f"{guess} 小了")
        elif guess > self.ANSWER:
            QMessageBox.about(self, "检查答案", f"{guess} 大了")
        else:
            QMessageBox.about(self, "恭喜", "回答正确，进入下一轮！")
            self.ui.AnswerInputArea.clear()
            self.init_answer()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GuessNumberWindow()
    w.show()
    sys.exit(app.exec())

```

用这种方法的话，没有对 ui 文件路径的依赖。

## 1.1 用 loadUi 方法，更彻底的界面/逻辑分离

界面单独创建一个类，逻辑创建另一个类。
将界面类的实例挂载为逻辑类的一个属性。

```py
# guessnumber1_1.py
import sys
from random import randint

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic import loadUi


class GuessNumberWindow(QMainWindow):
    # 为了方便IDE提供代码自动补全，在这里添加属性的类型标注
    # 这些对象在 Qt Designer 中拥有相同的命名
    GameDescription: QLabel
    SubmitButton: QPushButton
    AnswerInputArea: QLineEdit


class GuessNumberApp:
    ANSWER: int

    def __init__(self):
        self.ui = GuessNumberWindow()
        # 使用 loadUi 将 ui 文件中的属性加载到 self.ui 上
        loadUi("ui/guessnumber.ui", self.ui)
        # 由于 QtDesigner 中编辑信号-槽不方便
        # 所以在这里手动编辑
        self.ui.SubmitButton.clicked.connect(self.ui.AnswerInputArea.copy)
        self.ui.SubmitButton.clicked.connect(self.check_answer)
        self.init_answer()

    def init_answer(self):
        "准备好答案"
        self.ANSWER = randint(0, 100)
        print(f"{self.ANSWER=}")

    def check_answer(self):
        "检查答案"
        guess = int(self.ui.AnswerInputArea.text().strip())
        if guess < self.ANSWER:
            QMessageBox.about(self.ui, "检查答案", f"{guess} 小了")
        elif guess > self.ANSWER:
            QMessageBox.about(self.ui, "检查答案", f"{guess} 大了")
        else:
            QMessageBox.about(self.ui, "恭喜", "回答正确，进入下一轮！")
            self.ui.AnswerInputArea.clear()
            self.init_answer()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GuessNumberApp()
    w.ui.show()
    sys.exit(app.exec())

```

## 什么是信号-槽机制

简单理解，信号：一个事件发生产生一个信号；槽：接收这个信号并做出反应。

从代码上看，就是设置当一个事件发生时调用一个函数。
