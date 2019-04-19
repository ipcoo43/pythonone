print('--- 문자열로 입력 받아 홀수 짝수 구분 ---')
number = input('정수 입력> ')
last_character = number[-1]

if last_character in '02468':
	print('{} 은 짝수 입니다.'.format(number))

if last_character in '13579':
	print('{} 은 홀수 입니다.'.format(number))
print()

print('--- 숫자로 입력 받아 홀수 짝수 구분 ---')
number = int(input('정수 입력> '))

if number % 2 == 0:
	print('{} 은 짝수 입니다.'.format(number))

if number % 2 == 1:
	print('{} 은 홀수 입니다.'.format(number))

print('''
- 사람은 끝자리가 2,4,6,8로 짝수 입니다. 
- 컴퓨터는 2로 나눈 나머지가 0이면 짝수
''')