print('# 날짜 구하기')
import datetime
now = datetime.datetime.now() # 현재 시간이 들어감

print('now = datetime.datetime.now()')
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
print('now.year =',now.year)
print('now.month =',now.month)
print('now.day =',now.day)
print('now.hour =',now.hour)
print('now.minute =',now.minute)
print('now.second =',now.second)