# 변수 선언
list_test = [1,2,1,2]
value = 2
# list_test 내부에 value가 있다면 반복
while value in list_test:    # 2 < [1,2,1,2], 2<[1,1,2]
	list_test.remove(value)  # [1,1,2], [1,1]

print(list_test)  # [1,1]