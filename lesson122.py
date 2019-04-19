print('''
[ 문자열 자르기 : split(<자를 문자>) ]
- 문자열을 특정한 문자로 자를 때 사용
''')

output = '10 + 30 = 40'.split(' ')
print(output)
print()

a = input('입력> ').strip()
a = a.split(' ') 

for i in a:
	print(i, end=' ')
print()

