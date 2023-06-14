# -*- coding: utf-8 -*-
from sys import exit, argv

from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow
from cesar import cesar_encode, cesar_decode
from multymy import crypto, decrypto
from vigener import vigener_encode, vigener_decode
from xor_crypt import encrypt_xor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateTheme(self)

        self.light.clicked.connect(self.changeTheme)
        
        self.encode.clicked.connect(self.text_encode)
        self.decode.clicked.connect(self.text_decode)

        self.key.textChanged.connect(self.test)

    def test(self):
        text = self.key.toPlainText()
        if '\n' in text:
            self.key.setPlainText(text.replace('\n', ''))

    def changeTheme(self):  # TODO Сделать переключение тем
        if self.theme == 'dark':
            self.theme = 'light'

            self.main_backgroundcolor = (220, 220, 220)

            self.io_color = (8, 8, 8)
            self.io_backgroundcolor = (255, 255, 255, 0.9)

            self.codes_color = (16, 16, 16)

            self.decode_color = (16, 16, 16)
            self.decode_border_color = (190, 190, 190)
            self.decode_backgroundcolor = (200, 200, 200)
            self.decode_hover_backgroundcolor = (190, 190, 190)
            self.decode_pressed_backgroundcolor = (180, 180, 180)

            self.footer_color = (18, 18, 18)

            self.theme_icon = "img/moon.png"

            self.light_color = (250, 250, 250)
        elif self.theme == 'light':
            self.theme = 'dark'

            self.main_backgroundcolor = (16, 16, 16)

            self.io_color = (220, 220, 220)
            self.io_backgroundcolor = (32, 32, 32, 0.9)

            self.codes_color = (220, 220, 220)

            self.decode_color = (240, 240, 240)
            self.decode_border_color = (30, 30, 30)
            self.decode_backgroundcolor = (20, 20, 20)
            self.decode_hover_backgroundcolor = (30, 30, 30)
            self.decode_pressed_backgroundcolor = (15, 15, 15)

            self.footer_color = (220, 220, 220)

            self.theme_icon = "img/sun.png"

            self.light_color = (0, 0, 0)

        self.updateTheme(self)

    def text_encode(self):  # TODO Сделать 4 шифрования текста
        key = self.key.toPlainText()
        input_text = self.input.toPlainText()
        output = ''
        if self.code1.isChecked():
            if key.isdigit():
                output = cesar_encode(input_text, int(key))
            else:
                output = "Ошибка ключ должен быть числом!"
        elif self.code2.isChecked():
            if key.isdigit():
                output = crypto(input_text, int(key))
            else:
                output = "Ошибка ключ должен быть числом!"
        elif self.code3.isChecked():
            output = vigener_encode(input_text, key)
        elif self.code4.isChecked():
            output = encrypt_xor(input_text, key)
        self.output.setPlainText(output)

    def text_decode(self):  # TODO Сделать 4 расшифрования текста
        key = self.key.toPlainText()
        input_text = self.input.toPlainText()
        output = ''
        if self.code1.isChecked():
            if key.isdigit():
                output = cesar_decode(input_text, int(key))
            else:
                output = "Ошибка ключ должен быть числом!"
        elif self.code2.isChecked():
            if key.isdigit():
                output = decrypto(input_text, int(key))
            else:
                output = "Ошибка ключ должен быть числом!"
        elif self.code3.isChecked():
            output = vigener_decode(input_text, key)
        elif self.code4.isChecked():
            output = encrypt_xor(input_text, key)
        self.output.setPlainText(output)


def main():
    if len(argv) == 1:
        app = QApplication(argv)
        main_window = MainWindow()

        main_window.show()
        exit(app.exec_())


if __name__ == '__main__':
    main()
