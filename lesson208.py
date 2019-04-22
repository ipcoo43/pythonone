print('''
- Library : 정상적인 제어를 하는 모듈
- Framework : 제어 역전(IoC : Inversion of Control)이 발생하는 모듈 
- 제어 정방향
 > 우리가 만든 코드 -> 모듈[다른 사람이 만든것] 이것을 라이브러리
- 제어 역방향
 > 우리가 만든 코드 <- 모듈[다른 사람이 만든것] 이것을 프레임워크
''')

from math import sin, cos, tan, floor, ceil

print('sin(1) =',sin(1))
print('cos(1) =',cos(1))
print('tan(1) =',tan(1))

print('floor(2.5) =',floor(2.5))
print('ceil(2.5) =',ceil(2.5))