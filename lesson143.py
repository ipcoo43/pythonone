print('''
[ 딕셔너리 처리 ]
- 추가 : dict_a['new_name'] = 10
- 제거 : del dict_a['name']
- 확인 : key in dict_a
- 키에 없는 요소에 접근하면 에러 발생
''')

dict_a = {
	'name':'건조 망고',
	'type':'당절임',
	'ingredient':['망고','설탕','메타중아황산나트륨','치자황색소'],
	'origin':'필리핀'
}

dict_a['price'] = 5000   # 새로 생성
dict_a['name'] = '7D 건조 망고' # 수정
print(dict_a)

del dict_a['origin']
print(dict_a)

# 키에 없는 요소에 접근할 때 확인
print('name' in dict_a)
print('abss' in dict_a)

key = 'name'
if key in dict_a:
	print(dict_a[key])
else:
	print(key,'는 존재하지 않습니다.')


print(dict_a['name'])      # 없는 키에 접근하면 에러 출력
print(dict_a.get('name'))  # 없는 키에 접근하면 None 출력

name_value = dict_a.get('name')
if name_value != None:
	print(name_value)
else:
	print('키가 존재하지 않습니다')