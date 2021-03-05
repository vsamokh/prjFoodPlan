from PyQt5 import uic, QtWidgets, QtCore, QtGui#,QButtonGroup
import os
import sys

#from form import *


#import sys
 #app = QtWidgets.QApplication(sys.argv)
 #Optimalfoodplan = QtWidgets.QMainWindow()
 #ui = Ui_Optimalfoodplan()
 #ui.setupUi(Optimalfoodplan)
 #Optimalfoodplan.show()
 #ui.begin_button.clicked.connect(ui.Begin)
#sys.exit(app.exec_())

class Helper(QtWidgets.QDialog):
    def __init__(self):
        super(Helper, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("helper.ui", self)
        self.closer.clicked.connect(self.Close)
    def Close(self):
        self.close()

#class Ui3 (QtWidgets.QMainWindow):
 #   def __init__(self):
#        super(Ui3, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
#        uic.loadUi("form3uk.ui", self)
#        self.help.clicked.connect(self.Help)
        #self.add.clicked.connect(self.Add)
#        self.calculate.clicked.connect(self.Calculate)

        # self.show()

#    def Help(self):
#        self.h=Helper()
#        self.h.show()

    #def Add(self):
        #n=self.name.text()
        #print("0")



class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form2uk.ui", self)
        self.next_button.clicked.connect(self.ButtonNext)
        self.a1.clicked.connect(self.A1)
        self.a2.clicked.connect(self.A2)
        self.a3.clicked.connect(self.A3)
        self.a4.clicked.connect(self.A4)
        self.a5.clicked.connect(self.A5)
        self.a6.clicked.connect(self.A6)
        self.a7.clicked.connect(self.A7)
        self.a8.clicked.connect(self.A8)
        # self.show()
    def A1(self):
        print("1-Gluten")

    def A2(self):
        print("2-Lactoze")

    def A3(self):
        print("3-Dairy")

    def A4(self):
        print("4-Eggs")

    def A5(self):
        print("5-Nuts")

    def A6(self):
        print("6-Soy")

    def A7(self):
        print("7-Seafoods")

    def A8(self):
        print("8-No")
        #self.close()

    def ButtonNext(self):
        self.close()
        self.w2 = Ui3()
        self.w2.show()

class Ui1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui1, self).__init__()
        #self.title="Optimal food plan"
        #self.iconName="icon.png"
        uic.loadUi("form.ui", self)
        self.show()
        self.begin_button.clicked.connect(self.ButtonBegin)

    def ButtonBegin(self):
        self.w1 = Ui2()
        self.close()
        self.w1.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui1()
    # w.show()
    # sys.exit(app.exec_())
    app.exec_()