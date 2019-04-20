print('구문이 사용되었을 때 여러 줄 문자열')

# 변수 선언
number = int(input('정수 입력> '))

# if 조건문으로 홀수, 짝수 구분
if number % 2 == 0:
	print((
		"입력한 문자열은 {}입니다.\n"
		"{}는 짝수입니다."
	).format(number, number))
else:
	print((
		"입력한 문자열은 {}입니다.\n"
		"{}는 홀수입니다."
	).format(number, number))
print('-'*20)

if number % 2 == 0:
	print('\n'.join([
		"입력한 문자열은 {}입니다.",
		"{}는 짝수입니다."
	]).format(number, number))
else:
	print('\n'.join([
		"입력한 문자열은 {}입니다.",
		"{}는 홀수입니다."
	]).format(number, number))