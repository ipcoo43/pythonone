print('''
[ 사용자에게 태어난 년도를 입력 받아 그 해의 띠 출력 하기 ]
입력받은 년도를 12로 나눈 나머지를 사용한다.
나머지가 0,1,2,3,4,5,6,7,8,9,10,11 일때
원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양, 띠입니다.
''')

year = int(input('태어난 연도 입력> '))
if year % 12 == 0:
	print('원숭이')
elif year % 12 == 1:
	print('닭')
elif year % 12 == 2:
	print('개')
elif year % 12 == 3:
	print('돼지' )
elif year % 12 == 4:
	print('쥐')
elif year % 12 == 5:
	print('소')
elif year % 12 == 6:
	print('범')
elif year % 12 == 7:
	print('토끼')
elif year % 12 == 8:
	print('용')
elif year % 12 == 9:
	print('뱀')
elif year % 12 == 10:
	print('말')
else:
	print('양')
