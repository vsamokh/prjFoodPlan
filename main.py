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

test = Person("Test", "Male", 66.6, 166.6, 16, 1.9)

print(test.Qmin)
print(test.Qmax)
