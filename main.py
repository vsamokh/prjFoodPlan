import numpy as np
import scipy
import math
from scipy.optimize import linprog

class Person:
	def __init__(self, name, gender, weight, height, age, activity):
		self.name = name
		self.weight = weight
		self.height = height
		self.age = age
		self.activity = activity
		self.sugar = 50
		self.cholesterol = 300
		self.caffeine = 400
		self.sodium = 2
		self.cellulose = 50
		self.A = 900
		self.B12 = 2.4
		self.D = 800
		self.E = 10
		self.K = 120
		self.calcium = 1000
		self.magnesium = 600
		if gender == 'Male' :
			self.Qmin = (10 * weight + 6.25 * height -  5 * age + 5) * activity
			self.Qmax = (13.397 * weight + 4.799 * height - 5.677 * age + 88.362) * activity
			self.alcohol = 40
			self.B1 = 2.1
			self.B6 = 2
			self.C = 90
			self.iron = 12
			self.zinc = 15
		else :
			self.Qmin = (10 * weight + 6.25 * height -  5 * age - 161) * activity
			self.Qmax = (9.247 * weight + 3.098 * height - 4.330 * age + 447.593) * activity
			self.alcohol = 30
			self.B1 = 1.5
			self.B6 = 1.8
			self.C = 75
			self.iron = 30
			self.zinc = 12
		self.fat = Qmin / 24
		self.proteins = Qmin / 54
		self.carbohydrates = Qmin / 6

	def WeekPlan(self, home, List):

		self.WeekDishList = List 
		
		for day in range(7):
			for i in range(3):
				if home[day][i] == False :
					if i == 0 :
						self.WeekDishList[day].Breakfast()
					elif i == 1:
						self.WeekDishList[day].Lunch()
					elif i == 2:
						self.WeekDishList[day].Dinner()

		self.portions = Portions(self)


class Dish:
	def __init__(self, name, calories, fat, proteins, carbohydrates, sugar, cholesterol, alcohol, caffeine, sodium, cellulose, A, B1, B6, B12, C, D, E, K, calcium, iron, magnesium, zinc):
		self.name = name
		self.calories = calories
		self.fat = fat
		self.proteins = proteins
		self.carbohydrates = carbohydrates
		self.sugar = sugar
		self.cholesterol = cholesterol
		self.alcohol = alcohol
		self.caffeine = caffeine
		self.sodium = sodium
		self.cellulose = cellulose
		self.A = A
		self.B1 = B1
		self.B6 = B6
		self.B12 = B12
		self.C = C
		self.D = D
		self.E = E
		self.K = K
		self.calcium = calcium
		self.iron = iron
		self.magnesium = magnesium
		self.zinc = zinc

class DishList:
	def __init__(self):
			... #рандомная генерация списков блюд на завтрак обед ужин и перекусы 

	def Breakfast(self):
			... #рандомная генерация завтрака

	def Lunch(self):
			... #рандомная генерация обеда

	def Dinner(self):
			... #рандомная генерация ужина

def Portions(person):
	res = [[]]*7
	for day in range(7):
		a = np.zeros((person.WeekDishList[day].size, 29))
		c = np.ones(person.WeekDishList[day].size)
		b = np.array([person.Qmax*0.3, person.Qmin*0.3*(-1),person.Qmax*0.35, person.Qmin*0.35*(-1),person.Qmax*0.20, person.Qmin*0.20*(-1),person.Qmax*0.15, person.Qmin*0.15*(-1), person.fat*(-1) , person.proteins*(-1) ,  person.carbohydrates*(-1) ,  person.sugar*(-1) , person.cholesterol *(-1),  person.alcohol ,  person.caffeine ,  person.sodium *(-1),  person.cellulose *(-1),  person.A *(-1),  person.B1*(-1) ,  person.B6 *(-1),  person.B12 *(-1),  person.C *(-1),  person.D *(-1),  person.E *(-1),  person.K *(-1),  person.calcium *(-1),  person.iron *(-1),  person.magnesium*(-1),  person.zinc *(-1)])

		for i in range(len(person.WeekDishList[day].breakfast)):
			a[0][i] = person.WeekDishList[day].breakfast[i].calories
			a[1][i] = person.WeekDishList[day].breakfast[i].calories*(-1)
		for i in range(len(person.WeekDishList[day].lunch)):
			a[2][i + len(person.WeekDishList[day].breakfast)] = person.WeekDishList[day].dinner[i + len(person.WeekDishList[day].breakfast)].calories
			a[3][i + len(person.WeekDishList[day].breakfast)] = person.WeekDishList[day].dinner[i + len(person.WeekDishList[day].breakfast)].calories*(-1)
		for i in range(len(person.WeekDishList[day].dinner)):
			a[4][i + len(person.WeekDishList[day].lunch)] = person.WeekDishList[day].lunch[i + len(person.WeekDishList[day].lunch)].calories
			a[5][i + len(person.WeekDishList[day].lunch)] = person.WeekDishList[day].lunch[i + len(person.WeekDishList[day].lunch)].calories*(-1)
		for i in range(len(person.WeekDishList[day].snack)):
			a[6][i + len(person.WeekDishList[day].dinner)] = person.WeekDishList[day].snack[i + len(person.WeekDishList[day].dinner)].calories
			a[7][i + len(person.WeekDishList[day].dinner)] = person.WeekDishList[day].snack[i + len(person.WeekDishList[day].dinner)].calories*(-1)

		for i in range(person.WeekDishList[day].size):
			a[8][i] = person.WeekDishList[day].dish.fat  *(-1)
			a[9][i] = person.WeekDishList[day].dish.proteins  *(-1)
			a[10][i] = person.WeekDishList[day].dish.carbohydrates  *(-1)
			a[11][i] = person.WeekDishList[day].dish.sugar  *(-1)
			a[12][i] = person.WeekDishList[day].dish.cholesterol  *(-1)
			a[13][i] = person.WeekDishList[day].dish.alcohol  
			a[14][i] = person.WeekDishList[day].dish.caffeine  
			a[15][i] = person.WeekDishList[day].dish.sodium  *(-1)
			a[16][i] = person.WeekDishList[day].dish.cellulose  *(-1)
			a[17][i] = person.WeekDishList[day].dish.A  *(-1)
			a[18][i] = person.WeekDishList[day].dish.B1  *(-1)
			a[19][i] = person.WeekDishList[day].dish.B6  *(-1)
			a[20][i] = person.WeekDishList[day].dish.B12  *(-1)
			a[21][i] = person.WeekDishList[day].dish.C  *(-1)
			a[22][i] = person.WeekDishList[day].dish.D  *(-1)
			a[23][i] = person.WeekDishList[day].dish.E  *(-1)
			a[24][i] = person.WeekDishList[day].dish.K  *(-1)
			a[25][i] = person.WeekDishList[day].dish.calcium *(-1) 
			a[26][i] = person.WeekDishList[day].dish.iron  *(-1)
			a[27][i] = person.WeekDishList[day].dish.magnesium  *(-1)
			a[28][i] = person.WeekDishList[day].dish.zinc  *(-1)
		res[day] = linprog(c, a, b).X
	return res

def BnB (a, b, c, x, mnres, mnx):
        for i in range(len(x)):
                if x[i] != math.floor(x[i]):
                        x1 = math.floor(x[i])
                        x2 = math.ceil(x[i])
                        
                        a1 = np.zeros((a.shape[1]))
                        a1[i] = 1
                        #print(a)
                        #print(a1)
                        a1 = np.insert(a, 0, a1, axis = 0)
                        #print(a1)
                        a2 = np.zeros((a.shape[1]))
                        a2[i] = -1
                        a2 = np.insert(a, 0, a2, axis = 0)

                        b1 = np.insert(b, 0, x1)
                        #print(b)
                        #print(b1)
                        b2 = np.insert(b, 0, x2)

                        if x1 != 0 :
                                res1 = linprog(c, a1, b1)
                                if res1.success:
                                        if res1.fun <= mnres :
                                                mnres = res1.fun
                                                mnx = res1.x
                                        resx = BnB(a1, b1, c, res1.x, mnres, mnx)

                        res2 = linprog(c, a2, b2)
                        if res2.success:
                                if res2.fun <= mnres :
                                                mnres = res2.fun
                                                mnx = res2.x
                                resx = BnB(a2, b2, c, res2.x, mnres, mnx)

        return resx


a = np.array([[1,2],[-3,-4],[-5,-6]])
b = np.array([7,-8,-9])
c = np.array([1,1])
res = linprog(c, a, b)
print(res)
X = BnB(a, b, c, res.x, res.fun, res.x)
print(X)
