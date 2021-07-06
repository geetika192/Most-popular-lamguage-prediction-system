from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from project import admin
import sys
import pandas as pd
from project.adddata import add
from project.update import update
from project.add_language import addlanguage
from project.search import show
from project.seeratings import Show
from project.surveyDeatils import add_language
from project.showALL import Search
from project.language_rating import languageratings
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("adminDash.ui",self)
        self.add.triggered.connect(lambda:self.loadFrame(self.add))
        self.update.triggered.connect(lambda:self.loadFrame(self.update))
        self.add_language.triggered.connect(lambda: self.loadFrame(self.add_language))
        self.search.triggered.connect(lambda: self.loadFrame(self.search))
        self.rating.triggered.connect(lambda: self.loadFrame(self.rating))
        self.show_all.triggered.connect(lambda: self.loadFrame(self.show_all))
        self.highest.triggered.connect(lambda: self.loadFrame(self.highest))
        self.sm.triggered.connect(lambda: self.loadFrame(self.sm))

    def loadFrame(self,menuitem):
        caption=menuitem.text()
        print(caption)

        if caption=="language_details":
            self.m=addlanguage()
            self.m.show()
        if caption=="add_admin":
            self.u=add()
            self.u.show()
        if caption == "update_admin":
            self.i =update()
            self.i.show()
        if caption == "all_language":
            self.l =show()
            self.l.show()
        if caption=="language_rating":
            self.ur=Show()
            self.ur.show()
        if caption == "showall":
            self.u =Search()
            self.u.show()
        if caption=="highest":
            #languageratings = pd.read_excel("language_rating.xlsx", sheet_name="rating")
            self.p=languageratings()
            self.p.showchart()
        if caption == "survey_management":
            self.up=add_language()
            self.up.show()
def main():
        app=QApplication(sys.argv)
        m=Main()
        m.show()
        app.exec_()
if __name__ == '__main__':main()