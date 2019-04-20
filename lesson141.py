print('''
[ for 반복문 ]
for <반복자> in <반복할 수 있는 것> :
	<코드>
[ 리스트와 for 반복문 ]
for <요소를 담을 변수> in <리스트>:
	<코드>
''')

# 리스트 선언
array=[273,32,103,57,52]

# 리스트 반복문 적용
for element in array:
	if element > 100:
		print(element, end=',')
print()