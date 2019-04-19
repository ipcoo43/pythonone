print('''
[ False로 변환되는 값 ]
- if 조건문의 매개 변수에 불이 아닌 다른 값이 올 때는 자동으로 이를 불로 변환 처리 하게 된다.
- False : None, 0, 0.0, '', [], {}, (), 바이트열 
''')

if 0:
	print('0은 True로 변환됩니다.')
else:
	print('0은 False로 변환됩니다.')


if '':
	print('빈 문자열은 True로 변환됩니다.')
else:
	print('빈 문자열은 False로 변환됩니다.')

if []:
	print('빈 리스트는 True로 변환됩니다.')
else:
	print('빈 리스트는 False로 변환됩니다.')

if ():
	print('빈 튜플은 True로 변환됩니다.')
else:
	print('빈 튜플은 False로 변환됩니다.')

if {}:
	print('빈 딕셔너리는 True로 변환됩니다.')
else:
	print('빈 딕셔너리는 False로 변환됩니다.')