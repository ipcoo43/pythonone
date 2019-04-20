print('''
[ 매개 변수 ]
print(기본매개변수, 가변매개변수 )
[ 기본 매개 변수 }
def 함수_이름(a,b,c,d,e):
	<문장>
함수_이름(1,2,3,4,5)
- 매개 변수 오류 : 매개 변수를 입력한 것보다 적거나 많이 넣으면 오류 발생
[ 가변 매개 변수 ]
def 함수_이름(a,b,c,d,*e): * 기호 사용
	<문장>
함수_이름(1,2,3,4,5,6,7,8,9)
''')

# 기본 매개 변수
def print_n_times(value, n):
	# value = '안녕하세요'
	# n = 5
	for i in range(n):
		print(value)
print_n_times('안녕하세요',5)
print()

# 가변 매개 변수
def print_a_times(n, *values):
	# n번 반복 한다.
	for i in range(n):
		# values는 리스트처럼 활용한다.
		for value in values:
			print(value)
		# 단순한 줄바꿈
		print()
# 함수 호출
print_a_times(3,'안녕하세요','즐거운','파이썬 프로그래밍')