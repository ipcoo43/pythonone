print('''
[ 범위 만들기 ]
range(<숫자1>) : 0부터 (<숫자1>-1)까지의 정수 범위
range(<숫자1>,<숫자2>) : <숫자1>부터 (<숫자2>-1)까지의 정수의 범위
ringe(<숫자1>,<숫자2>,<숫자3>) : <숫자1>부터 <숫자3> 만큼의 차이를 가진 (<숫자2>-1)까지 범위
[ 범위와 반복문 ]
for <범위 내부의 숫자를 담을 변수> in <범위>:
	<코드>
''')

print(range(5))
print(list(range(5)))
for i in range(5):
	print('{}번째 반복문입니다.'.format(i))
print()

print(range(5,10))
print(list(range(5,10)))
for i in range(5,10):
	print('{}번째 반복문입니다.'.format(i))
print()

print(range(0,10,2))
print(list(range(0,10,2)))
for i in range(0,10,2):
	print('{}번째 반복문입니다.'.format(i))