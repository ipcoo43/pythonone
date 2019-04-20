print('''
map(<함수>,<리스트>) => 리스트의 각 요소에 함수를 적용해서 새로운 배열 생성
filter(<함수>,<리스트>)	=> 리스트의 각 요소 중에 함수에 맞는 아이들만 모아 추출
lambda <매개변수> : <리턴값> : 함수를 간단하게 선언하는 방법
''')

def call_10_times(func):
	for i in range(5):
		func()

def print_hello():
	print('안녕하세요')

call_10_times(print_hello)

list_a = [1,2,3,4,5,6,7,8,9]
def power(x):
	return x*x
list_b = map(power,list_a)
print(list(list_b))

def under_3(x):
	return x < 3
list_c = filter(under_3,list_a)
print(list(list_c))