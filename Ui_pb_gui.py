# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Администратор\Desktop\Python\CODE\PB\pb_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(754, 735)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Res/PrivatBank.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(10, 700, 118, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_exit.setObjectName("btn_exit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 10, 431, 56))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_period_start = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_period_start.setFont(font)
        self.label_period_start.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_period_start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_period_start.setObjectName("label_period_start")
        self.horizontalLayout.addWidget(self.label_period_start)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_period_end = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_period_end.setFont(font)
        self.label_period_end.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_period_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_period_end.setObjectName("label_period_end")
        self.horizontalLayout_2.addWidget(self.label_period_end)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(570, 390, 162, 241))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.lcdNumber_sel_record = QtWidgets.QLCDNumber(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumber_sel_record.setFont(font)
        self.lcdNumber_sel_record.setStyleSheet("color: rgb(0, 0, 255);\n"
"")
        self.lcdNumber_sel_record.setSmallDecimalPoint(False)
        self.lcdNumber_sel_record.setDigitCount(3)
        self.lcdNumber_sel_record.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_sel_record.setObjectName("lcdNumber_sel_record")
        self.verticalLayout_5.addWidget(self.lcdNumber_sel_record)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider_sel_record = QtWidgets.QSlider(self.layoutWidget1)
        self.horizontalSlider_sel_record.setAutoFillBackground(False)
        self.horizontalSlider_sel_record.setMinimum(1)
        self.horizontalSlider_sel_record.setMaximum(15)
        self.horizontalSlider_sel_record.setProperty("value", 1)
        self.horizontalSlider_sel_record.setSliderPosition(1)
        self.horizontalSlider_sel_record.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_sel_record.setInvertedAppearance(False)
        self.horizontalSlider_sel_record.setObjectName("horizontalSlider_sel_record")
        self.verticalLayout_2.addWidget(self.horizontalSlider_sel_record)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_left = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_left.setObjectName("btn_left")
        self.horizontalLayout_6.addWidget(self.btn_left)
        self.btn_right = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_right.setObjectName("btn_right")
        self.horizontalLayout_6.addWidget(self.btn_right)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.btn_load = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_load.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_load.setObjectName("btn_load")
        self.verticalLayout_5.addWidget(self.btn_load)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 80, 671, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 360, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 380, 521, 271))
        self.frame.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.btn_request = QtWidgets.QPushButton(self.frame)
        self.btn_request.setGeometry(QtCore.QRect(210, 230, 127, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_request.setFont(font)
        self.btn_request.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_request.setAutoDefault(False)
        self.btn_request.setDefault(False)
        self.btn_request.setObjectName("btn_request")
        self.splitter_4 = QtWidgets.QSplitter(self.frame)
        self.splitter_4.setGeometry(QtCore.QRect(30, 80, 461, 131))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_12 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_usd = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_usd.setFont(font)
        self.label_usd.setFrameShape(QtWidgets.QFrame.Box)
        self.label_usd.setTextFormat(QtCore.Qt.AutoText)
        self.label_usd.setScaledContents(False)
        self.label_usd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usd.setObjectName("label_usd")
        self.label_eur = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_eur.setFont(font)
        self.label_eur.setFrameShape(QtWidgets.QFrame.Box)
        self.label_eur.setTextFormat(QtCore.Qt.AutoText)
        self.label_eur.setScaledContents(False)
        self.label_eur.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eur.setObjectName("label_eur")
        self.label_rur = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_rur.setFont(font)
        self.label_rur.setFrameShape(QtWidgets.QFrame.Box)
        self.label_rur.setTextFormat(QtCore.Qt.AutoText)
        self.label_rur.setScaledContents(False)
        self.label_rur.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rur.setObjectName("label_rur")
        self.label_btc = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_btc.setFont(font)
        self.label_btc.setFrameShape(QtWidgets.QFrame.Box)
        self.label_btc.setTextFormat(QtCore.Qt.AutoText)
        self.label_btc.setScaledContents(False)
        self.label_btc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_btc.setObjectName("label_btc")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_13 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_usd_buy = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_usd_buy.setFont(font)
        self.label_usd_buy.setFrameShape(QtWidgets.QFrame.Box)
        self.label_usd_buy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usd_buy.setObjectName("label_usd_buy")
        self.label_eur_buy = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_eur_buy.setFont(font)
        self.label_eur_buy.setFrameShape(QtWidgets.QFrame.Box)
        self.label_eur_buy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eur_buy.setObjectName("label_eur_buy")
        self.label_rur_buy = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_rur_buy.setFont(font)
        self.label_rur_buy.setFrameShape(QtWidgets.QFrame.Box)
        self.label_rur_buy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rur_buy.setObjectName("label_rur_buy")
        self.label_btc_buy = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_btc_buy.setFont(font)
        self.label_btc_buy.setFrameShape(QtWidgets.QFrame.Box)
        self.label_btc_buy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_btc_buy.setObjectName("label_btc_buy")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_14 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_usd_sale = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_usd_sale.setFont(font)
        self.label_usd_sale.setFrameShape(QtWidgets.QFrame.Box)
        self.label_usd_sale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usd_sale.setObjectName("label_usd_sale")
        self.label_eur_sale = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_eur_sale.setFont(font)
        self.label_eur_sale.setFrameShape(QtWidgets.QFrame.Box)
        self.label_eur_sale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_eur_sale.setObjectName("label_eur_sale")
        self.label_rur_sale = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_rur_sale.setFont(font)
        self.label_rur_sale.setFrameShape(QtWidgets.QFrame.Box)
        self.label_rur_sale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rur_sale.setObjectName("label_rur_sale")
        self.label_btc_sale = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_btc_sale.setFont(font)
        self.label_btc_sale.setFrameShape(QtWidgets.QFrame.Box)
        self.label_btc_sale.setAlignment(QtCore.Qt.AlignCenter)
        self.label_btc_sale.setObjectName("label_btc_sale")
        self.splitter_6 = QtWidgets.QSplitter(self.frame)
        self.splitter_6.setGeometry(QtCore.QRect(400, 28, 84, 38))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_7 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_rec_number = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_rec_number.setFont(font)
        self.label_rec_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rec_number.setObjectName("label_rec_number")
        self.label_rec_date = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_rec_date.setFont(font)
        self.label_rec_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rec_date.setObjectName("label_rec_date")
        self.splitter_4.raise_()
        self.splitter_6.raise_()
        self.btn_request.raise_()
        self.label_PB_status_text = QtWidgets.QLabel(Form)
        self.label_PB_status_text.setGeometry(QtCore.QRect(8, 30, 174, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_PB_status_text.setFont(font)
        self.label_PB_status_text.setObjectName("label_PB_status_text")
        self.label_PB_status = QtWidgets.QLabel(Form)
        self.label_PB_status.setGeometry(QtCore.QRect(180, 30, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_PB_status.setFont(font)
        self.label_PB_status.setStyleSheet("")
        self.label_PB_status.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_PB_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PB_status.setObjectName("label_PB_status")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 656, 681, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.splitter_7 = QtWidgets.QSplitter(Form)
        self.splitter_7.setGeometry(QtCore.QRect(80, 100, 581, 257))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_calendar = QtWidgets.QLabel(self.layoutWidget2)
        self.label_calendar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_calendar.setObjectName("label_calendar")
        self.verticalLayout_4.addWidget(self.label_calendar)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget2)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.btn_load_calendar = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_load_calendar.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_load_calendar.setObjectName("btn_load_calendar")
        self.verticalLayout_3.addWidget(self.btn_load_calendar)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_result_box = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_result_box.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_result_box.setObjectName("verticalLayout_result_box")
        self.horizontalLayout_result_data = QtWidgets.QHBoxLayout()
        self.horizontalLayout_result_data.setObjectName("horizontalLayout_result_data")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(0, 170, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_result_data.addWidget(self.label)
        self.label_date = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_result_data.addWidget(self.label_date)
        self.verticalLayout_result_box.addLayout(self.horizontalLayout_result_data)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_result_box.addWidget(self.textEdit)
        self.horizontalLayout_btns = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btns.setObjectName("horizontalLayout_btns")
        self.btn_copy = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_copy.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_copy.setObjectName("btn_copy")
        self.horizontalLayout_btns.addWidget(self.btn_copy)
        self.btn_print = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_print.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_print.setObjectName("btn_print")
        self.horizontalLayout_btns.addWidget(self.btn_print)
        self.verticalLayout_result_box.addLayout(self.horizontalLayout_btns)
        self.splitter_7.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.btn_exit.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.frame.raise_()
        self.label_PB_status_text.raise_()
        self.label_PB_status.raise_()
        self.line_3.raise_()
        self.label_6.setBuddy(self.horizontalSlider_sel_record)
        self.label_calendar.setBuddy(self.calendarWidget)
        self.label.setBuddy(self.textEdit)
        self.label_date.setBuddy(self.textEdit)

        self.retranslateUi(Form)
        self.btn_copy.clicked.connect(self.textEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Курс валют Приват Банк"))
        self.btn_exit.setText(_translate("Form", "Выход"))
        self.label_2.setText(_translate("Form", "Записей в БД"))
        self.label_3.setText(_translate("Form", "Период"))
        self.label_period_start.setText(_translate("Form", "Начало"))
        self.label_period_end.setText(_translate("Form", "Конец"))
        self.label_6.setText(_translate("Form", "Выбор записи"))
        self.btn_left.setText(_translate("Form", "<--"))
        self.btn_right.setText(_translate("Form", "-->"))
        self.btn_load.setText(_translate("Form", "Загрузить"))
        self.btn_request.setText(_translate("Form", "Отправить запрос"))
        self.label_12.setText(_translate("Form", "Валюта"))
        self.label_usd.setText(_translate("Form", "USD"))
        self.label_eur.setText(_translate("Form", "EUR"))
        self.label_rur.setText(_translate("Form", "RUR"))
        self.label_btc.setText(_translate("Form", "BTC"))
        self.label_13.setText(_translate("Form", "Покупка, грн"))
        self.label_usd_buy.setText(_translate("Form", "--"))
        self.label_eur_buy.setText(_translate("Form", "--"))
        self.label_rur_buy.setText(_translate("Form", "--"))
        self.label_btc_buy.setText(_translate("Form", "--"))
        self.label_14.setText(_translate("Form", "Продажа, грн"))
        self.label_usd_sale.setText(_translate("Form", "--"))
        self.label_eur_sale.setText(_translate("Form", "--"))
        self.label_rur_sale.setText(_translate("Form", "--"))
        self.label_btc_sale.setText(_translate("Form", "--"))
        self.label_7.setText(_translate("Form", "Record: "))
        self.label_rec_number.setText(_translate("Form", "--"))
        self.label_rec_date.setText(_translate("Form", "--/--/----"))
        self.label_PB_status_text.setText(_translate("Form", "Privat Bank API Status - "))
        self.label_PB_status.setText(_translate("Form", "GOOD"))
        self.label_calendar.setText(_translate("Form", "Выбор записи"))
        self.btn_load_calendar.setText(_translate("Form", "Загрузить"))
        self.label.setText(_translate("Form", "Карта"))
        self.label_date.setText(_translate("Form", "Дата"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.btn_copy.setText(_translate("Form", "Copy"))
        self.btn_print.setToolTip(_translate("Form", "<html><head/><body><p>Print Tool Tip</p></body></html>"))
        self.btn_print.setWhatsThis(_translate("Form", "<html><head/><body><p>Print command What this</p></body></html>"))
        self.btn_print.setText(_translate("Form", "Печать"))

