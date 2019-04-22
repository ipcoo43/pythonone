class Student:
	count = 0
	def __init__(self, name, korean, math, english, science):
		Student.count += 1
		self.name = name
		self.korean = korean
		self.math = math
		self.english = english
		self.science = science
	
	@classmethod
	def count(cls):
		print(Student.count)

Student.count()


