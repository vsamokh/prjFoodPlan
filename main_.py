from PyQt5 import uic, QtWidgets, QtCore, QtGui#,QButtonGroup
import os
import sys



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