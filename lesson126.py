	# 날짜/시간과 관련된 기능을 가져 온다
import datetime
	# 현재 날짜/시간을 구한다
now = datetime.datetime.now()
print('오늘은 {}년 {}월 {}입니다.'.format(now.year, now.month, now.day))
	# 오전 구분
if now.hour < 12:
	print('현재 시간은 {}시 {}분으로 오전입니다.'.format(now.hour,now.minute))
	# 오후 구분
if now.hour >= 12:
	print('현재 시간은 {}시 {}분으로 오후입니다.'.format(now.hour,now.minute))