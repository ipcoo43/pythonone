try:
	input_a = input('정수 입력> ')
	number_input_a = int(input_a)
	list_a = list(range(10))
	print(list_a[number_input_a])
except:
	print('예외 처리 구문')