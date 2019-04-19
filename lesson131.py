print('''
[ elif 구문 ]
if <조건A>:
	<조건A가 참일 때 실행할 문장>
elif <조건B>:
	<조건B가 참일 때 실행할 문장>
elif <조건C>:
	<조건C가 참일 때 실행할 문장>
else:
	<모든 조건이 거짓일 때 실행할 문장>
''')

import datetime
now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5 :
	print('이번 달은 {}월로 봄 입니다.'.format(month))
elif 6 <= month <= 8 :
	print('이번 달은 {}월로 여름 입니다.'.format(month))
elif 9 <= month <= 11 :
	print('이번 달은 {}월로 가을 입니다.'.format(month))
else:
	print('이번 달은 {}월로 겨울 입니다.'.format(month))
