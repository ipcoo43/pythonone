class Student:
	def __init__(self, name, korean, math, english, science):
		self.name = name
		self.korean = korean
		self.math = math
		self.english = english
		self.science = science
	
	def get_sum(self):
		return self.korean + self.math + self.english + self.science
	
	def get_average(self):
		return self.get_sum() / 4
	
	def __str__(self):
		return '{}\t{}\t{}'.format(self.name, self.get_sum(), self.get_average())
	
	def __eq__(self,value):
		print('eq 함수 호출')
		return 0

a = Student('홍길동',87,98,99,95)
# print(isinstance(a,Student))
print(str(a))

a == a
print(a==a)