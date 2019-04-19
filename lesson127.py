import datetime
now = datetime.datetime.now()
if 3 <= now.month <= 5: # 3보다 크거나 같거나, 5보다 작거나 같으면
	print('이번 달은 {}월로 봄 입니다.'.format(now.month))
if 6 <= now.month <= 8: # 6보다 크거나 같거나, 8보다 작거나 같으면
	print('이번 달은 {}월로 여름 입니다.'.format(now.month))
if 9 <= now.month <= 11: # 9보다 크거나 같거나, 11보다 작거나 같으면
	print('이번 달은 {}월로 가을 입니다.'.format(now.month))
if now.month == 12 or 1 <= now.month <= 2: # 12 또는 1보다 크거나 같거나, 1보다 작거나 같으면
	print('이번 달은 {}월로 겨울 입니다.'.format(now.month))
