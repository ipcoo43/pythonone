list_number = [52, 273, 32, 72, 100]
try:
	number_input_a = int(input('정수 입력> '))
	print('{}번째 요소: {}'.format(number_input_a, list_number[number_input_a]))
except Exception as e:
	print(type(e),'=>',e)
	if type(e) == IndexError:
		print('인덱스를 넘었습니다. 5 미만의 값을 입력 해 주세요')
	elif type(e) == ValueError:
		print('정수를 입력 해 주세요')
	else:
		print('알수 없는 에러가 발생 했습니다.')