from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dbproject.dbdetails import dbdata as dbc
import sys

class Search(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("showAll.ui", self)
        self.con = dbc.createdata()
        self.mycursor = self.con.cursor()
        self.fillcombo()
        self.btnsubmit.clicked.connect(self.fillTable)

    def fillcombo(self):
        strselect="select * from  languagedetails"
        self.mycursor=self.con.cursor()
        self.mycursor.execute(strselect)
        dataset = self.mycursor.fetchall()
        for row in dataset:
             print(row[1])
             self.cmfill.addItem(row[1])

    def fillTable(self):
                print("in fill")
                strsql="select l.inventer,l.inventionyear,l.features from languagedetails l where languagename=%s "
                md=self.cmfill.currentText()
                data=(md,)
                self.cursor=self.con.cursor()
                self.cursor.execute(strsql, data)
                dataset= self.cursor.fetchall()
                rowcnt=len(dataset)
                print(rowcnt)
                self.tbl.setRowCount(rowcnt)
                rownum=0
                for row in dataset:
                    for column in range(len(row)):
                        print(row[column])
                        self.tbl.setItem(rownum,column,QTableWidgetItem(str(row[column])))
                    rownum=rownum+1
def main():
    app=QApplication(sys.argv)
    m=Search()
    m.show()
    app.exec_()

if __name__ == '__main__':
            main()