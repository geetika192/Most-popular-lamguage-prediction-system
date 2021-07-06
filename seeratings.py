from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dbproject.dbdetails import dbdata as dbc
from PyQt5 import QtGui
import sys
class Show(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("see_ratings.ui",self)
        self.con=dbc.createdata()
        self.mycursor=self.con.cursor()
        self.populatetable()
    def  populatetable(self):
        strsql="select l.languagename , s.rating from languagedetails l,language_survey s where l.languageId=s.languageId "
        self.mycursor.execute(strsql)
        dataset=self.mycursor.fetchall()
        rownum=0
        for row in dataset:
           for column in range(len(row)):
                print(row[column])
                self.tbl.setItem(rownum,column,QTableWidgetItem(str(row[column])))
           rownum=rownum+1

def main():
    app = QApplication([])
    frame=Show()
    frame.show()
    app.exec_()
if __name__ == '__main__':
    main()