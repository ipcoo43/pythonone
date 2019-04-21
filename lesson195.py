print('''finally 구문이 의미를 갖는 이유
- try/except 구문을 확 빠져 나갔을 때
 > return 키워드
 > break 키워드
''')

print('# try에서 return 할 경우')
def test():
	print('함수 시작 부분')
	try:
		print('try 구문의 1번 지점')
		return  # 함수를 벗어나라
		print('try 구문의 2번 지점')
	except:
		print('except 구문 지점')
	finally:
		print('finally 구문 지점')
	print('함수 끝 부분')

test()
print()

print('# except에서 return 할 경우')
def testB():
	print('함수 시작 부분')
	try:
		print('try 구문 지점')
		aaaa.bbbb.cccc   # 에러 발생
	except:
		print('except 구문 1번 지점')
		return  # 함수를 벗어나라
		print('except 구문 2번 지점')
	finally:
		print('finally 구문 지점')
	print('함수 끝 부분')

testB()