from PyQt5 import uic, QtWidgets, QtCore, QtGui#,QButtonGroup
import os
import sys


class Ui2uk(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2uk, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form2(uk).ui", self)
        self.next_button.clicked.connect(self.ButtonNext)

        # self.show()

    def ButtonNext(self):
        self.close()
        self.w2 = Ui3uk()
        self.w2.show()


class Ui2ru(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2ru, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form2(ru).ui", self)
        self.next_button.clicked.connect(self.ButtonNext)

        # self.show()

    def ButtonNext(self):
        self.close()
        self.w2 = Ui3ru()
        self.w2.show()


class Ui2en(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2en, self).__init__()
        # self.setWindowTitle('Optimal food plan')
        # self.setupUi(self)
        uic.loadUi("form2(en).ui", self)
        self.no.clicked[bool].connect(self.Allergen)
        self.gluten.clicked[bool].connect(self.Allergen)
        self.lactose.clicked[bool].connect(self.Allergen)
        self.dairy.clicked[bool].connect(self.Allergen)
        self.eggs.clicked[bool].connect(self.Allergen)
        self.soy.clicked[bool].connect(self.Allergen)
        self.seafoods.clicked[bool].connect(self.Allergen)
        self.nuts.clicked[bool].connect(self.Allergen)
        #self.next_button.clicked.connect(self.ButtonNext)

        # self.show()
    def Allergen(self):
        if self.no.clicked()==True:
            allergenlist.append("No")
        else:
            if self.gluten.clicked()==True:
                allergenlist.append("Gluten")
            elif self.lactose.clicked()==True:
                allergenlist.append("Lactose")
            elif self.dairy.clicked()==True:
                allergenlist.append("Dairy")
            elif self.nuts.clicked()==True:
                allergenlist.append("Nuts")
            elif self.soy.clicked()==True:
                allergenlist.append("Soy")
            elif self.seafoods.clicked()==True:
                allergenlist.append("Seafoods")
            elif self.eggs.clicked()==True:
                allergenlist.append("Eggs")
        self.next_button.clicked.connect(self.ButtonNext)

    def ButtonNext(self):
        self.close()
        self.w2 = Ui3en()
        self.w2.show()

class Ui1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui1, self).__init__()
        #self.title="Optimal food plan"
        #self.iconName="icon.png"
        uic.loadUi("form.ui", self)
        #self.begin_button.clicked.connect(lambda: self.ButtonBegin(self.ru.isChecked(), self.uk.isChecked(),self.en.isChecked()))
        #self.ru.setChecked(True)
        #self.buttongroup = QButtonGroup()
        #self.buttongroup.buttonClicked[int].connect(self.On)
        #self.buttongroup.addButton(ru, 1)
        #self.buttongroup.addButton(en, 2)
        #self.buttongroup.addButton(uk, 3)
        self.ru.toggled.connect(self.On)
        self.uk.toggled.connect(self.On)
        self.en.toggled.connect(self.On)
        self.show()

   # def On(self, id):
    #    for button in self.buttongroup.buttons():
    #        if self.buttongroup.button(id):
    #            if button.text() =='Русский'):
    def On(self):

        if self.uk.isChecked()==True:
            self.w1 = Ui2uk()
        elif self.ru.isChecked() == True:
            self.w1 = Ui2ru()
        elif self.en.isChecked()==True:
            self.w1 = Ui2en()
        self.begin_button.clicked.connect(self.ButtonBegin)

    def ButtonBegin(self):
        #if self.ru.isChecked():
        #    self.w1 = Ui2ru()
        #elif self.uk.isChecked():
        #    self.w1 = Ui2uk()
        #else:
        #    self.w1 = Ui2en()
        self.close()
        self.w1.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui1()
    # w.show()
    # sys.exit(app.exec_())
    app.exec_()