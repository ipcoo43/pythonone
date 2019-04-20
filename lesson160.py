print('리스트 내포')
# 변수 선언
list_a = []
# 반복문 적용
for i in range(0,20,2):
	list_a.append(i*i)
print(list_a)

print('''
프로그램 계발할 때 특수한 형태의 리스트를 사용할 때가 많다
list_a = []
for i in range(0,20,2):
	list_a.append(i*i)
이렇게 많이 사용하는 것을 짧게 표현 방법을 리스트 내포라고 한다.
list_b = [i * i for i in range(0,20,2)]
list_c = [i * i for i in range(0,20,2) if 100<i*i<300]
list_d = ['사과','자두','초콜릿','바나나','체리']
output = [fruit for fruit in list_d if fruit != '초콜릿']
''')

list_b = [i * i for i in range(0,20,2)]
print(list_b)

list_c = [i * i for i in range(0,20,2) if 100<i*i<300]
print(list_c)

list_d = ['사과','자두','초콜릿','바나나','체리']
output = [fruit for fruit in list_d if fruit != '초콜릿']
print(output)