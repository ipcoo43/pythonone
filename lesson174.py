print('''
[ 재귀 함수의 문제 ]
- 피보나치 수열은 토끼는 어떠한 속도로 번식하는가
 > 처음에는 토끼가 한 쌍만 존재한다.
 > 두 달 이상 된 토기는 번식할 수 있다.
 > 번식한 토끼는 매달 새끼를 한 쌍씩 낳는다.
 > 토끼는 죽지 않는다고 가정한다.
 > 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
- f(1) = 1
- f(2) = 1
- f(n) = f(n-1) + f(n-2)
- f(3) = f(2)+f(1) = 1+1 =2
''')

# 함수 선언
def fibonacci(n):
	if n == 1:
		return 1  # 탈출구
	if n == 2 :
		return 1  # 탈출구
	else:
		return fibonacci(n-1) + fibonacci(n-2)
# 함수 호출 한다
print('fibonacci(1): ', fibonacci(1))
print('fibonacci(2): ', fibonacci(2))
print('fibonacci(3): ', fibonacci(3))
print('fibonacci(4): ', fibonacci(4))

print('fibonacci(50)을 입력하면 한 시간을 계산하는 문제점을 발생하는 재귀함수의 문제점 노출 ')