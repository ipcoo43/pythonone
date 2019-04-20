print('''
[ 재귀 함수로 팩터리얼 구하기 ]
factorial(n) = n * factorial(n-1) ( n >= 2 일 때)
factorial(1) = 1
factorial(4) = 4 * factorial(4-1) = 24
factorial(3) = 3 * factorial(3-1) = 6
factorial(2) = 2 * factorial(2-1) = 2
factorial(1) = 1 # 탈출구가 된다.
- 함수가 위에서 아래로 내려오다가 탈출구를 맞나면 위로 다시 올라 가면서 최종 값을 리턴한다.
''')

# 함수 선언
def factorial(n):
	# n이 1이라면 1을 리턴
	if n == 1: # 탈출구
		return 1
	# n이 1이 아니라면 n*(n-1)!을 리턴
	elif n >1:
		return n * factorial(n-1)
# 함수 호출
print('1! =',factorial(1))
print('2! =',factorial(2))
print('3! =',factorial(3))
print('4! =',factorial(4))
print('5! =',factorial(5))

