print('''
[ 튜플 ]
- 리스트와 같은데 요소를 변경 할 수 없다.
- 기본 생성 방법 : (<데이터>,<데이터>,<데이터>)
- 요소를 하나만 가지는 튜플 : (100,)
- 튜플을 사용한 할당 : (a,b)=(10,20)
- 튜플 생략하기 : (10,20) -> 10, 20
''')

test = (1,2,3,4,5)
print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])

[a,b]=[10,20]
c,d=30,40
print(a)
print(b)
print(c)
print(d)