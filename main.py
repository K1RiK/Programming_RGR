# -*- coding: utf-8 -*-
import sys

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

            self.key.textChanged.connect(self.key_enter_delete)

            self.input_file.clicked.connect(self.input_text_from_file)
            self.output_file.clicked.connect(self.save_file_with_text)
        else:
            self.itext = ''
            self.ofile = ''
            self.ikey = ''
            self.action_func = None
            self.otext = ''

    def result_text(self, func, key_only_int: bool = 0, cmd_mode: int = 0) -> str:
        """ Возвращает обработаный текст.
            Шифрует текст заданной функцией с проверкой ключа при заданном ключе key_only_int на то,
            является ли он числом. В графическом режиме cmd_mode = 0 выводит текст в поле для вывода"""
        if cmd_mode:
            key = self.ikey
            itext = self.itext
        else:
            key = self.key.toPlainText()
            itext = self.input.toPlainText()

        if key_only_int:
            result = func(itext, int(key)) if key.isdigit() else "Ошибка ключ должен быть числом!"
        else:
            result = func(itext, key)

        if not cmd_mode:
            self.output.setPlainText(result)
        return result

    def key_enter_delete(self):
        """ Проверяет поле ввода ключа на наличие переноса строки и удаляет его при его наличии """
        text = self.key.toPlainText()
        if '\n' in text:
            self.key.setPlainText(text.replace('\n', ''))

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
        text = self.open_file()
        self.input.setPlainText(text)

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

    def set_itext(self, text_or_file: str = 'text'):
        """ Устанавливает входной текст в консольном режиме из параметра или файла
            в соответствии с параметром text_or_file """
        if not self.itext:
            if text_or_file == 'text':
                self.itext = self.current_arg
            elif text_or_file == 'file':
                try:
                    with open(self.current_arg, 'r', encoding='utf-8') as file:
                        self.itext = file.read()
                except Exception as _ex:
                    if _ex == FileNotFoundError:
                        print(f'Файл {self.current_arg} не найден!')
        else:
            print('Разрешено использовать только один из следующих флагов -i -itext -if -ifile и только один раз')

    def set_ofile(self):
        """ Устанавливает имя файла для сохранения выходного текста в консольном режиме"""
        if not self.ofile:
            self.ofile = self.current_arg
        else:
            print('Разрешено использовать только один из следующих флагов -o -ofile и только один раз')

    def set_ikey(self):
        """ Устанавливает ключ в консольном режиме """
        if not self.ikey:
            self.ikey = self.current_arg
        else:
            print('Разрешено только один следующий флаг -key')

    def argparse(self, args: list[str]) -> int:
        """ Парсим агрументы при запуске из консоли и в соответствии с флагами
            и их параметрами возвращаем результат """
        flags_with_args_list = ('-i', '-itext', '-if', '-ifile', '-o', '-ofile', '-key')
        flags_without_args_list = ('--cesar_encode', '--cesar_decode', '--multitable_encode', '--multitable_encode',
                                   '--vigener_encode', '--vigener_decode', '--xor')
        if '--help' in args:
            print("""Шифрует или дешифрует текст по одному из методов шифрования:\n
                    \r    Шифр Цезаря (ключ должен быть числом)
                    \r    Шифр замены с умножением (ключ должен быть числом)
                    \r    Шифр Виженера
                    \r    XOR шифрование\n
                    \rДоступные флаги:
                    \r
                    \r    Для большей надёжности указывайте значение флагов в одинарных или двойных кавычках
                    \r
                    \r    При шифровании рекомендуется сохранять результат в файл,
                    \r    так как некоторые символы в консоли могут отображаться некорректно
                    \r
                    \r    --help                         Выводит данное сообщение
                    \r    -i   -itext  "Текст"           Принимает на вход текст для шифрования/дешифрования
                    \r    -if  -ifile  "Путь до файла"   Принимает на вход файл для шифрования/дешифрования
                    \r    -o   -ofile  "Название файла"  Сохраняет вывод в файл
                    \r    -key         "Ключ"            Ключ для шифрования\n
                    \r    --cesar_encode                 Зашифровать шифром Цезаря
                    \r    --cesar_decode                 Расшифровать шифр цезаря\n
                    \r    --multitable_encode            Зашифровать шифром замены с умножением
                    \r    --multitable_decode            Расшифровать шифр замены с умножением\n
                    \r    --vigener_encode               Зашифровать шифром Виженера
                    \r    --vigener_decode               Расшифровать шифр Виженера\n
                    \r    --xor                          Зашифровать/Расшифровать XOR шифр""")
            return 0
        for i, arg in enumerate(args):
            try:
                self.current_arg = args[i + 1]
            except:
                if arg in flags_with_args_list:
                    print(f'Значение аргумента для флага {arg} не может быть пустым')
                    return 1

            if arg in flags_with_args_list:
                if arg in ('-i', '-itext'):
                    self.set_itext('text')
                if arg in ('-if', '-ifile'):
                    self.set_itext('file')
                if arg in ('-o', '-ofile'):
                    self.set_ofile()
                if arg == '-key':
                    self.set_ikey()
            elif arg in flags_without_args_list:
                if arg == '--cesar_encode':
                    self.action_func = cesar_encode
                elif arg == '--cesar_decode':
                    self.action_func = cesar_decode
                elif arg == '--multitable_encode':
                    self.action_func = crypto
                elif arg == '--multitable_decode':
                    self.action_func = decrypto
                elif arg == '--xor':
                    self.action_func = encrypt_xor
        if not self.action_func:
            print('Укажите один из следующих типов действия --cesar_encode --cesar_decode --multitable_encode\
                  \n\r--multitable_encode --vigener_encode --vigener_decode --xor')
        elif self.action_func and self.ikey:
            if 'cesar' in self.action_func.__name__ or 'multitable' in self.action_func.__name__:
                self.otext = self.result_text(self.action_func, 1, cmd_mode=1)
            else:
                self.otext = self.result_text(self.action_func, 0, cmd_mode=1)
        if not self.itext:
            print('Укажите агрумент для одного следующих флагов -i -itext -if -ifile')
        if self.otext:
            if not self.ofile:
                print(f"Исходный текст: {self.itext}",
                      f"Результат операции: {self.otext}", sep='\n')
            else:
                print(f"Исходный текст: {self.itext}")
                try:
                    with open(self.ofile, 'w+', encoding='utf-8') as file:
                        file.write(self.otext)
                except Exception as _ex:
                    print(f"Ошибка сохранения результата в файл! {_ex}")
                    return -1
                print(f"Результат успешно сохранен в файл {self.ofile}")

        if not self.ikey:
            print('Укажите агрумент для флага -key')
        return 0


def main():
    args = sys.argv[1::]
    if len(args) == 0:
        app = QApplication(args)
        main_window = MainWindow()

        main_window.show()
        sys.exit(app.exec_())
    else:
        main_window = MainWindow(gui_mode=0)
        main_window.argparse(args)


if __name__ == '__main__':
    main()
