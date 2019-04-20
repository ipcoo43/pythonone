print('''
[ 함수의 가장 기본적인 형태 ]	
def <함수>(<매개변수>):
	<변수>=<초기값>
	<여러 가지 처리>
	<여러 가지 처리>
	return <변수>
''')

# 함수 선언
def sum_all(start, end):
	# 변수 선언
	output = 0
	# 반복문 돌려 숫자 더하기
	for i in range(start, end+1):
		output += i
	# 리턴 한다
	return output
# 함수 호출
print('0 to 100 :', sum_all(0,100))
print('0 to 1000 :', sum_all(0,1000))
print('50 to 100 :', sum_all(50,100))
print('500 to 1000 :', sum_all(500,1000))