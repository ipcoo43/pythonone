# 변수 선언
counter = 0
# 함수 선언
def fibonacci(n):
	# 어떤 피보나치 수를 구하는지 출력한다.
	print('fibonacci({})를 구한다'.format(n))
	global counter
	counter += 1
	# 피보나치 수를 구한다.
	if n == 1:
		return 1
	if n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
# 함수 호출
fibonacci(10)
print('-'*40)
print('fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.'.format(counter))