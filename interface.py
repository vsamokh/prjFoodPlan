from PyQt5 import uic, QtWidgets, QtCore, QtGui
#,QButtonGroup
import os
import sys
import numpy as np
import algorithms as al
import glob_settings
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
    def __init__(self, dishlist, family, num):
        self.dishlist = dishlist
        self.family = family
        self.num = num
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
        print(num)
        self.name1.setText(self.family[0].name) #
        if self.num > 1:
            self.name2.setText(self.family[1].name) #
        else:
            self.name2.setText(" ")
        if self.num > 2:
            self.name3.setText(self.family[2].name) #
        else:
            self.name3.setText(" ")    
        if self.num > 3:
            self.name4.setText(self.family[3].name) #
        else:
            self.name4.setText(" ")
        if self.num > 4:
            self.name5.setText(self.family[4].name) #
        else:
            self.name5.setText(" ")
        if self.num > 5:
            self.name6.setText(self.family[5].name) #
        else:
            self.name6.setText(" ")
        self.show()



    def Out(self, day):

        breakfast = ""
        for i in range(len(self.dishlist[day][0])):
            breakfast += str(i+1) + ") " + self.dishlist[day][0][i].name+"\n"

        lunch = ""
        for i in range(len(self.dishlist[day][1])):
            lunch += str(i+1) + ") " + self.dishlist[day][1][i].name+"\n"

        dinner = ""
        for i in range(len(self.dishlist[day][2])):
            dinner += str(i+1) + ") " + self.dishlist[day][2][i].name+"\n"

        snack = ""
        for i in range(len(self.dishlist[day][3])):
            snack += str(i+1) + ") " + self.dishlist[day][3][i].name+"\n"

        self.breakfast.setText(breakfast) 
        self.lunch.setText(lunch) 
        self.dinner.setText(dinner)
        self.snacs.setText(snack)

        b = [""]*self.num
        l = [""]*self.num
        d = [""]*self.num
        s = [""]*self.num
        for j in range(self.num):
            b[j] = ""
            for i in range(len(self.dishlist[day][0])):
                b[j] += str(i+1) + ") " + str(self.family[j].WeekDishList[day][0][i].portion)+"\n"
            l[j] = ""
            if self.family[0].work[day][1] != True:
                for i in range(len(self.dishlist[day][1])):
                    l[j] += str(i+1) + ") " + str(self.family[j].WeekDishList[day][1][i].portion)+"\n"
            else:
                l[j] = "Рекомендуємо блюда з калорійністю від " + str(round(self.family[j].Qmin*0.35,3)) + " до " + str(round(self.family[j].Qmax*0.35,3))
            d[j] = ""
            for i in range(len(self.dishlist[day][2])):
                d[j] += str(i+1) + ") " + str(self.family[j].WeekDishList[day][2][i].portion)+"\n"

            s[j] = ""
            for i in range(len(self.dishlist[day][3])):
                s[j] += str(i+1) + ") " + str(self.family[j].WeekDishList[day][3][i].portion)+"\n"

        self.b1.setText(b[0])
        self.l1.setText(l[0])
        self.d1.setText(d[0])
        self.s1.setText(s[0])

        if self.num > 1:
            self.b2.setText(b[1])
            self.l2.setText(l[1])
            self.d2.setText(d[1])
            self.s2.setText(s[1])
        if self.num > 2:
            self.b3.setText(b[2])
            self.l3.setText(l[2])
            self.d3.setText(d[2])
            self.s3.setText(s[2])
        if self.num > 3:
            self.b4.setText(b[3])
            self.l4.setText(l[3])
            self.d4.setText(d[3])
            self.s4.setText(s[3])
        if self.num > 4:
            self.b5.setText(b[4])
            self.l5.setText(l[4])
            self.d5.setText(d[4])
            self.s5.setText(s[4])
        if self.num > 5:
            self.b6.setText(b[5])
            self.l6.setText(l[5])
            self.d6.setText(d[5])
            self.s6.setText(s[5])

    #def Show(self):
    #    self.test = Test()
    #    self.close()
    #   self.test.show()

    def Monday(self):
        self.Out(0)
    def Tuesday(self):
        self.Out(1)
    def Wednesday(self):
        self.Out(2)
    def Thursday(self):
        self.Out(3)
    def Friday(self):
        self.Out(4)
    def Saturday(self):
        self.Out(5)
    def Sunday(self):
        self.Out(6)


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
        self.dishlist = al.DishList()
        self.family = []
        self.num = 0
        self.view()
        """
        super(Ui3, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form3uk.ui", self)
        self.help.clicked.connect(self.Help)
        self.add.clicked.connect(self.Add)
        self.calculate.clicked.connect(self.Calculate)

        self.show()
        """

    def view(self):
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
        gender = self.comboBox_2.currentIndex()
        age = float(self.age.text())
        height = float(self.height.text())
        weight = float(self.weight.text())
        """
        print(name)
        print(gender)
        print(age)
        print(height)
        print(weight)
        """
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
        member = al.Person(name,gender,weight,height,age,koef)
        self.family.append(member)
        #print(koef)
        work = np.zeros((7,3))
        if self.monday.isChecked() == True:
            #print("Monday")
            work[0][1] = True
        if self.tuesday.isChecked() == True:
            #print("Tuesday")
            work[1][1] = True
        if self.wednesday.isChecked() == True:
            #print("Wednesday")
            work[2][1] = True
        if self.thursday.isChecked() == True:
            #print("Thursday")
            work[3][1] = True
        if self.friday.isChecked() == True:
            #print("Friday")
            work[4][1] = True
        if self.saturday.isChecked() == True:
            #print("Saturday")
            work[5][1] = True
        if self.sunday.isChecked() == True:
            #print("Sunday")
            work[6][1] = True
        #print(work)
        self.family[self.num].WeekPlan(work, self.dishlist)
        self.num += 1 

    def Add(self):
        self.data()
        if self.num == 6:
            self.w3 = Ui4(self.dishlist, self.family, self.num)
            self.close()
            self.w3.show()
        else:
            #self.a = Ui3()
            self.close()
            #self.a.show()
            self.view()

    def Calculate(self):
        self.data()
        self.w3 = Ui4(self.dishlist, self.family, self.num)
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
        glob_settings.allergyid_list.append(1)
        print("1-Gluten")

    def A2(self):
        glob_settings.allergyid_list.append(2)
        print("2-Lactoze")

    def A3(self):
        glob_settings.allergyid_list.append(3)
        print("3-Dairy")

    def A4(self):
        glob_settings.allergyid_list.append(4)
        print("4-Eggs")

    def A5(self):
        glob_settings.allergyid_list.append(5)
        print("5-Nuts")

    def A6(self):
        glob_settings.allergyid_list.append(6)
        print("6-Soy")

    def A7(self):
        glob_settings.allergyid_list.append(7)
        print("7-Seafoods")

    def A8(self):
        glob_settings.allergyid_list.append(8)
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
