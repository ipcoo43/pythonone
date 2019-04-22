class Test:
	def __init__(self):
		print('생성되었습니다.')
	
	def __del__(self):
		print('소멸되었습니다')

test = Test()
test = Test()
test = Test()
test = Test()