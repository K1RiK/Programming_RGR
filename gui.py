# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.theme = 'dark'

        self.io_color = (220, 220, 220)
        self.io_backgroundcolor = (32, 32, 32, 0.9)

        self.codes_color = (220, 220, 220)

        self.decode_color = (240, 240, 240)
        self.decode_border_color = (30, 30, 30)
        self.decode_backgroundcolor = (20, 20, 20)
        self.decode_hover_backgroundcolor = (30, 30, 30)
        self.decode_pressed_backgroundcolor = (15, 15, 15)

        self.footer_color = (170, 170, 170)

        self.theme_icon = "img/sun.png"

        self.main_backgroundcolor = (16, 16, 16)

    def updateTheme(self, MainWindow):
        MainWindow.setStyleSheet(f"background-color: rgb{self.main_backgroundcolor};\n"
                                 "font-size: 14px;\n"
                                 "font-family: Arial, sans-serif;\n"
                                 "\n"
                                 "QWidget {\n"
                                 "    position: absolute;\n"
                                 "    align-items: center;\n"
                                 "}")
        self.light.setStyleSheet("QPushButton {\n"
                                 "    background-color: rgba(250, 250, 250, 0);\n"
                                 "    border: solid rgb(220, 220, 220);\n"
                                 "    border-radius: 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgba(220, 220, 220, 0);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: rgba(200, 200, 200, 0);\n"
                                 "    color: rgba(0, 0, 0, .5);\n"
                                 "}")
        self.decode.setStyleSheet("#decode {\n"
                                  f"    color: rgb{self.decode_color};\n"
                                  f"    background-color: rgb{self.decode_backgroundcolor};\n"
                                  f"    border: 3px solid rgb{self.decode_border_color};\n"
                                  "     border-radius: 15px;\n"
                                  "    font-family: \"Arial Black\", sans-serif;\n"
                                  "}\n"
                                  "\n"
                                  "#decode:hover {\n"
                                  f"    background-color: rgb{self.decode_hover_backgroundcolor};\n"
                                  "}\n"
                                  "\n"
                                  "#decode:pressed {\n"
                                  f"    background-color: rgb{self.decode_pressed_backgroundcolor};\n"
                                  f"    color: rgba{self.decode_color + (.7,)};\n"
                                  "}")
        self.encode.setStyleSheet("#encode {\n"
                                  f"    color: rgb{self.decode_color};\n"
                                  f"    background-color: rgb{self.decode_backgroundcolor};\n"
                                  f"    border: 3px solid rgb{self.decode_border_color};\n"
                                  "     border-radius: 15px;\n"
                                  "    font-family: \"Arial Black\", sans-serif;\n"
                                  "}\n"
                                  "\n"
                                  "#encode:hover {\n"
                                  f"    background-color: rgb{self.decode_hover_backgroundcolor};\n"
                                  "}\n"
                                  "\n"
                                  "#encode:pressed {\n"
                                  f"    background-color: rgb{self.decode_pressed_backgroundcolor};\n"
                                  f"    color: rgba{self.decode_color + (.7,)};\n"
                                  "}")
        self.footer.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                  f"color: rgb{self.footer_color};\n"
                                  "font-weight: bold;\n"
                                  "border: none;\n"
                                  "padding: 0px;\n"
                                  "margin: 0px;")
        self.input.setStyleSheet("font-family: \"Lucida Console\", monospace;\n"
                                 "font-size: 14px;\n"
                                 f"background-color: rgba{self.io_backgroundcolor};\n"
                                 f"color: rgb{self.io_color};\n"
                                 "border: none;")
        self.output.setStyleSheet("font-family: \"Lucida Console\", monospace;\n"
                                  "font-size: 14px;\n"
                                  f"background-color: rgba{self.io_backgroundcolor};\n"
                                  f"color: rgb{self.io_color};\n"
                                  "border: none")
        self.code1.setStyleSheet("#code1 {\n"
                                 f"   color: rgb{self.codes_color};\n"
                                 "    font-weight: 500;\n"
                                 "    font-family: Arial, sans;\n"
                                 "}\n"
                                 "\n"
                                 "#code1:hover {\n"
                                 "    text-decoration: underline;    \n"
                                 "}")
        self.code2.setStyleSheet("#code2 {\n"
                                 f"   color: rgb{self.codes_color};\n"
                                 "    font-weight: 500;\n"
                                 "    font-family: Arial, sans;\n"
                                 "}\n"
                                 "\n"
                                 "#code2:hover {\n"
                                 "    text-decoration: underline;    \n"
                                 "}")
        self.code3.setStyleSheet("#code3 {\n"
                                 f"   color: rgb{self.codes_color};\n"
                                 "    font-weight: 500;\n"
                                 "    font-family: Arial, sans;\n"
                                 "}\n"
                                 "\n"
                                 "#code3:hover {\n"
                                 "    text-decoration: underline;    \n"
                                 "}")
        self.code4.setStyleSheet("#code4 {\n"
                                 f"   color: rgb{self.codes_color};\n"
                                 "    font-weight: 500;\n"
                                 "    font-family: Arial, sans;\n"
                                 "}\n"
                                 "\n"
                                 "#code4:hover {\n"
                                 "    text-decoration: underline;    \n"
                                 "}")
        self.key.setStyleSheet("font-family: \"Lucida Console\", monospace;\n"
                               "font-size: 14px;\n"
                               "padding-top: 4px;\n"
                               "border: none;\n"
                               f"background-color: rgba{self.io_backgroundcolor};\n"
                               f"color: rgb{self.io_color};")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.theme_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light.setIcon(icon)
        self.light.setIconSize(QtCore.QSize(32, 32))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(480, 640)
        MainWindow.setMinimumSize(QtCore.QSize(480, 640))
        MainWindow.setMaximumSize(QtCore.QSize(480, 640))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(1)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)

        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPlainTextEdit {\n"
                                         "    background-color: rgb(240, 240, 240);\n"
                                         "    \n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton {\n"
                                         "    background-color: rgba(0, 0, 0, 0);\n"
                                         "    color: rgb(240, 240, 240);\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar:vertical {\n"
                                         "    border: none;\n"
                                         "    background: #2d2d44;\n"
                                         "    width: 14px;\n"
                                         "    margin: 15px 0 15px 0;\n"
                                         "    border-radius: 0px;\n"
                                         " }\n"
                                         "\n"
                                         "QScrollBar::handle:vertical {   \n"
                                         "    background-color: #5e00cc;\n"
                                         "    min-height: 30px;\n"
                                         "    border-radius: 7px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover { \n"
                                         "    background-color: #9900ff;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:pressed {   \n"
                                         "    background-color: #5100a0;\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar::sub-line:vertical {\n"
                                         "    border: none;\n"
                                         "    background-color: #3b3b5a;\n"
                                         "    height: 15px;\n"
                                         "    border-top-left-radius: 7px;\n"
                                         "    border-top-right-radius: 7px;\n"
                                         "    subcontrol-position: top;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:hover {   \n"
                                         "    background-color: #9900ff;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:pressed { \n"
                                         "    background-color: #5100a0;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QScrollBar::add-line:vertical {\n"
                                         "    border: none;\n"
                                         "    background-color: #3b3b5a;\n"
                                         "    height: 15px;\n"
                                         "    border-bottom-left-radius: 7px;\n"
                                         "    border-bottom-right-radius: 7px;\n"
                                         "    subcontrol-position: bottom;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:hover {   \n"
                                         "    background-color: #ff9900;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:pressed { \n"
                                         "    background-color: #ba7000;\n"
                                         "}\n"
                                         "\n"
                                         "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                         "    background: none;\n"
                                         "    \n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                         "    background: none;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.light = QtWidgets.QPushButton(self.centralwidget)
        self.light.setGeometry(QtCore.QRect(430, 590, 32, 32))
        self.light.setText("")
        self.light.setObjectName("light")
        self.decode = QtWidgets.QPushButton(self.centralwidget)
        self.decode.setEnabled(True)
        self.decode.setGeometry(QtCore.QRect(270, 490, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.decode.setFont(font)

        self.decode.setCheckable(True)
        self.decode.setObjectName("decode")

        self.encode = QtWidgets.QPushButton(self.centralwidget)
        self.encode.setObjectName(u"encode")
        self.encode.setEnabled(True)
        self.encode.setGeometry(QtCore.QRect(50, 490, 161, 61))
        font1 = QtGui.QFont()
        font1.setFamily(u"Arial Black")
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.encode.setFont(font1)

        self.encode.setCheckable(True)

        self.footer = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(10, 590, 251, 41))
        self.footer.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        self.footer.setReadOnly(True)
        self.footer.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.footer.setObjectName("footer")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 441, 194))
        self.layoutWidget.setObjectName("layoutWidget")
        self.io = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.io.setContentsMargins(0, 0, 0, 0)
        self.io.setObjectName("io")
        self.input = QtWidgets.QPlainTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(1)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.input.setFont(font)

        self.input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhMultiLine)
        self.input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input.setPlainText("")
        self.input.setObjectName("input")
        self.io.addWidget(self.input)
        self.output = QtWidgets.QPlainTextEdit(self.layoutWidget)

        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.io.addWidget(self.output)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 260, 441, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.codes = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.codes.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.codes.setContentsMargins(0, 0, 0, 0)
        self.codes.setObjectName("codes")
        self.code1 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.code1.setTabletTracking(False)
        self.code1.setAcceptDrops(False)
        self.code1.setAutoFillBackground(False)

        self.code1.setObjectName("code1")
        self.codes.addWidget(self.code1)
        self.code2 = QtWidgets.QRadioButton(self.layoutWidget1)

        self.code2.setObjectName("code2")
        self.codes.addWidget(self.code2)
        self.code3 = QtWidgets.QRadioButton(self.layoutWidget1)

        self.code3.setObjectName("code3")
        self.codes.addWidget(self.code3)
        self.code4 = QtWidgets.QRadioButton(self.layoutWidget1)

        self.code4.setObjectName("code4")
        self.codes.addWidget(self.code4)
        self.key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(130, 420, 221, 32))

        self.updateTheme(self)

        self.key.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.key.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.key.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.key.setObjectName("key")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифрумбус"))
        self.decode.setText(_translate("MainWindow", "Расшифровать"))
        self.encode.setText(_translate("MainWindow", "Зашифровать"))
        self.footer.setPlaceholderText(_translate("MainWindow", "Автор: Лазарев Кирилл АБ-220 Почта: kirikillerlazarev@gmail.com"))
        self.input.setPlaceholderText(_translate("MainWindow", "Введите текст для шифровки/дешифровки"))
        self.code1.setText(_translate("MainWindow", "Шифр Цезаря"))
        self.code2.setText(_translate("MainWindow", "Шифр замены с умножением"))
        self.code3.setText(_translate("MainWindow", "Шифр Виженера"))
        self.code4.setText(_translate("MainWindow", "XOR шифрование"))
        self.key.setPlaceholderText(_translate("MainWindow", "Введите ключ"))
