print('''
[ 딕셔너리 ]
- 일반적으로 문자열을 기반으로 값을 저장하는 것
- {<키>:<값>}
- 리스트 : list_a[1] -> 인덱스
- 딕셔너리 : dict_a['name'] -> 키
''')
# 딕셔너리 생성
dict_a = {
	'name':'건조 망고',
	'type':'당절임',
	'ingredient':['망고','설탕','메타중아황산나트륨','치자황색소'],
	'origin':'필리핀'
}

print(dict_a['name'])
print(dict_a['type'])
print(dict_a['ingredient'])
print(dict_a['ingredient'][0])
print(dict_a['ingredient'][1])
print(dict_a['origin'])
