import textwrap
print(textwrap.dedent('''
[ 리스트,문자열,범위,딕셔너리와 함께 사용하는 함수 ]
- reversed() 함수로 리스트 뒤집기 : 역 반복문
'''))

list_a = [1,2,3,4,5,]
for i in list_a:
	print(i,end=',')
print()

for i in reversed(list_a):
	print(i,end=',')
print()