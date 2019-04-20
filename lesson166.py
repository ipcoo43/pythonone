print('''
[ 디폴트(아무것도 입력하지 않아도 들어가는 값) 매개 변수(= 기본 매기 변수)]
def 함수_이름(a=10, b=20):
	<문장>
함수_이름()
함수_이름(10)
함수_이름(10,20)
[ 키워드 매개 변수 ]
def 함수_이름(name=10):
	<문장>
함수_이름(10)
함수_이름(name=10)
''')

# 디폴트 매개 변수
def print_a_times(value, n=2):
	# n번 반복 한다
	for i in range(n):
		print(value)
# 함수 호출
print_a_times("안녕하세요")

# 키워드 매개 변수
def print_b_times(value, n=2):
	# n번 반복 한다
	for i in range(n):
		print(value)
# 함수 호출
print_b_times(value="안녕하세요", n=3)

print('1','2','3','4',sep='||',end='\n')