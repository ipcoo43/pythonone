# 클래스<이름 Camel Case> 선언
class Student:
	# 생성자 : 자기 자신을 생성하는 함수
	# self 객체 자신을 나타냄
	# 정보 입력 과정
	def __init__(self, name,korean,math,english,science): 
		self.name = name
		self.korean = korean
		self.math = math
		self.english = english
		self.science = science

	def get_sum(self):
		return self.korean + self.math + self.english + self.science

	def get_vaerage(self):
		return self.get_sum() / 4

	def to_string(self):
		return '{}\t{}\t{}'.format(self.name,self.get_sum(),self.get_vaerage())


# 학생의 리스트를 선언한다.
students = [
	Student('윤인성', 87, 98, 88, 95 ), 
	Student('연하진', 92, 98, 96, 98 ),
	Student('구진연', 76, 96, 94, 90 ),
	Student('나선주', 98, 92, 96, 92 ),
	Student('윤아린', 95, 98, 98, 98 ),
	Student('윤명월', 64, 98, 92, 92 ),
	Student('김미화', 82, 86, 98, 88 ),
	Student('김연화', 88, 74, 78, 92 ),
	Student('박아현', 97, 92, 88, 95 ),
	Student('서준서', 45, 52, 72, 78 )
]


# 학생을 한 명씩 반복하기
print('이름','총점','평균', sep='\t')
for student in students:
	print(student.to_string())