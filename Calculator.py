import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.label_num1 = QtWidgets.QLabel(self)
        self.label_num1.setText("Sayı 1: ")
        self.label_num1.move(50,30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150,30)
        self.txt_num1.resize(200,32)

        self.label_num2 = QtWidgets.QLabel(self)
        self.label_num2.setText("Sayı 2: ")
        self.label_num2.move(50,80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150,80)
        self.txt_num2.resize(200,32)

def app():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

app()