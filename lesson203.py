print('조건문 반복문 함수 : 재귀함수')
print('모듈 : os')

import os
for path in os.listdir('.'):
	if os.path.isdir(path):
		print(path, '은 디렉토리입니다.')
	else:
		print(path, '은 파일입니다.')