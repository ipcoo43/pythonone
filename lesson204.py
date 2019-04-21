print('조건문 반복문 함수 : 재귀함수')
print('모듈 : os')

import os

def read_folder(original_path):
	for path in os.listdir(original_path):
		if os.path.isdir(path):
			read_folder(original_path+'/'+path)
		else:
			print(path)

read_folder('.')