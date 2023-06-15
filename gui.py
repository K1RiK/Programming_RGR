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

        self.footer_color = (220, 220, 220, .8)

        self.theme_icon = "img/sun.png"

        self.main_backgroundcolor = (16, 16, 16)

    def updateTheme(self, MainWindow):
        MainWindow.setStyleSheet("* {"
                                 "    font-size: 14px;"
                                 "}"
                                 "QMainWindow {"
                                 "    background-color: rgb(16, 16, 16);"
                                 "}"
                                 "QPlainTextEdit {"
                                 "    background-color: rgb(240, 240, 240);"
                                 "}"
                                 "QRadioButton {"
                                 "    background-color: rgba(0, 0, 0, 0);"
                                 "    color: rgb(240, 240, 240);"
                                 "}"
                                 "QPushButton {"
                                 "    font-family: Arial, sans-serif;"
                                 "}"
                                 "#centralwidget {"
                                 f"   background-color: rgb{self.main_backgroundcolor};"
                                 "    font-family: Arial, sans-serif;"
                                 "}"
                                 "#input, #output, #key {"
                                 "    font-family: \"Lucida Console\", monospace;"
                                 f"   background-color: rgba{self.io_backgroundcolor};"
                                 f"   color: rgb{self.io_color};"
                                 "    border: non"
                                 "}"
                                 "#code1, #code2, #code3, #code4 {"
                                 f"   color: rgb{self.codes_color};"
                                 "    font-weight: 500;"
                                 "    font-family: Arial, sans;"
                                 "}"
                                 "#decode, #encode {"
                                 f"   color: rgb{self.decode_color};"
                                 f"   background-color: rgb{self.decode_backgroundcolor};"
                                 f"   border: 3px solid rgb{self.decode_border_color};"
                                 "    border-radius: 16px;"
                                 "    font-family: \"Arial Black\", sans-serif;"
                                 "}"
                                 "#decode:hover, #encode:hover {"
                                 f"    background-color: rgb{self.decode_hover_backgroundcolor};"
                                 "}"
                                 "#decode:pressed, #encode:pressed{"
                                 f"    background-color: rgb{self.decode_pressed_backgroundcolor};"
                                 f"    color: rgba{self.decode_color + (.7,)};"
                                 "}"
                                 "#light {"
                                 "    background-color: rgba(0, 0, 0, 0);"
                                 "}")
        self.key.setStyleSheet("padding-top: 4px;")
        self.footer.setStyleSheet("background-color: rgba(0, 0, 0, 0);"
                                  f"color: rgba{self.footer_color};"
                                  "font-weight: bold;"
                                  "border: none;"
                                  "padding: 0px;"
                                  "margin: 0px;"
                                  "font-family: Arial, sans-serif;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.theme_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.light.setIcon(icon)
        self.light.setIconSize(QtCore.QSize(32, 32))

    def setupUi(self, MainWindow):
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
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
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QScrollBar:vertical {"
                                         "    border: none;"
                                         "    background: #2d2d44;"
                                         "    width: 8px;"
                                         "    margin: 15px 0 15px 0;"
                                         "    border-radius: 0px;"
                                         "}"
                                         "QScrollBar::handle:vertical {"
                                         "    background-color: #5e00cc;"
                                         "    min-height: 30px;"
                                         "    border-radius: 7px;"
                                         "}"
                                         "QScrollBar::handle:vertical:hover {"
                                         "    background-color: #9900ff;"
                                         "}"
                                         "QScrollBar::handle:vertical:pressed {"
                                         "    background-color: #5100a0;"
                                         "}"
                                         "QScrollBar::sub-line:vertical {"
                                         "    border: none;"
                                         "    background-color: #3b3b5a;"
                                         "    height: 15px;"
                                         "    border-top-left-radius: 7px;"
                                         "    border-top-right-radius: 7px;"
                                         "    subcontrol-position: top;"
                                         "    subcontrol-origin: margin;"
                                         "}"
                                         "QScrollBar::sub-line:vertical:hover {"
                                         "    background-color: #9900ff;"
                                         "}"
                                         "QScrollBar::sub-line:vertical:pressed {"
                                         "    background-color: #5100a0;"
                                         "}"
                                         "QScrollBar::add-line:vertical {"
                                         "    border: none;"
                                         "    background-color: #3b3b5a;"
                                         "    height: 15px;"
                                         "    border-bottom-left-radius: 7px;"
                                         "    border-bottom-right-radius: 7px;"
                                         "    subcontrol-position: bottom;"
                                         "    subcontrol-origin: margin;"
                                         "}"
                                         "QScrollBar::add-line:vertical:hover {"
                                         "    background-color: #ff9900;"
                                         "}"
                                         "QScrollBar::add-line:vertical:pressed {"
                                         "    background-color: #ba7000;"
                                         "}"
                                         "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {"
                                         "    background: none;"
                                         "}"
                                         "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
                                         "    background: none;"
                                         "}")

        self.light = QtWidgets.QPushButton(self.centralwidget)
        self.light.setGeometry(QtCore.QRect(430, 590, 32, 32))
        self.light.setObjectName("light")

        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(1)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.decode = QtWidgets.QPushButton(self.centralwidget)
        self.decode.setEnabled(True)
        self.decode.setGeometry(QtCore.QRect(270, 490, 161, 61))
        self.decode.setFont(font)
        self.decode.setCheckable(True)
        self.decode.setObjectName("decode")

        self.encode = QtWidgets.QPushButton(self.centralwidget)
        self.encode.setObjectName("encode")
        self.encode.setEnabled(True)
        self.encode.setGeometry(QtCore.QRect(50, 490, 161, 61))
        self.encode.setFont(font)
        self.encode.setCheckable(True)

        self.footer = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.footer.setGeometry(QtCore.QRect(10, 590, 275, 41))
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

        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(1)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.input = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.input.setFont(font)
        self.input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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
        self.key.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.key.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.key.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.key.setObjectName("key")

        self.updateTheme(self)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифрумбус"))
        self.key.setPlaceholderText(_translate("MainWindow", "Введите ключ"))
        self.input.setPlaceholderText(_translate("MainWindow", "Введите текст для шифровки/дешифровки"))
        self.footer.setPlainText(_translate("MainWindow", "Автор: Лазарев Кирилл АБ-220 Почта: kirikillerlazarev@gmail.com"))
        self.decode.setText(_translate("MainWindow", "Расшифровать"))
        self.encode.setText(_translate("MainWindow", "Зашифровать"))
        self.code1.setText(_translate("MainWindow", "Шифр Цезаря"))
        self.code2.setText(_translate("MainWindow", "Шифр замены с умножением"))
        self.code3.setText(_translate("MainWindow", "Шифр Виженера"))
        self.code4.setText(_translate("MainWindow", "XOR шифрование"))
