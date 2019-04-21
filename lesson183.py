print('''
[ 예외처리 ]
- 구문 오류 : 실행 전 - syntax error (프로그램 전체 실행 되지 않음)
- 예외 :실행 중에 발생하는 오류: exception/ runtime error (코드 읽다가 발생 함)
- 에외 처리 : 실행 중에 발생하는 오류를 미리 처리하는 것
- 기본 예외 처리 : if 기본적인 방법 
- 고급 예외 처리 : try except 사용
''')

print('기본 예외 처리')
while True:
	input_a = input('정수 입력> ')
	if input_a.isdigit():
		import os
		os.system('clear')
		number_input_a = int(input_a)
		print('원의 반지름 =', number_input_a)
		print('원의 둘레 =',2*3.14*number_input_a)
		print('원의 넓이 =',3.14*number_input_a*number_input_a)
		break
	else:
		print('정수를 입력 해주세요')