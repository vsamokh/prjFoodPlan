import numpy as np
import scipy
import math
import db_connect
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
						self.WeekDishList[day][0] = Breakfast()
					elif i == 1:
						self.WeekDishList[day][1] = Lunch()
					elif i == 2:
						self.WeekDishList[day][2] = Dinner()

		self.portions = Portions(self)
		print(self.portions)

"""
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
"""


def Portions(person):
	res = [[]]*7
	for day in range(7):
		a = np.zeros((person.WeekDishList[day].size, 29))
		c = np.ones(person.WeekDishList[day].size)
		b = np.array([person.Qmax*0.3, person.Qmin*0.3*(-1),person.Qmax*0.35, person.Qmin*0.35*(-1),person.Qmax*0.20, person.Qmin*0.20*(-1),person.Qmax*0.15, person.Qmin*0.15*(-1), person.fat*(-1) , person.proteins*(-1) ,  person.carbohydrates*(-1) ,  person.sugar*(-1) , person.cholesterol *(-1),  person.alcohol ,  person.caffeine ,  person.sodium *(-1),  person.cellulose *(-1),  person.A *(-1),  person.B1*(-1) ,  person.B6 *(-1),  person.B12 *(-1),  person.C *(-1),  person.D *(-1),  person.E *(-1),  person.K *(-1),  person.calcium *(-1),  person.iron *(-1),  person.magnesium*(-1),  person.zinc *(-1)])

		for i in range(len(person.WeekDishList[day][0])):
			a[0][i] = person.WeekDishList[day][0][i].calories
			a[1][i] = person.WeekDishList[day][0][i].calories*(-1)
		for i in range(len(person.WeekDishList[day][1])):
			a[2][i + len(person.WeekDishList[day][0])] = person.WeekDishList[day][1][i + len(person.WeekDishList[day][0])].calories
			a[3][i + len(person.WeekDishList[day][0])] = person.WeekDishList[day][1][i + len(person.WeekDishList[day][0])].calories*(-1)
		for i in range(len(person.WeekDishList[day][3])):
			a[4][i + len(person.WeekDishList[day].lunch)] = person.WeekDishList[day][2][i + len(person.WeekDishList[day].lunch)].calories
			a[5][i + len(person.WeekDishList[day].lunch)] = person.WeekDishList[day][2][i + len(person.WeekDishList[day].lunch)].calories*(-1)
		for i in range(len(person.WeekDishList[day][4])):
			a[6][i + len(person.WeekDishList[day][3])] = person.WeekDishList[day][4][i + len(person.WeekDishList[day][3])].calories
			a[7][i + len(person.WeekDishList[day][3])] = person.WeekDishList[day][4][i + len(person.WeekDishList[day][3])].calories*(-1)

		dishes = sum(person.WeekDishList[day], [])

		for i in range(len(dishes)):
			a[8][i] = dishes[i].fat  *(-1)
			a[9][i] = dishes[i].proteins  *(-1)
			a[10][i] = dishes[i].carbohydrates  *(-1)
			a[11][i] = dishes[i].sugar  *(-1)
			a[12][i] = dishes[i].cholesterol  *(-1)
			a[13][i] = dishes[i].alcohol  
			a[14][i] = dishes[i].caffeine  
			a[15][i] = dishes[i].sodium  *(-1)
			a[16][i] = dishes[i].cellulose  *(-1)
			a[17][i] = dishes[i].A  *(-1)
			a[18][i] = dishes[i].B1  *(-1)
			a[19][i] = dishes[i].B6  *(-1)
			a[20][i] = dishes[i].B12  *(-1)
			a[21][i] = dishes[i].C  *(-1)
			a[22][i] = dishes[i].D  *(-1)
			a[23][i] = dishes[i].E  *(-1)
			a[24][i] = dishes[i].K  *(-1)
			a[25][i] = dishes[i].calcium *(-1) 
			a[26][i] = dishes[i].iron  *(-1)
			a[27][i] = dishes[i].magnesium  *(-1)
			a[28][i] = dishes[i].zinc  *(-1)
		simplex = linprog(c, a, b)
		res[day] = BnB(a, b, c, simplex.x, simplex.fun, simplex.x)
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
                        #print(a2)
                        b1 = np.insert(b, 0, x1)
                        #print(b)
                        #print(b1)
                        b2 = np.insert(b, 0, x2)
                        #print(b2)
                        #break 
                        res1 = linprog(c, a1, b1)
                        #print(res1)
                        #break
                        #print(x)
                        #print(mnx)
                        if x[i] == res1.x[i]:
                                break
                        if res1.success:
                                if res1.fun <= mnres :
                                        mnres = res1.fun
                                        mnx = res1.x
                                mnx = BnB(a1, b1, c, res1.x, mnres, mnx)
                                mnres = 0;
                                for j in range(len(x)):
                                        mnres += mnx[j]

                        res2 = linprog(c, a2, b2)
                        #print(res2)
                        if x[i] == res2.x[i]:
                                break
                        if res2.success:
                                if res2.fun <= mnres :
                                                mnres = res2.fun
                                                mnx = res2.x
                                mnx = BnB(a2, b2, c, res2.x, mnres, mnx)
                                mnres = 0;
                                for j in range(len(x)):
                                        mnres += mnx[j]
        return mnx

"""
a = np.array([[1,2],[-3,-4],[-5,-6]])
b = np.array([7,-8,-9])
c = np.array([1,1])
res = linprog(c, a, b)
print(res)
X = BnB(a, b, c, res.x, res.fun, res.x)
print(X)
"""
