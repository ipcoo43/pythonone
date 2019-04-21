import os
while True:
	input_a = input('입력 101~200> ')
	if input_a.isdigit():
		os.system('clear')
		unmber_input_a = int(input_a)
		with open('lesson'+input_a+'.py','r',encoding='utf-8') as fp:
			print(fp.read())
	else:
		break		

