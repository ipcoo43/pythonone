list_number = [52, 273, 32, 72, 100]
try:
	number_input_a = int(input('정수 입력> '))
	print('{}번째 요소: {}'.format(number_input_a, list_number[number_input_a]))
except IndexError as e:
	print('5미만의 값을 입력 해 주세요')
except ValueError as e:
	print('정수를 입력해 주세요')
except Exception as e:
	print(type(e),'=>',e)