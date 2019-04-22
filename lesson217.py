# 객체를 생성하는 함수
def create_student(name,korean,math,english,science):
	return {
		'name':name,
		'korean':korean,
		'math':math,
		'english':english,
		'science':science
	}

# 함수가 생성되므로써 함수를 활용한 간단한 입력을 하게 된다.
# 객체를 생성하는 함수
# 이전 보다는 훨씬 코드가 줄어듬
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

# 이제 활용하는 부분도 함수를 만들었으면 
# 학생을 한 명씩 반복하기
print('이름','총점','평균', sep='\t')
for student in students:
	# 점수의 총합과 평균을 구하기
	score_sum = student['korean'] + student['math'] + student['english'] + student['science']
	score_average = score_sum / 4
	# 출력하기
	print(student['name'], score_sum, score_average, sep='\t')
