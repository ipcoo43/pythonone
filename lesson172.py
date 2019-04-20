print('''
[ 팩터리얼 구하기 ]	
n! = n * (n-1) * (n-2) ... * 1
3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
''')
# 함수 선언
def factorial(n):
	# 변수 선언
	output = 1
	# 반복 돌려 숫자 더한다
	for i in range(1, n+1):  # 마지막 n+1은 n을 포함시키기 위함
		output *= i
	# 리턴 한다
	return output

# 함수 호출
print('2! =',factorial(2))
print('3! =',factorial(3))