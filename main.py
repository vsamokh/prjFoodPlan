class Person:
	def __init__(self, name, gender, weight, height, age, activity):
		self.name = name
		self.weight = weight
		self.height = height
		self.age = age
		self.activity = activity
		if gender == 'Male' :
			self.Qmin = (10 * weight + 6.25 * height -  5 * age + 5) * activity
			self.Qmax = (13.397 * weight + 4.799 * height - 5.677 * age + 88.362) * activity
		else :
			self.Qmin = (10 * weight + 6.25 * height -  5 * age - 161) * activity
			self.Qmax = (9.247 * weight + 3.098 * height - 4.330 * age + 447.593) * activity


test = Person("Test", "Male", 66.6, 166.6, 16, 1.9)

print(test.Qmin)
print(test.Qmax)
