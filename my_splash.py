from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import pyttsx3 as p
import sys
import time
from project.login import Mylogin
def main():
    app=QApplication(sys.argv)
    splash_pix=QPixmap("hd.jpg")


    splash=QSplashScreen(splash_pix)
    splash.showFullScreen()

    current_window_flags=splash.windowFlags()
    splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | current_window_flags)
    font=QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setPointSize(40)
    splash.setFont(font)
    message="LANGUAGE PREDICTOR WELCOMES YOU"


    splash.showMessage(message,QtCore.Qt.AlignCenter | QtCore.Qt.AlignBaseline,QtGui.QColor.fromRgb(250,250,150))

    splash.show()
    app.processEvents()
    import time
    time.sleep(0)

    engine = p.init()
    engine.setProperty("rate",100)

    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say("language predictor welcomes you")
    engine.runAndWait()
    engine.stop()


    login=Mylogin()
    login.show()
    splash.finish(login)
    app.exec_()
if __name__ == '__main__': main()