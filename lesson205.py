print('''
바이너리 : 숫자만 0과 1만 사용
텍스트 데이터 : 글자를 쳐서 만들자 - 프로그래밍 언어
큰 의미 : 컴퓨터 내부의 모든 데이터
작은 의미 : 텍스트 데이터가 아닌 데이터
''')

# 텍스트 데이터 다루는 방법 : 글자가 적혀있는 파일
file = open('test.txt', 'r')
textdata = file.read()
file.close()
print(type(textdata))

# 바이너리 데이터 : 큰의미 : 컴퓨터 내부에 있는 모든 파일
# b'': 바이트열
# 작은 의미는 텍스트 파일이 아닐 때 의미를 지님
file = open('test.txt', 'rb')
bdata = file.read()
file.close()
print(type(bdata))
print(bdata)