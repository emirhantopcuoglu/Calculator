import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowIcon(QIcon("calculator.png"))
        self.initUI()

    def initUI(self):
        self.label_num1 = QtWidgets.QLabel(self)
        self.label_num1.setText("Sayı 1: ")
        self.label_num1.move(50, 30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150, 30)
        self.txt_num1.resize(200, 32)

        self.label_num2 = QtWidgets.QLabel(self)
        self.label_num2.setText("Sayı 2: ")
        self.label_num2.move(50, 80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150, 80)
        self.txt_num2.resize(200, 32)

        self.button_add = QtWidgets.QPushButton(self)
        self.button_add.setText("Topla")
        self.button_add.move(150, 130)
        self.button_add.clicked.connect(self.calculate)

        self.button_sub = QtWidgets.QPushButton(self)
        self.button_sub.setText("Çıkar")
        self.button_sub.move(150, 170)
        self.button_sub.clicked.connect(self.calculate)

        self.button_mul = QtWidgets.QPushButton(self)
        self.button_mul.setText("Çarp")
        self.button_mul.move(150, 210)
        self.button_mul.clicked.connect(self.calculate)

        self.button_div = QtWidgets.QPushButton(self)
        self.button_div.setText("Böl")
        self.button_div.move(150, 250)
        self.button_div.clicked.connect(self.calculate)

        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setText("Sonuç: ")
        self.label_result.move(150, 290)
        self.label_result.resize(200, 32)

    def calculate(self):
        sender = self.sender().text()
        result = 0
        if sender == "Topla":
            result = float(self.txt_num1.text()) + float(self.txt_num2.text())
        elif sender == "Çıkar":
            result = float(self.txt_num1.text()) - float(self.txt_num2.text())
        elif sender == "Çarp":
            result = float(self.txt_num1.text()) * float(self.txt_num2.text())
        elif sender == "Böl":
            if float(self.txt_num1.text()) == 0 and float(self.txt_num2.text()) == 0:
                result = "Belirsiz"
            elif float(self.txt_num1.text()) != 0 and float(self.txt_num2.text()) == 0:
                result = "Tanımsız"
            else:
                result = float(self.txt_num1.text()) / float(self.txt_num2.text())
        self.label_result.setText("Sonuç: " + str(result))


def app():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


app()
