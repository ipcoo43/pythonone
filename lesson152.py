print('''
[ continue keyword ]
- 반복문의 현재 단계를 넘어가는 키워드	
''')
# 변수 선언
numbers = [5,15,6,20,7,25]
# 반복 돌림
for number in numbers:
	# number가 10보다 작으면 다음 반복으로 넘어간다.
	if number < 10:
		continue
	print(number)

# 위 코드와 같은 결과
for number in numbers:
	# number가 10보다 작으면 다음 반복으로 넘어간다.
	if number >= 10:
		print(number)

# continue를 사용하는 이유는 들여쓰기가 복잡할 때 사용함
# break, continue는 적절하게 사용 해야 한다.