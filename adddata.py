from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from dbproject.dbdetails import dbdata as dbc
import sys
class add(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("adddata1.ui", self)
        self.con=dbc.createdata()
        self.mycursor=self.con.cursor()
        self.btnsubmit.clicked.connect(self.fetchdata)
    def fetchdata(self):
        self.ui=self.txtid.text().strip()
        self.up = self.txtpw.text().strip()
        self.un=self.txtname.text().strip()
        self.uph = self.txtno.text().strip()
        self.ue=self.txtemail.text().strip()

        
        if len(self.ui)==0 or len(self.up)==0 or len(self.un)==0 or len(self.uph)==0 or len(self.ue)==0:
            self.showMessage("errror","data needed")
        else:
            strinsert ="insert into admindetails(Adminid, Password, Name, Phone, Email)values(%s,%s,%s,%s,%s)"
            self.mycursor.execute(strinsert,(self.ui,self.up,self.un,self.uph ,self.ue))
            self.con.commit()
            self.showMessage("inseration","row added succesfully")

    def showMessage(self,title,message):
         msg=QMessageBox()
         msg.setWindowTitle(title)
         msg.setText(message)
         msg.setStandardButtons(QMessageBox.Ok)
         msg.show()
         msg.exec_()
def main():
    app=QApplication(sys.argv)
    frame=add()
    frame.show()
    app.exec_()
if __name__ == '__main__':main()
