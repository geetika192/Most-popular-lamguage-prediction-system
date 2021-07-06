from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from project.admindash import Main
import sys
class Mylogin(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("login.ui",self)
        self.btnsubmit.clicked.connect(self.checkLogin)
    def checkLogin(self):
        userid=self.txtname.text()
        userpassword=self.txtpassword.text()


        if userid=="bbd"and userpassword=="bbdec":
           self.m=Main()
           self.m.show()
           self.close()
           print(userid+userpassword)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("error message")
            msg.setText("invalid/password")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.show()
            msg.exec_()


def main():
    app=QApplication(sys.argv)
    frame=Mylogin()
    frame.show()
    app.exec_()
if __name__ == '__main__':main()
