from PyQt5 import uic, QtWidgets, QtCore, QtGui
#,QButtonGroup
import os
import sys
import numpy as np
import algorithms as al
import glob_settings
import random
#from form import *


#import sys
 #app = QtWidgets.QApplication(sys.argv)
 #Optimalfoodplan = QtWidgets.QMainWindow()
 #ui = Ui_Optimalfoodplan()
 #ui.setupUi(Optimalfoodplan)
 #Optimalfoodplan.show()
 #ui.begin_button.clicked.connect(ui.Begin)
#sys.exit(app.exec_())

class Data(QtWidgets.QMainWindow):
    def __init__(self, family, num):
        super(Data, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form5.ui", self)
        names = ""
        ages = ""
        genders = ""
        weights = ""
        heights = ""
        activitys = ""
        alergens = ""
        for i in range(num):
            names += str(i+1) + ") " + family[i].name + "\n"
            ages += str(i+1) + ") " + str(family[i].age) + "\n"
        
            genders += str(i+1) + ") "
            if family[i].gender == 0:
                genders += "Чоловіча\n"
            else:
                genders += "Жіноча\n"
            weights += str(i+1) + ") " + str(family[i].weight) + "кг.\n"
            heights += str(i+1) + ") " + str(family[i].height) + "см.\n"
            activitys += str(i+1) + ") "
            if family[i].activity == 1.2:
                activitys += "Дуже слабка\n"
            elif family[i].activity == 1.375:
                activitys += "Cлабка\n"
            elif family[i].activity == 1.55:
                activitys += "Середня\n"
            elif family[i].activity == 1.7:
                activitys += "Висока\n"
            elif family[i].activity == 1.9:
                activitys += "Екстримальна\n"
        for i in range(len(glob_settings.allergyid_list)):
            if glob_settings.allergyid_list[i] == 1:
                alergens += "Глютен\n"
            if glob_settings.allergyid_list[i] == 2:
                alergens += "Лактоза\n"
            if glob_settings.allergyid_list[i] == 3:
                alergens += "Молочні продукти\n"
            if glob_settings.allergyid_list[i] == 4:
                alergens += "Яйця\n"
            if glob_settings.allergyid_list[i] == 5:
                alergens += "Горіхи\n"
            if glob_settings.allergyid_list[i] == 6:
                alergens += "Соя\n"
            if glob_settings.allergyid_list[i] == 7:
                alergens += "Морепродукти\n"
        if alergens == "":
            alergens = "Нема"
        self.name.setText(names)
        self.gender.setText(genders)
        self.age.setText(ages)
        self.weight.setText(weights)
        self.height.setText(heights)
        self.activity.setText(activitys)
        self.alergens.setText(alergens)
        self.pushButton.clicked.connect(self.Return)
        self.show()

    def Return(self):
        self.close()


class Test(QtWidgets.QMainWindow):
    def __init__(self, dishlist, family, num, day):
        super(Test, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form6.ui", self)
        calories = np.zeros(num)
        proteins = np.zeros(num)
        fat = np.zeros(num)
        carbohydrates = np.zeros(num)
        cholesterol = np.zeros(num)
        cellulose = np.zeros(num)
        sodium = np.zeros(num)
        
        for i in range(num):
            for j in range(4):
                for k in range(len(family[i].WeekDishList[day][j])):
                    calories[i] += family[i].WeekDishList[day][j][k].calories * family[i].portion[day][j][k]
                    fat[i] += family[i].WeekDishList[day][j][k].fat * family[i].portion[day][j][k]
                    proteins[i] += family[i].WeekDishList[day][j][k].proteins * family[i].portion[day][j][k]
                    carbohydrates[i] += family[i].WeekDishList[day][j][k].carbohydrates * family[i].portion[day][j][k]
                    cholesterol[i] += family[i].WeekDishList[day][j][k].cholesterol * family[i].portion[day][j][k]
                    cellulose[i] += family[i].WeekDishList[day][j][k].cellulose * family[i].portion[day][j][k]
                    sodium[i] += family[i].WeekDishList[day][j][k].sodium * family[i].portion[day][j][k]

        self.name1_3.setText(family[0].name)
        print(calories[0])
        self.k1.setText(str(calories[0])) # количество калорий в рационе
        print(proteins[0])
        self.b1_3.setText(str(proteins[0])) # количество белка в рационе
        print(fat[0])
        self.f1.setText(str(fat[0])) # количестважира в рационе
        print(carbohydrates[0])
        self.c1.setText(str(carbohydrates[0])) #количество углевода в рационе
        print(sodium[0])
        self.n1.setText(str(sodium[0]))#количество натрия в рационе
        print(cellulose[0])
        self.kl1.setText(str(cellulose[0])) #количество клетчатки в рационе
        print(cholesterol[0])
        self.h1.setText(str(cholesterol[0])) # количество холестерина в рационе
        self.nk1.setText(str(family[0].Qmin) + " - " + str(family[0].Qmax)) #  норма калорий
        self.nb1.setText(str(family[0].proteins_min) + " - " + str(family[0].proteins_max)) #норма белка
        self.nf1.setText(str(family[0].fat_min) + " - " + str(family[0].fat_max)) #норма жира
        self.nc1.setText(str(family[0].carbohydrates_min) + " - " + str(family[0].carbohydrates_max)) # норма углевов
        if num > 1:
            self.name2_3.setText(family[1].name)
            self.k2.setText(str(calories[1])) # количество калорий в рационе
            self.b2_3.setText(str(proteins[1])) # количество белка в рационе
            self.f2.setText(str(fat[1])) # количестважира в рационе
            self.c2.setText(str(carbohydrates[1])) #количество углевода в рационе
            self.n2.setText(str(sodium[1]))#количество натрия в рационе
            self.kl2.setText(str(cellulose[1])) #количество клетчатки в рационе
            self.h2.setText(str(cholesterol[1])) # количество холестерина в рационе
            self.nk2.setText(str(family[1].Qmin) + " - " + str(family[1].Qmax)) #  норма калорий
            self.nb2.setText(str(family[1].proteins_min) + " - " + str(family[1].proteins_max)) #норма белка
            self.nf2.setText(str(family[1].fat_min) + " - " + str(family[1].fat_max)) #норма жира
            self.nc2.setText(str(family[1].carbohydrates_min) + " - " + str(family[1].carbohydrates_max)) # норма углевов 
        if num > 2:
            self.name3_3.setText(family[2].name)
            self.k3.setText(str(calories[2])) # количество калорий в рационе
            self.b3_3.setText(str(proteins[2])) # количество белка в рационе
            self.f3.setText(str(fat[2])) # количестважира в рационе
            self.c3.setText(str(carbohydrates[2])) #количество углевода в рационе
            self.n3.setText(str(sodium[2]))#количество натрия в рационе
            self.kl3.setText(str(cellulose[2])) #количество клетчатки в рационе
            self.h3.setText(str(cholesterol[2])) # количество холестерина в рационе
            self.nk3.setText(str(family[2].Qmin) + " - " + str(family[2].Qmax)) #  норма калорий
            self.nb3.setText(str(family[2].proteins_min) + " - " + str(family[2].proteins_max)) #норма белка
            self.nf3.setText(str(family[2].fat_min) + " - " + str(family[2].fat_max)) #норма жира
            self.nc3.setText(str(family[2].carbohydrates_min) + " - " + str(family[2].carbohydrates_max)) # норма углевов

        if num > 3:
            self.name4_3.setText(family[3].name)
            self.k4.setText(str(calories[3])) # количество калорий в рационе
            self.b4_3.setText(str(proteins[3])) # количество белка в рационе
            self.f4.setText(str(fat[3])) # количестважира в рационе
            self.c4.setText(str(carbohydrates[3])) #количество углевода в рационе
            self.n4.setText(str(sodium[3]))#количество натрия в рационе
            self.kl4.setText(str(cellulose[3])) #количество клетчатки в рационе
            self.h4.setText(str(cholesterol[3])) # количество холестерина в рационе
            self.nk4.setText(str(family[3].Qmin) + " - " + str(family[3].Qmax)) #  норма калорий
            self.nb4.setText(str(family[3].proteins_min) + " - " + str(family[3].proteins_max)) #норма белка
            self.nf4.setText(str(family[3].fat_min) + " - " + str(family[3].fat_max)) #норма жира
            self.nc4.setText(str(family[3].carbohydrates_min) + " - " + str(family[3].carbohydrates_max)) # норма углевов

        if num > 4:
            self.name5_3.setText(family[4].name)
            self.k5.setText(str(calories[4])) # количество калорий в рационе
            self.b5_3.setText(str(proteins[4])) # количество белка в рационе
            self.f5.setText(str(fat[4])) # количестважира в рационе
            self.c5.setText(str(carbohydrates[4])) #количество углевода в рационе
            self.n5.setText(str(sodium[4]))#количество натрия в рационе
            self.kl5.setText(str(cellulose[4])) #количество клетчатки в рационе
            self.h5.setText(str(cholesterol[4])) # количество холестерина в рационе
            self.nk5.setText(str(family[4].Qmin) + " - " + str(family[4].Qmax)) #  норма калорий
            self.nb5.setText(str(family[4].proteins_min) + " - " + str(family[4].proteins_max)) #норма белка
            self.nf5.setText(str(family[4].fat_min) + " - " + str(family[4].fat_max)) #норма жира
            self.nc5.setText(str(family[4].carbohydrates_min) + " - " + str(family[4].carbohydrates_max)) # норма углевов

        if num > 5:
            self.name6_3.setText(family[5].name)
            self.k6.setText(str(calories[5])) # количество калорий в рационе
            self.b6_3.setText(str(proteins[5])) # количество белка в рационе
            self.f6.setText(str(fat[5])) # количестважира в рационе
            self.c6.setText(str(carbohydrates[5])) #количество углевода в рационе
            self.n6.setText(str(sodium[5]))#количество натрия в рационе
            self.kl6.setText(str(cellulose[5])) #количество клетчатки в рационе
            self.h6.setText(str(cholesterol[5])) # количество холестерина в рационе
            self.nk6.setText(str(family[5].Qmin) + " - " + str(family[5].Qmax)) #  норма калорий
            self.nb6.setText(str(family[5].proteins_min) + " - " + str(family[5].proteins_max)) #норма белка
            self.nf6.setText(str(family[5].fat_min) + " - " + str(family[5].fat_max)) #норма жира
            self.nc6.setText(str(family[5].carbohydrates_min) + " - " + str(family[5].carbohydrates_max)) # норма углевов
        
        self.pushButton.clicked.connect(self.Back)
        self.show()

    def Back(self):
        self.close()


class Helper2(QtWidgets.QDialog):
    def __init__(self):
        super(Helper2, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("helper2.ui", self)
        self.closer.clicked.connect(self.Close)

    def Close(self):
        self.close()


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
        self.shown.clicked.connect(self.Shown)
        self.shown1.clicked.connect(self.Shown1)
        self.pushButton.clicked.connect(self.Helper)
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

    def Helper(self):
        self.h=Helper2()
        self.h.show()

    def Out(self, day):
        self.day = day
        breakfast = ""
        for i in range(len(self.dishlist[day][0])):
            breakfast += str(i+1) + ") " + self.dishlist[day][0][i].name+"\n"

        lunch = ""
        home = False
        for i in range(self.num):
            if self.family[i].work[day][1] == False:
                home = True
                break
        if home:
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
                b[j] += str(i+1) + ") " + str(self.family[j].portion[day][0][i])+"\n"
            l[j] = ""
            if self.family[j].work[day][1] != True:
                for i in range(len(self.dishlist[day][1])):
                    l[j] += str(i+1) + ") " + str(self.family[j].portion[day][1][i])+"\n"
            else:
                l[j] = "Рекомендуємо блюда з калорійністю від " + str(round(self.family[j].Qmin*0.35,3)) + " до " + str(round(self.family[j].Qmax*0.35,3))
            d[j] = ""
            for i in range(len(self.dishlist[day][2])):
                d[j] += str(i+1) + ") " + str(self.family[j].portion[day][2][i])+"\n"

            s[j] = ""
            for i in range(len(self.dishlist[day][3])):
                s[j] += str(i+1) + ") " + str(self.family[j].portion[day][3][i])+"\n"

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

    def Shown(self):
        self.test = Test(self.dishlist, self.family, self.num, self.day)
        #self.close()
        self.test.show()
    def Shown1(self):
        self.data = Data(self.family,self.num)
        #self.close()
        self.data.show()

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
        # self.show()



    def buttonnext(self):
        if self.a1.isChecked()==True:
            glob_settings.allergyid_list.append(1)
            print("Gluten")
        if self.a2.isChecked()==True:
            glob_settings.allergyid_list.append(2)
            print("lactose")
        if self.a3.isChecked()==True:
            glob_settings.allergyid_list.append(3)
            print("Dairy")
        if self.a4.isChecked()==True:
            glob_settings.allergyid_list.append(4)
            print("Eggs")
        if self.a5.isChecked()==True:
            glob_settings.allergyid_list.append(5)
            print("Nuts")
        if self.a6.isChecked()==True:
            glob_settings.allergyid_list.append(6)
            print("Soy")
        if self.a7.isChecked()==True:
            glob_settings.allergyid_list.append(7)
            print("Seafoods")
        """
        if self.a8.isChecked()==True:
            glob_settings.allergyid_list.clear()
            print("No")
        """
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
    #w = Test()
    # w.show()
    # sys.exit(app.exec_())
    app.exec_()
