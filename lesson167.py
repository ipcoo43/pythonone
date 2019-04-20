print('''
[ 리턴값 ]
- 어떤 결과의 값을 저장하는 것, 반환 값
value = input('> ')
print(value)
''')
# 함수 정의
def return_test():
	print('A 위치입니다.')
	return # 리턴합니다. 함수를 여기서 끝내고 돌아가 주세요, 
	print('B 위치입니다.') # 출력이 안됨
# 함수 호출
return_test()

# 함수 정의
def return_testB():
	print('A 위치입니다.')
	return 100  # 지정한 값을 들고 돌아가 주세요
	print('B 위치입니다.') # 출력이 안됨
# 함수 호출
value = return_testB()
print(value)

	