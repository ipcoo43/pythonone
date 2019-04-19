print('''
[ else 구문 ]
 if <불 값>:
	 <참일 때 실행할 문장>
 else:
	 <거짓일 때 실행할 문장>
''')

number = int(input('정수 입력> '))

if number % 2 == 0:  # 참일 때 : 짝수
	print('{}는 짝수 입니다.'.format(number))
else:  # 거짓일 때 : 홀수
	print('{}는 홀수 입니다.'.format(number))