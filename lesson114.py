print('''
[ 복합 대입 연산자 ]
- 변수와 함께 사용할 수 있는 연산자
- 대입 연산자 : a = 10
 > 오른쪽의 10의 값을 a에 넣는다.
 > a = a + 10
- 복합 대입 연산자
 > a += 10
[ 숫자에 적용하는 복합 대입 연산자 ]
 - += : 숫자 덧셈 후 대입
 - -= : 숫자 뺄셈 후 대입
 - *= : 숫자 곱셈 후 대입
 - /= : 숫자 나눗셈 후 대입
 - %= : 숫자 나머지 구한 후 대입
 - **= : 숫자 제곱 후 대입
[ 문자열에 적용하는 복합 대입 연산자 ]
 - += : 문자열 연결 후 대입
 - *= : 문자열 반복 후 대입
''')

print('# 대입 연산자')
a = 10
print('a = {}'.format(a))
a = a+10
print('a=a+10 =>',a)
a = a+10
print('a=a+10 =>',a)
print()

print('# 복합 대입 연산자')
a = 10
print('a = {}'.format(a))
a += 10
print('a += 10 =>',a)
a += 10
print('a += 10 =>',a)
print()

print('# 숫자 복합 대입 연산자')
number = 100
print('number =',number)
number += 10
print('number +=10 =>',number)
number += 20
print('number +=20 =>',number)
number += 30
print('number +=30 =>',number)
print()

print('# 문자열 복합 대입 연산자')
string = '안녕하세요'
print('string =',string)
string += '!'
print('string += "!" =>',string)
string += '!'
print('string += "!" =>',string)