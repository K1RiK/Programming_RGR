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

        self.light.clicked.connect(self.changeTheme)

        self.encode.clicked.connect(self.text_encode)
        self.decode.clicked.connect(self.text_decode)

        self.key.textChanged.connect(self.key_enter_delete)

    def result_text(self, func, key_only_int: bool = 0) -> str:
        key = self.key.toPlainText()
        itext = self.input.toPlainText()
        if key_only_int:
            self.output.setPlainText(func(itext, int(key)) if key.isdigit() else "Ошибка ключ должен быть числом!")
        else:
            self.output.setPlainText(func(itext, key))

    def key_enter_delete(self):
        text = self.key.toPlainText()
        if '\n' in text:
            self.key.setPlainText(text.replace('\n', ''))

    def changeTheme(self):
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

            self.footer_color = (18, 18, 18, .8)

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

            self.footer_color = (220, 220, 220, .8)

            self.theme_icon = "img/sun.png"

            self.light_color = (0, 0, 0)

        self.updateTheme(self)

    def text_encode(self):
        if self.code1.isChecked():
            self.result_text(cesar_encode, 1)
        elif self.code2.isChecked():
            self.result_text(crypto, 1)
        elif self.code3.isChecked():
            self.result_text(vigener_encode)
        elif self.code4.isChecked():
            self.result_text(encrypt_xor)

    def text_decode(self):
        if self.code1.isChecked():
            self.result_text(cesar_decode, 1)
        elif self.code2.isChecked():
            self.result_text(decrypto, 1)
        elif self.code3.isChecked():
            self.result_text(vigener_decode)
        elif self.code4.isChecked():
            self.result_text(encrypt_xor)


def main():
    if len(argv) == 1:
        app = QApplication(argv)
        main_window = MainWindow()

        main_window.show()
        exit(app.exec_())


if __name__ == '__main__':
    main()
