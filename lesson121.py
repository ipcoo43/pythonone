print('''
[ 문자열 찾기 - find(), rfind() ]
- 문자열 내무에 특정 문자가 어디에 위치하는지 확인 할 때 사용
- find() : 왼쪽부터 찾아서 처음 등장하는 위치 찾는다.
- rfind() : 오른쪽부터 찾아서 처음 등장하는 위치 찾는다.
- "주어".서술어('목적어')
 > "안녕안녕하세요".find("안녕")
   ~에서.~해라(~을)
[ 문자열 in 연산자 ]
- 문자열 내부에 어떤 문자열이 있는지 확인만 하려면 in 연산자 사용
 > 문자열과 in 연산자
 > <문자열A> in <문자열B> # 문자열 B 내부에 문자열A가 있는지 확인
 > 출력은 True, False
''')

print('# 왼쪽 부터 찾기 find()')
output_a = "안녕안녕하세요".find("안녕")  # 0
print('find()', output_a)
print()

print('#오른쪽 부터 찾기 rfind()')
output_b = "안녕안녕하세요".rfind("안녕") # 2
print('findr()', output_b)
print()

print('# 문자열과 in 연산자')
print('"안녕" in "안녕하세요" =',"안녕" in "안녕하세요")
print('"잘자" in "안녕하세요" =',"잘자" in "안녕하세요")
print()

lis = ['*','/','+','-']
a = ['*','+','**']
for i in a:
	if i in lis:
		print('Yes : {}'.format(i))
	else:
		print('No : {}'.format(i))