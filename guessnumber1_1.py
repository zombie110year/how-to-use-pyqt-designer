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
