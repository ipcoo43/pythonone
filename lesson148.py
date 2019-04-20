print('''
[ while 반복문 ]
- 조건을 기반으로 반복할 때 사용하는 반복문
while <조건>:
	<조건이 참일 때 반복할 코드>
[ for 반복문 ]
- 특정 횟구 또는 특정 요소에 대해 반복할 때 사용하는 반복문
for i in range(10):
''')

i = 0
while i < 10:
	print('{}번째 반복입니다'.format(i))
	i += 1