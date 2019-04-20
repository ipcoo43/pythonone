# 리스트 선언
array=[273,32,103,57,52]

# 리스트에 반복문 적용
for element in array:
	if element > 100:
		print(element, end=',')
print()

# 딕셔너리 선언 
dict_a = {
	'name':'건조 망고',
	'type':'당절임',
	'ingredient':['망고','설탕','메타중아황산나트륨','치자황색소'],
	'origin':'필리핀'
}

for key in dict_a:
	print('{} | {}'.format(key,dict_a[key]))
	print('-'*70)
	