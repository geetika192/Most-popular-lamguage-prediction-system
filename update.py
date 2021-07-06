from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from dbproject.dbdetails import dbdata as dbc
import sys
class update(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("update.ui", self)
        self.con=dbc.createdata()
        self.mycursor=self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)
    def fetchdata(self):
        self.ui=self.txtid.text().strip()
        self.up=self.txtpw.text().strip()
        self.un=self.txtname.text().strip()
        self.uph=self.txtno.text().strip()
        self.ue=self.txtemail.text().strip()
        strupdate="update admindetails set  Password=%s, Name=%s, Phone=%s , Email=%s where Adminid=%s "
        self.mycursor.execute(strupdate,(self.up,self.un,self.uph,self.ue,self.ui))
        self.con.commit()

        if len(self.ui)==0 or len(self.up)==0 or len(self. un)==0 or len(self.uph)==0 or len(self.ue)==0:
            self.showMessage("errror","data needed")
        else:
           self.showMessage("successful","data updated")

    def showMessage(self,title,message):
         msg=QMessageBox()
         msg.setWindowTitle(title)
         msg.setText(message)
         msg.setStandardButtons(QMessageBox.Ok)
         msg.show()
         msg.exec_()



def main():
    app=QApplication([])
    frame=update()
    frame.show()
    app.exec_()
if __name__ == '__main__':main()