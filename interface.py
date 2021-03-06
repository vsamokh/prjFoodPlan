from PyQt5 import uic, QtWidgets, QtCore, QtGui
#,QButtonGroup
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

#class Test(QtWidgets.QMainWindow):
#    super(Test, self).__init__()
#    # self.setWindowTitle('Optimal food plan')
#    # self.setupUi(self)
#    uic.loadUi("form5uk.ui", self)


class Ui4(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui4, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form4uk.ui", self)
       # self.shown.clicked.connect(self.Show)
        self.monday.clicked.connect(self.Monday)
        self.tuesday.clicked.connect(self.Tuesday)
        self.wednesday.clicked.connect(self.Wednesday)
        self.thursday.clicked.connect(self.Thursday)
        self.friday.clicked.connect(self.Friday)
        self.saturday.clicked.connect(self.Saturday)
        self.sunday.clicked.connect(self.Sunday)
        #n=3 #количество членов семьи
        #self.hiden(n)
        self.name1.setText("1") #
        self.name2.setText("2") #
        self.name3.setText("3") #
        self.name4.setText("4") #
        self.name5.setText("5") #
        self.name6.setText("6") #
        self.show()



    def Out(self):
        self.breakfast.setText("brekfast") #
        self.lunch.setTexet("Lunch") #
        self.dinner.setText("Dinner")#
        self.snacs.setText("Snacs")
        self.b1.setText(" ")
        self.l1.setText(" ")
        self.d1.setText(" ")
        self.s1.setTwxt(" ")
        self.b2.setText(" ")
        self.l2.setText(" ")
        self.d2.setText(" ")
        self.s2.setTwxt(" ")
        self.b3.setText(" ")
        self.l3.setText(" ")
        self.d3.setText(" ")
        self.s3.setTwxt(" ")
        self.b4.setText(" ")
        self.l4.setText(" ")
        self.d4.setText(" ")
        self.s4.setTwxt(" ")
        self.b5.setText(" ")
        self.l5.setText(" ")
        self.d5.setText(" ")
        self.s5.setTwxt(" ")
        self.b6.setText(" ")
        self.l6.setText(" ")
        self.d6.setText(" ")
        self.s6.setTwxt(" ")

    #def Show(self):
    #    self.test = Test()
    #    self.close()
    #   self.test.show()

    def Monday(self):
        self.Out()
    def Tuesday(self):
        self.Out()
    def Wednesday(self):
        self.Out()
    def Thursday(self):
        self.Out()
    def Friday(self):
        self.Out()
    def Saturday(self):
        self.Out()
    def Sunday(self):
        self.Out()


class Helper(QtWidgets.QDialog):
    def __init__(self):
        super(Helper, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("helper.ui", self)
        self.closer.clicked.connect(self.Close)

    def Close(self):
        self.close()


class Ui3 (QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui3, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form3uk.ui", self)
        self.help.clicked.connect(self.Help)
        self.add.clicked.connect(self.Add)
        self.calculate.clicked.connect(self.Calculate)

        self.show()

    def Help(self):
        self.h=Helper()
        self.h.show()

    def data(self):
        name = self.name.text()
        age = self.age.text()
        height = self.height.text()
        weight = self.weight.text()
        print(name)
        print(age)
        print(height)
        print(weight)

        k = self.comboBox.currentIndex()
        if k == 0:
            koef = 1.2
        elif k == 1:
            koef = 1.375
        elif k == 2:
            koef = 1.55
        elif k == 3:
            koef = 1.7
        elif k == 4:
            koef = 1.9
        print(koef)
        if self.monday.isChecked() == True:
            print("Monday")
        if self.tuesday.isChecked() == True:
            print("Tuesday")
        if self.wednesday.isChecked() == True:
            print("Wednesday")
        if self.thursday.isChecked() == True:
            print("Thursday")
        if self.friday.isChecked() == True:
            print("Friday")
        if self.saturday.isChecked() == True:
            print("Saturday")
        if self.sunday.isChecked() == True:
            print("Sunday")

    def Add(self):
        self.data()
        self.a = Ui3()
        self.close()
        self.a.show()

    def Calculate(self):
        self.data()
        self.w3 = Ui4()
        self.close()
        self.w3.show()


class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form2uk.ui", self)
        self.next_button.clicked.connect(self.buttonnext)
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

    def buttonnext(self):
        self.w2 = Ui3()
        self.close()
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
