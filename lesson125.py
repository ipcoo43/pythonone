print('''
[ if 조건문(condition) ]
- if : 만약 ~ 라면
- if <불 값>:
	<불 값이 참일 때 실행할 문장>
- 소프트탭 : 탭을 입력하면 띄어쓰기
''')

if True:
	print('True입니다.')

if False:
	print('Fasle입니다.')

print()
number = input('정수 입력> ')  # 정수 입력
number = int(number)
if number > 0:			# 양수 조건
	print('{} 은 양수 입니다.'.format(number))
if number < 0:			# 음수 조건
	print('{} 은 음수 입니다'.format(number))
if number == 0:			# 0 조건
	print('0 입니다.')