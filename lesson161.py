# 리스트의 함수
list_a = [52,273,103,32,57]

# 최소값과 최대값 구하기
# min_value = min(list_a)
# max_value = max(list_a)

# 최소값
min_value = list_a[0]
for element in list_a:
	if element < min_value:
		min_value = element

# 최대값
max_value = list_a[0]
for element in list_a:
	if element > max_value:
		max_value = element

# 출력
print('최소값 :', min_value) # 32
print('최대값 :', max_value) # 273