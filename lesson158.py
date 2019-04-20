print('리스트에서 인덱스와 값을 출력하는 방법')

list_a = ['요소A','요소B','요소C']
print('list_a =',list_a)
print()

print('방법1) 인덱스 변수를 만들어 추가')
i=0
for item in list_a:
	print('{}번째 요소는 {} 입니다'.format(i,item))
	i += 1
print()

print('방법2) range(len(list_a))')
for i in range(len(list_a)):
	print('{}번째 요소는 {} 입니다'.format(i,list_a[i]))
print()

print('방법3) enumerate(list_a)')
for index,element in enumerate(list_a):
	print('{}번째 요소는 {} 입니다'.format(index,element))
print()