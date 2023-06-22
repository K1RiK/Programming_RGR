# -*- coding: utf-8 -*-
from sys import exit
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from gui import Ui_MainWindow
from cesar import cesar_encode, cesar_decode
from multimy import crypto, decrypto
from vigener import vigener_encode, vigener_decode
from xor_crypt import encrypt_xor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, gui_mode: int = 1):
        if gui_mode:
            super().__init__()
            self.setupUi(self)

            self.light.clicked.connect(self.changeTheme)

            self.encode.clicked.connect(self.text_encode)
            self.decode.clicked.connect(self.text_decode)

            self.input_file.clicked.connect(self.input_text_from_file)
            self.output_file.clicked.connect(self.save_file_with_text)

    def result_text(self, func, key_only_int: bool = 0) -> str:
        """ Шифрует текст заданной функцией с проверкой ключа при заданном ключе key_only_int
            на то, является ли он числом. """
        key = self.key.text()
        itext = self.input.toPlainText()

        if key_only_int:
            result = func(itext, int(key)) if key.isdigit() else "Ошибка ключ должен быть числом!"
        else:
            result = func(itext, key)

        self.output.setPlainText(result)

    def open_file(self, text: str = '', action: str = 'r') -> str:
        filename = QFileDialog.getOpenFileName(self, 'Выбор файла', '', 'Text files (*.txt)')[0]
        if filename == '' or filename.split('.')[-1] != 'txt':
            return ''
        with open(filename, action, encoding='utf-8') as file:
            if action == 'r':
                return file.read()
            elif action == 'w+':
                file.write(text)
                return 'Текст успешно сохранен в файл'

    def input_text_from_file(self):
        self.input.setPlainText(self.open_file())

    def save_file_with_text(self):
        self.open_file(self.output.toPlainText(), action='w+')

    def changeTheme(self):
        """ Меняет тему с темной на светлую и наоборот """
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

        self.updateTheme(self)

    def text_encode(self):
        """ Шифрует текст исходя из выбранного типа шифрования """
        if self.code1.isChecked():
            self.result_text(cesar_encode, 1)
        elif self.code2.isChecked():
            self.result_text(crypto, 1)
        elif self.code3.isChecked():
            self.result_text(vigener_encode)
        elif self.code4.isChecked():
            self.result_text(encrypt_xor)

    def text_decode(self):
        """ Дешифрует текст исходя из выбранного типа шифрования """
        if self.code1.isChecked():
            self.result_text(cesar_decode, 1)
        elif self.code2.isChecked():
            self.result_text(decrypto, 1)
        elif self.code3.isChecked():
            self.result_text(vigener_decode)
        elif self.code4.isChecked():
            self.result_text(encrypt_xor)


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
