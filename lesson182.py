print('''
[ 텍스트 파일 다루기 ]
- 파일 열기 : open(file,mode='r,w,a',encoding)
- 파일 읽기 : file.read()
- 파일 쓰기 : file.write()
- 파일 닫기 : file.close()
''')

with open('test.txt',mode='a', encoding='UTF-8') as fp:
	fp.write('abcde\n')

with open('test.txt','r',encoding='utf-8') as fp:
	i = 0
	for line in fp:
		print(i, line, end="")
		i += 1
