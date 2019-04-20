print('파괴적 함수 : 원본 데이터에 영향을 미침 ')
list_a = [1,2,3,4]
print('원본 파일 : ',list_a)

list_a.append(1)
print('list_a.append(1)', list_a)

list_a.remove(2)
print('list_a.remove(2)', list_a)

list_a.pop()
print('list_a.pop()', list_a)