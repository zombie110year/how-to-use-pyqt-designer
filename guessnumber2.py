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
