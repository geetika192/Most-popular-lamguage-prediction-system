from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dbproject.dbdetails import dbdata as dbc
import sys


class add_language(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("surveyDeatils.ui", self)
        self.con=dbc.createdata()
        self.mycursor=self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)

    def fetchdata(self):
        self.id=self.txtid.text().strip()
        self.name=self.txtname.text().strip()
        self.rat=self.txtratings.text().strip()
        self.date=self.txtdate.text().strip()

        if len(self.id)==0 or len(self.name)==0 or len(self.rat)==0 or len(self.date)==0:
            self.showMessage("errror","data needed")
        else:
             strinsert="insert into  language_survey (languageId, companeyName, rating, date)values(%s,%s,%s,%s)"
             self.mycursor.execute(strinsert,(self.id, self.name, self.rat, self.date))
             self.con.commit()
             self.showMessage("inseration","row added succesfully")

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()


def main():
    app = QApplication(sys.argv)
    frame = add_language()
    frame.show()
    app.exec_()


if __name__ == '__main__': main()
