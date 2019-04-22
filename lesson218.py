# 객체를 생성하는 함수 선언
# 학생과 점수를 입력 할 함수
def create_student(name,korean,math,english,science):
	return {
		'name':name,
		'korean':korean,
		'math':math,
		'english':english,
		'science':science
	}

# 학생을 처리하는 함수 선언
# student 매개 변수로 넣어서 총점을 구하는 함수
def student_get_sum(student):
	return student['korean'] + student['math'] + student['english'] + student['science']

# student 매개 변수로 넣어서 평균을 구하는 함수
def student_get_vaerage(student):
	return student_get_sum(student) / 4

# student 매개 변수로 넣어서 하나의 문자열로 변환하는 함수
def student_to_string(student):
	return '{}\t{}\t{}'.format(student['name'],student_get_sum(student),student_get_vaerage(student))

students = [
	create_student('윤인성', 87, 98, 88, 95 ), 
	create_student('연하진', 92, 98, 96, 98 ),
	create_student('구진연', 76, 96, 94, 90 ),
	create_student('나선주', 98, 92, 96, 92 ),
	create_student('윤아린', 95, 98, 98, 98 ),
	create_student('윤명월', 64, 98, 92, 92 ),
	create_student('김미화', 82, 86, 98, 88 ),
	create_student('김연화', 88, 74, 78, 92 ),
	create_student('박아현', 97, 92, 88, 95 ),
	create_student('서준서', 45, 52, 72, 78 )
]

# student에서 총함을 구하겠다.
# print(student_get_sum(students[0]))

# 학생을 한 명씩 반복하기
print('이름','총점','평균', sep='\t')
for student in students:
	print(student_to_string(student))
