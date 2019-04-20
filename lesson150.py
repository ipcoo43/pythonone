import time # UNIX 타임 : 1970년 1월 1일 0시 0초 기준으로 몇 초

now_after_5 = time.time() + 5 # 실행 시점 + 5초 유닉스 초 

print('5초 기다리세요')
output = 0
while time.time() < now_after_5:
	output += 1
print('5초 동안 반복한 회수 : ', output)