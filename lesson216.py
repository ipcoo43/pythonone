# 학생 리스트를 선언한다.
# 학생 하나, 하나를 객체라고 할 수 있다.
# 어떠한 속성을 가지고 있으면 객체
# 학생의 속성을 추가하다보면 사소한 실수를 발생하게되면서
# 학생의 실수를 줄이기위한 함수를 생성한다.
students = [
	{'name':'윤인성', 'korean':87, 'math':98 , 'english':88 , 'science':95 }, 
	{'name':'연하진', 'korean':92, 'math':98 , 'english':96 , 'science':98 },
	{'name':'구진연', 'korean':76, 'math':96 , 'english':94 , 'science':90 },
	{'name':'나선주', 'korean':98, 'math':92 , 'english':96 , 'science':92 },
	{'name':'윤아린', 'korean':95, 'math':98 , 'english':98 , 'science':98 },
	{'name':'윤명월', 'korean':64, 'math':98 , 'english':92 , 'science':92 },
	{'name':'김미화', 'korean':82, 'math':86 , 'english':98 , 'science':88 },
	{'name':'김연화', 'korean':88, 'math':74 , 'english':78 , 'science':92 },
	{'name':'박아현', 'korean':97, 'math':92 , 'english':88 , 'science':95 },
	{'name':'서준서', 'korean':45, 'math':52 , 'english':72 , 'science':78 }
]

# 학생을 한 명씩 반복하기
print('이름','총점','평균', sep='\t')
for student in students:
	# 점수의 총합과 평균을 구하기
	score_sum = student['korean'] + student['math'] + student['english'] + student['science']
	score_average = score_sum / 4
	# 출력하기
	print(student['name'], score_sum, score_average, sep='\t')
