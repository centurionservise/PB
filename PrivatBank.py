import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import uic
from PyQt5 import QtWidgets
from Ui_pb_gui import Ui_Form

import requests
# from multiprocessing import Queue
# from idna import idnadata

import json
import datetime
import sqlite3
import os, sys
import msvcrt
# from PB_module import pb_func

# DB='privat_api.db'
# privat_txt='privat_api.txt'
# url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

# cursor=None
# connector=None

# import design  # Это наш конвертированный файл дизайна

class SergWindow(QtWidgets.QMainWindow, Ui_Form):
    cursor=None
    connector=None

    def __init__(self):
        self.DB='privat_api.db'
        self.privat_txt='privat_api.txt'
        self.url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        self.line_empty='----------------------------------------------'
        self.line_header='''----------------------------------------------
            Privat Bank - API
----------------------------------------------'''
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        # self.setWindowTitle("Hello world")
        self.connector, self.cursor=self.db_connect()
        self.lcdNumber.display(self.records_count())
        self.horizontalSlider_sel_record.valueChanged.connect(self.select_record)
        self.btn_request.clicked.connect(self.main_func)
        self.btn_exit.clicked.connect(self.close)
        self.btn_load.clicked.connect(self.get_record)
        self.btn_load_calendar.clicked.connect(self.get_record_calendar)
        self.btn_left.clicked.connect(self.move_left)
        self.btn_right.clicked.connect(self.move_right)
        self.btn_copy.clicked.connect(self.copy_text)
        self.btn_print.clicked.connect(self.print_result)

        self.first_init()
        

    def first_init(self):
        self.api_status()
        self.set_period()

        if self.records_count()==0:
            self.horizontalSlider_sel_record.setMinimum(0)
            self.horizontalSlider_sel_record.setMaximum(0)
            self.horizontalSlider_sel_record.setValue(0)
        else:
            self.horizontalSlider_sel_record.setMinimum(1)
            self.horizontalSlider_sel_record.setMaximum(self.records_count())
            self.horizontalSlider_sel_record.setValue(1)
            self.lcdNumber_sel_record.display(self.horizontalSlider_sel_record.value())



    def set_period(self):
        self.period=self.get_period()
        self.label_period_start.setText(self.period[0])
        self.label_period_end.setText(self.period[1])

    def print_text(self,temp_text):
        import tempfile
        import win32api
        import win32print
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(temp_text)
        win32api.ShellExecute(0,'printto',filename,'"%s"' % win32print.GetDefaultPrinter(),'.',0)

    def print_result(self):
        text_from_textEdit=self.textEdit.toPlainText()
        if text_from_textEdit:
            self.print_text(text_from_textEdit)

    def copy_text(self):
        self.textEdit.copy()
        
    def move_left(self):
        self.horizontalSlider_sel_record.setValue(self.horizontalSlider_sel_record.sliderPosition()-1)
    def move_right(self):
        self.horizontalSlider_sel_record.setValue(self.horizontalSlider_sel_record.sliderPosition()+1)
    def get_record_calendar(self):
        '''Function return exect records from DB'''
        date=self.get_date()
        try:
            self.cursor.execute("SELECT * FROM Exchange_Rates WHERE date='{}'".format(date))
            row=self.cursor.fetchall()

            if row:
                self.textEdit.clear()
                counter_small=1
                self.textEdit.append('Record '+str(row[0][0])+':')
                self.label_date.setText(date)

                for record in row:
                    if counter_small==5:
                        self.textEdit.append('')
                        self.textEdit.append('Record '+str(record[0])+':')
                        counter_small=1  
                    temp_str=str(record[1])+"   "+str(record[2])+"   "+str(record[3])+"   "+str(record[4])
                    self.textEdit.append(temp_str)
                    counter_small+=1

        except sqlite3.DatabaseError as DB_error:
            print("sqlite3.DatabaseError: ",DB_error)
            return 0


    def get_date(self):
        year=self.calendarWidget.selectedDate().year()
        month=self.calendarWidget.selectedDate().month()
        day=self.calendarWidget.selectedDate().day()
        date=str(day)+'-'+str(month)+'-'+str(year)
        self.label_calendar.setText(date)
        return date


    def select_record(self):
        self.lcdNumber_sel_record.display(self.horizontalSlider_sel_record.value())

    def records_count(self):
        '''Function return amount of records in DB'''
        try:
            self.cursor.execute("SELECT * FROM Exchange_Rates WHERE ccy='USD'")
            row=self.cursor.fetchall()
            return(len(row))
        except sqlite3.DatabaseError as DB_error:
            print("sqlite3.DatabaseError: ",DB_error)
            return 0


    def get_period (self):
        '''Function return period of records in DB'''
        try:
            self.cursor.execute("SELECT * FROM Exchange_Rates WHERE ccy='USD'")
            row=self.cursor.fetchall()
            
            if len(row)==0:
                return ("00-00-0000","00-00-0000")
            elif len(row)==1:
                return (row[0][5],row[0][5])
            elif len(row)>1:
                return (row[0][5],row[-1][5])

        except sqlite3.DatabaseError as DB_error:
            print("sqlite3.DatabaseError: ",DB_error)
            return 0
    
    def get_record (self):
        '''Function return exect records from DB'''
        try:
            record_number=self.horizontalSlider_sel_record.value()
            self.cursor.execute("SELECT * FROM Exchange_Rates WHERE id='{}'".format(record_number))
            row=self.cursor.fetchall()

            # self.textEdit.clear()
            # print(row)
            self.fill_table_BD(row)
            # for record in row:
            #     temp_str=str(record[1])+"   "+str(record[2])+"   "+str(record[3])+"   "+str(record[4])
                # self.textEdit.append(temp_str)
                # self.label_date.setText(str(record[5]))
            

        except sqlite3.DatabaseError as DB_error:
            print("sqlite3.DatabaseError: ",DB_error)
            return 0

    def db_connect(self):
        '''Function get DB name, connects and return DB Tuple - (connector, cursor)'''
        try:
            connector=sqlite3.connect(self.DB)
            cursor=connector.cursor()
            new_table="CREATE TABLE IF NOT EXISTS Exchange_Rates (id INTEGER,ccy STRING,base_ccy STRING,buy REAL,sale REAL,date TEXT,time TEXT)"
            cursor.execute(new_table)
            return (connector,cursor)
        except sqlite3.DatabaseError as DB_error:
            print("sqlite3.DatabaseError: ", DB_error)
            return (None, None)

    def get_request(self, temp_url):
        '''Function gets Data by Url and returns result of request''' 
        try:
            return (requests.get(temp_url)).json()
        except :
            print("There was an error with the request")
            print("Check Internet Connection or PrivatBank API url")
            return None

    def api_status(self):
        if self.get_request(self.url)!=None:
            self.label_PB_status.setText('GOOD')
            self.label_PB_status.setStyleSheet('color: green')
            return 1
        else:
            self.label_PB_status.setText('BAD')
            self.label_PB_status.setStyleSheet('color: red')
            return 0

    def main_func(self):
        self.api_status()
        from_PB=self.get_request(self.url)
        temp_id=self.records_count()+1
        temp_list=[]
        temp_time=None
        now = datetime.datetime.now()
        # self.textEdit.clear()

        if from_PB!=None:
            temp_time=now.strftime("%d-%m-%#Y %H:%M:%S")
            # self.label_date.setText(now.strftime("%d-%m-%#Y"))
            counter=1
            self.textEdit.clear()
            self.fill_table(from_PB,temp_id,now.strftime("%d-%m-%#Y"))

            for i in from_PB:
                line_main='{}. {}: buy - {:.2f} {} / sale - {:.2f} {}'.format(counter, i['ccy'], float(i['buy']), i['base_ccy'], float(i['sale']),i['base_ccy'])
                temp_list.append(line_main)
                # self.textEdit.append(line_main)
                counter+=1
                try:
                    self.cursor.execute("INSERT INTO Exchange_Rates (id,ccy,base_ccy,buy,sale,date,time) VALUES (?,?,?,?,?,?,?)",(temp_id,i['ccy'], i['base_ccy'],i['buy'],i['sale'],now.strftime("%d-%m-%#Y"),now.strftime("%H:%M:%S")))
                except sqlite3.DatabaseError as err:
                    print("Error SQLite3: ", err)
                else:
                    self.connector.commit()

            with open(self.privat_txt,'w') as file:
                file.write(temp_time)
                file.write('\n'+self.line_header)
                for elem in temp_list:
                    file.write('\n'+elem)
                file.write('\n'+self.line_empty)

            self.lcdNumber.display(self.records_count())
            self.horizontalSlider_sel_record.setMaximum(self.records_count())
            self.set_period()
        
        else:
            pass


    def fill_table(self,requests_result,rec_number,rec_date):
        for i in requests_result:
            if i['ccy']=='USD':
                self.label_usd_buy.setText('{:.2f}'.format(float(i['buy'])))
                self.label_usd_sale.setText('{:.2f}'.format(float(i['sale'])))
            elif i['ccy']=='EUR':
                self.label_eur_buy.setText('{:.2f}'.format(float(i['buy'])))
                self.label_eur_sale.setText('{:.2f}'.format(float(i['sale'])))
            elif i['ccy']=='RUR':
                self.label_rur_buy.setText('{:.2f}'.format(float(i['buy'])))
                self.label_rur_sale.setText('{:.2f}'.format(float(i['sale'])))
            elif i['ccy']=='BTC':
                self.label_btc_buy.setText('{:.2f}'.format(float(i['buy'])))
                self.label_btc_sale.setText('{:.2f}'.format(float(i['sale'])))
        self.label_rec_number.setText(str(rec_number))
        self.label_rec_date.setText(rec_date)

    def fill_table_BD(self,requests_BD):
        # for record in row:
                # temp_str=str(record[1])+"   "+str(record[2])+"   "+str(record[3])+"   "+str(record[4])
        for i in requests_BD:
            rec_number=i[0]
            rec_date=i[5]
            if i[1]=='USD':
                self.label_usd_buy.setText('{:.2f}'.format(float(i[2])))
                self.label_usd_sale.setText('{:.2f}'.format(float(i[3])))
            elif i[1]=='EUR':
                self.label_eur_buy.setText('{:.2f}'.format(float(i[2])))
                self.label_eur_sale.setText('{:.2f}'.format(float(i[3])))
            elif i[1]=='RUR':
                self.label_rur_buy.setText('{:.2f}'.format(float(i[2])))
                self.label_rur_sale.setText('{:.2f}'.format(float(i[3])))
            elif i[1]=='BTC':
                self.label_btc_buy.setText('{:.2f}'.format(float(i[2])))
                self.label_btc_sale.setText('{:.2f}'.format(float(i[3])))
        self.label_rec_number.setText(str(rec_number))
        self.label_rec_date.setText(rec_date)
    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SergWindow()  # Создаём объект класса SergWindow
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    # print("Buy-buy")

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()