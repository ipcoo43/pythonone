print('''
[ 숫자열을 문자열로 바꾸기 ]
- str(<다른 자료형>) : int(), float()와 비슷한 형태

- format()
 > '{} {}'.format(10,20)
''')

print('# str()로 변환')
str_int_a = str(52)
str_float_a = str(52.273)
print('str_int_a, type(str_int_a) =', str_int_a, type(str_int_a))
print('str_float_a, type(str_float_a) =', str_float_a, type(str_float_a))
print('str_int_a + str_float_a = ', str_int_a + str_float_a)
print()

print('# format() ')
str_a = '{},{}'.format(10,20)
print(str_a, type(str_a))