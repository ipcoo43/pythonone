# 함수 선언
def sum_all(start=0, end=100, step=1):
	# 변수 선언
	output = 0
	# 반복문 돌려 숫자 더하기
	for i in range(start, end+1, step):
		output += i
	# 리턴 한다.
	return output

# 한수 호출
print('A.',sum_all(0,100,10))
print('B.',sum_all(end=100))
print('C.',sum_all(end=100, step=2))