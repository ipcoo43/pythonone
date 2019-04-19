print('''
[ 연산자의 우선 순위 ]
 - 곱하기와 나누기가 우선
 - 더하기와 빼기가 다음으로 우선
 - 잘 모르겠을 때는 괄호 치기
 - 명시적 : 일부러 2+(3*2)
''')

print('// - 정수 나누기')
print('5/2 => 몫={}, 나머지={}'.format(5//2, 5%2))
print()

print('** - 제곱 연산자')
print('2**2 = 2^2 = 2 * 2 = {}'.format(2**2))
print('2**3 = 2^3 = 2 * 2 * 2 = {}'.format(2**3))
print()

print('# 연산자의 우선 순위')
print('5+3*2 = 5+{} = {}'.format(3*2, 5+6))

print('2+2-2*2/2*2 =',2+2-2*2/2*2)
print('2-2+2/2*2+2 =',2-2+2/2*2+2)

print('5//2 =',5//2)
print('5**2 =',5**2)
print('5+3*2 =',5+3*2)
print('5+(3*2) =',5+(3*2))
print('(5+3)*2 =',(5+3)*2)

print('# 문자열 연산자의 우선순위')
print("'안녕 '+'하세요 '*3 =", '안녕 '+'하세요 '*3)