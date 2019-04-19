print('''
[ 불(Boolean) ]
- True, False를 갖는 값
- 비교 연산자(비교 할 때 사용하는 연산자)
 > == : 같다
 > != : 다르다
 > < : 오른쪽이 크다
 > > : 왼쪽이 크다
 > <= : 오른쪽이 크거나 같다
 > >= : 왼쪽이 크거나 같다 
- 논리 연산자(불에 적용하는 연산자)
 > not : 아니다, 단항 연산자, True -> False, False -> True 
 > and : 그리고, 이항 연산자 
 > or  : 또는, 이항 연산자
- 단항 연산자 : 피연산자 하나 => 부호 연산자
 > -10
 > +10
- 이항 연산자 : 피연산자 두 개 => 숫자 연산자
 > 10 + 10
 > 10 - 10
''')

print('# 숫자 비교')
print('10 == 100 =>', 10 == 100 )
print('10 != 100 =>', 10 != 100 )
print('10 <  100 =>', 10 < 100 )
print('10 >  100 =>', 10 > 100 )
print('10 <= 100 =>', 10 <= 100 )
print('10 >= 100 =>', 10 >= 100 )
print()

print('# 문자열 비교')
print(" '가' < '하' =>",'가' < '하' )
print(" '가' > '하' =>",'가' > '하' )
print(sorted(['+','-','*','/','//','%']))
print()

print('# 논리 연산자 : not, 단항 연산자')
print('not True =', not True)
print('not False =', not False)
x=10
is_under_30 = x < 30
print('is_under_30 = 10 < 30 =>', is_under_30)
print('변수의 값을 반전해서 사용 not is_nuder_30 =',not is_under_30)
print()

print('# and - 둘 다 참일 때만 참')
print('True and True =', True and True)
print('False and True =', False and True)
print('True and False =', True and False)
print('False and False =', False and False)
print()

print('# or - 하나만 참일 때도 참')
print('True or True =', True or True)
print('False or True =', False or True)
print('True or False =', True or False)
print('False or False =', False or False)