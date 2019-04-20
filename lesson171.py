print('''
[ 재귀(본디의 곳으로 다시 돌아감) 함수 ] 
- recursion(재귀)
- 자기 자신을 무한 반복으로 불러 오류 발생함
- 탈출 할 수 있는 구멍, 탈출구를 꼭 만들어 사용 해야함
''')

def recursion_function(i):
	print('안녕하세요')
	if i < 10:
		recursion_function(i+1)

recursion_function(2)