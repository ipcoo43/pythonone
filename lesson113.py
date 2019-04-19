print('''
[ 변수(variable) ]
- 변수 : 변 할 수 있는 자료
- 변수 선언 : 변수 생성
  > π 사용하겠다! -> 변수 선언
- 변수 할당 : 변수에 값을 넣는 것
  > π = 3.14159265 -> 변수 할당
- 변수 참조 : 변수에서 값을 꺼내는 것
  > 2 * π * r -> 변수 참조
  > π * r * r -> 변수 참조
''')

pi = 3.14159265 # 변수 선언과 할당
r=10
print('pi={}, r={}'.format(pi,r))
print('2*pi*r =',2*pi*r)  # 변수 참조
print('pi*r*r =',pi*r*r)  # 변수 참조