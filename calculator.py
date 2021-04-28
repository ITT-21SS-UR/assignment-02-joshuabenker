#!/usr/bin/python3
import sys
from PyQt5 import uic, QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QMainWindow


class Calculator (QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calculator.ui", self)
        self.init_buttons()

    def init_buttons(self):
        self.ui.button_zero.clicked.connect(lambda x: self.button_input('0'))
        self.ui.button_one.clicked.connect(lambda x: self.button_input('1'))
        self.ui.button_two.clicked.connect(lambda x: self.button_input('2'))
        self.ui.button_three.clicked.connect(lambda x: self.button_input('3'))
        self.ui.button_four.clicked.connect(lambda x: self.button_input('4'))
        self.ui.button_five.clicked.connect(lambda x: self.button_input('5'))
        self.ui.button_six.clicked.connect(lambda x: self.button_input('6'))
        self.ui.button_seven.clicked.connect(lambda x: self.button_input('7'))
        self.ui.button_eight.clicked.connect(lambda x: self.button_input('8'))
        self.ui.button_nine.clicked.connect(lambda x: self.button_input('9'))
        self.ui.button_decpoint.clicked.connect(lambda x: self.button_input('.'))

        self.ui.button_equals.clicked.connect(lambda x: self.button_input('='))
        self.ui.button_add.clicked.connect(lambda x: self.button_input('+'))
        self.ui.button_subtract.clicked.connect(lambda x: self.button_input('-'))
        self.ui.button_multiple.clicked.connect(lambda x: self.button_input('*'))
        self.ui.button_divide.clicked.connect(lambda x: self.button_input('/'))
        self.ui.button_clear.clicked.connect(lambda x: self.button_input('c'))
        self.ui.button_delete.clicked.connect(lambda x: self.button_input('d'))

    def calc_log(message):
        def log_event(func):
            def logging(self, text):
                self.log_message(message, text)
                func(self, text)
            return logging
        return log_event

    def log_message(self, message, text):
        numbers_operators = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/']
        if text in numbers_operators:
            sys.stdout.write(message + text + "\n")
        elif text == "c":
            sys.stdout.write(message + text + ". Input got cleared. \n")
        elif text == "d":
            sys.stdout.write(message + text + ". Last character deleted. \n")
        elif text == "=":
            to_calculate = self.ui.result.text()
            solution = eval(to_calculate)
            sys.stdout.write(message + text + ". Result: " + str(solution) + "\n")

    def keyPressEvent(self, event):
        numbers_operators = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/', '=']
        if event.text() in numbers_operators:
            self.key_input(event.text())
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.key_input('d')
        elif event.key() == QtCore.Qt.Key_Delete:
            self.key_input('c')
        elif event.key() == QtCore.Qt.Key_Return:
            self.key_input('=')

    @calc_log("key pressed: ")
    def key_input(self, char):
        self.calculator_output(char)

    @calc_log("button pressed: ")
    def button_input(self, char):
        self.calculator_output(char)

    def calculator_output(self, char):
        if char == '=':
            to_calculate = self.ui.result.text()
            solution = eval(to_calculate)
            self.ui.result.setText(str(solution))
        elif char == 'd':
            text = self.ui.result.text()
            self.ui.result.setText(text[0:len(text) - 1])
        elif char == 'c':
            self.ui.result.setText("")
        else:
            text = self.ui.result.text()
            self.ui.result.setText(text + char)


if __name__ == '__main__':
    app = Qt.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
