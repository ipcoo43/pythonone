print('''
가비지 컬렉터 (Garbage Collector) : 쓰레기를 컬렉터 한다.
 - 더 이상 사용하지 않는 변수를 해제 시켜 주는 역할 
 - 컴퓨터에서 자동으로 메모리가 생성되는데, 사용 후 청소하는 역할
''')

class Test:
	def __init__(self,name):
		self.name = name
		print('{} - 생성되었습니다.'.format(self.name))
	
	def __del__(self):
		print('{} - 소멸되었습니다.'.format(self.name))

a=Test('A')
b=Test('B')
c=Test('C')

print('프로그램이 종료되는 시점')