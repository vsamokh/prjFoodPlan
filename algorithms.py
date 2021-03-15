import numpy as np
import scipy
import math
import db_interface as db
import glob_settings as gb
import random
from scipy.optimize import linprog

gb.glob_init()
gb.lang = "uk"
conn = db.connect_db("databaseV2.7.db")


class Person:
	"""
	Класс в котором хранятся основные характеристики человека 
	"""
	def __init__(self, name, gender, weight, height, age, activity):
		"""
		Инициализация основных характеристик человека 
		"""
		self.name = name
		self.gender = gender
		self.weight = weight
		self.height = height
		self.age = age
		self.activity = activity
		self.sugar = 50
		self.cholesterol = 300
		self.caffeine = 400
		self.sodium = 2000
		self.cellulose = 50
		self.A = 900
		self.B12 = 2.4
		self.D = 800
		self.E = 10
		self.K = 120
		self.calcium = 1000
		self.magnesium = 600
		if gender == 0 :
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
		self.fat_min = weight * 0.8
		self.proteins_min = weight * 1.5
		self.carbohydrates_min = weight * 2 - 10
		self.fat_max = weight
		self.proteins_max = weight * 2
		self.carbohydrates_max = weight * 2 + 10

	def WeekPlan(self, work, List):
		"""
		Инициализация графика работы, коректировка плана питания на неделю и расчет порций
		"""
		self.work = work
		self.WeekDishList = List 
		#проходим по графику работы, если человек не дома, меняем блюда на эту часть дня
		for day in range(7):
			for i in range(3):
				if work[day][i]:
					if i == 0 :
						self.WeekDishList[day][0] = db.Breakfast(conn)
					elif i == 1:
						#self.WeekDishList[day][1] = db.Lunch(conn)
						dish = Pseudo_Dish(self)
						lunch = [dish]
						self.WeekDishList[day][1] = lunch
					elif i == 2:
						self.WeekDishList[day][2] = db.Dinner(conn)
		#количество порций соответствующее личному списку блюд
		x = Portions(self)
		#print(x)
		self.portion = [[[] for _ in range(4)] for _ in range(7)]
		#print(self.portion)
		for day in range(7):
			for i in range(len(self.WeekDishList[day][0])):
				self.portion[day][0].append(x[day][i])
				#print(self.portion,"\n")
			for i in range(len(self.WeekDishList[day][1])):
				self.portion[day][1].append(x[day][i + len(self.WeekDishList[day][0])])
				#print(self.portion,"\n")
			for i in range(len(self.WeekDishList[day][2])):
				self.portion[day][2].append(x[day][i + len(self.WeekDishList[day][1]) + len(self.WeekDishList[day][0])])
				#print(self.portion,"\n")
			for i in range(len(self.WeekDishList[day][3])):
				self.portion[day][3].append(x[day][i + len(self.WeekDishList[day][2])+ len(self.WeekDishList[day][1]) + len(self.WeekDishList[day][0])])
				#print(self.portion,"\n")
		#print(self.portion)
			
class Pseudo_Dish:
	def __init__(self, person):
		self.name = "-"
		self.calories = random.uniform(person.Qmin*0.35,person.Qmax*0.35)
		self.fat = random.uniform(person.fat_min*0.25,person.fat_max*0.35)
		self.proteins = random.uniform(person.proteins_min*0.25,person.proteins_max*0.35)
		self.carbohydrates = random.uniform(person.carbohydrates_min*0.25,person.carbohydrates_max*0.35)
		self.cholesterol = 0
		self.sodium = 0
		self.cellulose = 0

def Portions(person):
	"""
	Функция просчета кол-ва порций для человека

	"""
	res = [[]]*7
	for day in range(7):
		size = len(person.WeekDishList[day][0]) + len(person.WeekDishList[day][1]) + len(person.WeekDishList[day][2]) + len(person.WeekDishList[day][3])
		#масив параметров блюд
		a = np.zeros((17, size))
		#минимизируемая функция
		c = np.ones(size)
		#масив ограничений
		#b = np.array([person.Qmax*0.3, person.Qmin*0.3*(-1),person.Qmax*0.35, person.Qmin*0.35*(-1),person.Qmax*0.20, person.Qmin*0.20*(-1),person.Qmax*0.15, person.Qmin*0.15*(-1), person.fat*(-1) , person.proteins*(-1) ,  person.carbohydrates*(-1) ,  person.sugar*(-1) , person.cholesterol *(-1),  person.alcohol ,  person.caffeine ,  person.sodium *(-1),  person.cellulose *(-1),  person.A *(-1),  person.B1*(-1) ,  person.B6 *(-1),  person.B12 *(-1),  person.C *(-1),  person.D *(-1),  person.E *(-1),  person.K *(-1),  person.calcium *(-1),  person.iron *(-1),  person.magnesium*(-1),  person.zinc *(-1)])
		b = np.array([person.Qmax*0.3,person.Qmin*0.3*(-1),person.Qmax*0.35, person.Qmin*0.35*(-1),person.Qmax*0.20, person.Qmin*0.20*(-1),person.Qmax*0.15, person.Qmin*0.15*(-1), person.fat_min * (-1)*0.8, person.fat_max*1.2, person.proteins_min * (-1)*0.8, person.proteins_max*1.2, person.carbohydrates_min * (-1)*0.8, person.carbohydrates_max*1.2, person.cholesterol, person.sodium,  person.cellulose])
		#заполнение масива параметров блюд
		for i in range(len(person.WeekDishList[day][0])):
			a[0][i] = person.WeekDishList[day][0][i].calories
			a[1][i] = person.WeekDishList[day][0][i].calories * (-1)
		for i in range(len(person.WeekDishList[day][1])):
			a[2][i + len(person.WeekDishList[day][0])] = person.WeekDishList[day][1][i].calories
			a[3][i + len(person.WeekDishList[day][0])] = person.WeekDishList[day][1][i].calories * (-1)
		for i in range(len(person.WeekDishList[day][2])):
			a[4][i + len(person.WeekDishList[day][1]) + len(person.WeekDishList[day][0])] = person.WeekDishList[day][2][i].calories
			a[5][i + len(person.WeekDishList[day][1]) + len(person.WeekDishList[day][0])] = person.WeekDishList[day][2][i].calories * (-1)
		for i in range(len(person.WeekDishList[day][3])):
			a[6][i + len(person.WeekDishList[day][2])+ len(person.WeekDishList[day][1]) + len(person.WeekDishList[day][0])] = person.WeekDishList[day][3][i].calories
			a[7][i + len(person.WeekDishList[day][2])+len(person.WeekDishList[day][1]) + len(person.WeekDishList[day][0])] = person.WeekDishList[day][3][i].calories * (-1)
		dishes = sum(person.WeekDishList[day], [])
		for i in range(len(dishes)):
			a[8][i] = dishes[i].fat*(-1)
			a[9][i] = dishes[i].fat
			a[10][i] = dishes[i].proteins*(-1)
			a[11][i] = dishes[i].proteins
			a[12][i] = dishes[i].carbohydrates *(-1)
			a[13][i] = dishes[i].carbohydrates
			a[14][i] = dishes[i].cholesterol
			a[15][i] = dishes[i].sodium 
			a[16][i] = dishes[i].cellulose 
		cal = 0
		for i in range(len(dishes)):
			if i < len(dishes) - len(person.WeekDishList[day][3]):
				a1 = np.zeros((a.shape[1]))
				a1[i] = -1
				a = np.insert(a, 0, a1, axis = 0)
				b = np.insert(b, 0, -10)
				a1[i] = 1
				a = np.insert(a, 0, a1, axis = 0)
				b = np.insert(b, 0, 100)
			else:
				a1 = np.zeros((a.shape[1]))
				a1[i] = -1
				a = np.insert(a, 0, a1, axis = 0)
				b = np.insert(b, 0, -1)
				a1[i] = 1
				a = np.insert(a, 0, a1, axis = 0)
				b = np.insert(b, 0, 10)
			#print(dishes[i].name)
			"""
			a[11][i] = dishes[i].sugar * (-1)
			a[13][i] = dishes[i].alcohol  
			a[14][i] = dishes[i].caffeine  
			a[17][i] = dishes[i].A * (-1)
			a[18][i] = dishes[i].B1 * (-1)
			a[19][i] = dishes[i].B6 * (-1)
			a[20][i] = dishes[i].B12 * (-1)
			a[21][i] = dishes[i].C * (-1)
			a[22][i] = dishes[i].D * (-1)
			a[23][i] = dishes[i].E * (-1)
			a[24][i] = dishes[i].K * (-1)
			a[25][i] = dishes[i].calcium * (-1) 
			a[26][i] = dishes[i].iron * (-1)
			a[27][i] = dishes[i].magnesium * (-1)
			a[28][i] = dishes[i].zinc * (-1)
		print(a,b)
			"""
		#вычисление дробного кол-ва блюд, через библеотеку scipy
		simplex = linprog(c, a, b, method='simplex')
		print(a,b)
		#print("day ", day+1, ":", simplex.success)
		#получение целочисленного решения
		res[day] = BnB(a, b, c, simplex.x, simplex.fun, simplex.x)
		if res[day][0] == 0 :
			while cal < person.Qmin:
				for i in range(size):
					res[day][i] += 1	
					cal += dishes[i].calories
					if cal >= person.Qmin:
						break
		cal = 0
		for i in range(size):
			res[day][i] = round(res[day][i])
			cal += dishes[i].calories * res[day][i]

		#print(cal)
		#print(res[day])
	return res

def BnB (a, b, c, x, mnres, mnx):
	"""
	Метод ветвей границ, для нахождения целого решения сипмлекс метода
	"""
	#проходим по масиву порций
	for i in range(len(x)):
			#если порция не целая, делаем округление вверх и вниз с записью в новые переменные
			if x[i] != math.floor(x[i]):
					x1 = math.floor(x[i])
					x2 = math.ceil(x[i])
					#создаем две новые таблицы параметров = а , добавляя в них строку из 0, с 1 на позиции х
					a1 = np.zeros((a.shape[1]))
					a1[i] = 1
					a1 = np.insert(a, 0, a1, axis = 0)
					a2 = np.zeros((a.shape[1]))
					a2[i] = -1
					a2 = np.insert(a, 0, a2, axis = 0)
					#для каждой матрицы добавляем добавляем масив ограничений, в котором новым строкам соответствуют округленные х
					b1 = np.insert(b, 0, x1)
					b2 = np.insert(b, 0, x2)
					#решаем задачу с новыми ограничениями 
					res1 = linprog(c, a1, b1, method='simplex')
					#если получилось решить задачу, запоминаем минимальное знач. функции и х, после чего выволняем метод для полученого решения
					if res1.success and x[i] != res1.x[i] and x1 != 0:
							if res1.fun <= mnres or (res1.fun == math.floor(res1.fun) and mnres == math.floor(mnres)):
								mnres = res1.fun
								mnx = res1.x
							mnx = BnB(a1, b1, c, res1.x, mnres, mnx)
							mnres = 0
							for j in range(len(x)):
								mnres += mnx[j]

					res2 = linprog(c, a2, b2, method='simplex')
					if res2.success and x[i] != res2.x[i]:
							if res2.fun <= mnres or (res2.fun == math.floor(res2.fun) and mnres == math.floor(mnres)):
								mnres = res2.fun
								mnx = res2.x
							mnx = BnB(a2, b2, c, res2.x, mnres, mnx)
							mnres = 0
							for j in range(len(x)):
								mnres += mnx[j]
	#возвращаем минимальное целое решение
	
	return mnx

def DishList():
	"""
	Функция формирующая список блюд на неделю
	"""
	List = [[[]]]*7
	for day in range(7):
		List[day] = [db.Breakfast(conn), db.Lunch(conn), db.Dinner(conn), db.Snack(conn)]
	return List

"""
a = np.array([[1,2],[-3,-4],[-5,-6]])
b = np.array([7,-8,-9])
c = np.array([1,1])
res = linprog(c, a, b)
print(res)
X = BnB(a, b, c, res.x, res.fun, res.x)
print(X)


List = [[[]]]*7
for day in range(7):
		List[day] = [db.Breakfast(conn), db.Lunch(conn), db.Dinner(conn), db.Snack(conn)]

days = np.zeros((7,3))
days[0][1] = 1
test = Person("Testovenko Test Testovich", "Male", 66, 166, 66, 1.6)
#print(test.Qmin, test.Qmax)
test.WeekPlan(days, List)
print(test.portion[1][1][1])


for day in range(7):
	print("\nDay", day+1, ":\n")
	for i in range(4):
		print("Part", i+1, ":\n")
		for j in range(len(test.WeekDishList[day][i])):
			print(test.WeekDishList[day][i][j].name, test.WeekDishList[day][i][j].portion)
"""
