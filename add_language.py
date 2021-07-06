from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dbproject.dbdetails import dbdata as dbc

import sys 


class addlanguage(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("add_language.ui", self)
        self.con = dbc.createdata()
        self.mycursor = self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)

    def fetchdata(self):
        self.id = self.txtid.text().strip()
        self.name = self.txtname.text().strip()
        self.inventor = self.txtin.text().strip()
        self.year = self.txtyear.text().strip()
        self.feature = self.txtfea.text().strip()

        if len(self.id) == 0 or len(self.name) == 0 or len(self.inventor) == 0 or len(self.year) == 0 or len(self.feature) == 0:
            self.showMessage("errror", "data needed")
        else:
            strinsert = "insert into languagedetails(languageid, languagename, inventer, inventionyear, features)values(%s,%s,%s,%s,%s)"
            self.mycursor.execute(strinsert, (self.id, self.name, self.inventor, self.year, self.feature))
            self.con.commit()
            self.showMessage("inseration", "row added succesfully")

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()


def main():
    app = QApplication(sys.argv)
    frame = addlanguage()
    frame.show()
    app.exec_()


if __name__ == '__main__': main()
