from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from project.adddata import add
from project.update import update
from project.add_language import addlanguage
from project.search import show
from project.showALL import Search
class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("projectadmin.ui",self)
        self.btnadd.clicked.connect(self.viewadd)
        self.btnupdate.clicked.connect(self.viewupdate)
        self.btnadd_language.clicked.connect(self.viewadd_language)
        self.btnsearch.clicked.connect(self.viewsearch)
        self.btnshow_all.clicked.connect(self.viewshow_all)
    def viewadd(self):
        self.a=add()
        self.a.show()
    def viewupdate(self):
        self.u= update()
        self.u.show()

    def viewadd_language(self):
        self.ad = addlanguage()
        self.ad.show()

    def viewsearch(self):
        self.s = show()
        self.s.show()

    def viewshow_all(self):
        self.sh =Search()
        self.sh.show()


def main():
    app=QApplication(sys.argv)
    admin=Admin()
    admin.show()
    app.exec_()
if __name__ == '__main__':main()
