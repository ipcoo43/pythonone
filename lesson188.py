print('''
- finally는 함수에서 사용된다.
- try + except 구문 조합 < 많이 사용>
- try + except + finally 구문 조합
- try + except + else + finally  구문 조합 < 많이 사용 >
- try + finally  구문 조합
''')
def test_function():
	try:
		input_a = input('숫자 입력> ')
		number_input_a = int(input_a)
		print(number_input_a*number_input_a)
	except:
		print('예외가 발생했습니다.')
	else:
		print('예외가 발생하지 않았습니다.')
	finally:
		print('반드시 실행되는 코드입니다.')

test_function()