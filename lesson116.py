print('''
[ 문자열을 숫자로 바꾸기 ]
 - int() : 정수로 변환
 - float() : 실수로 변환
''')

print('# 두 수 정수 입력 하세요')
string_a = input('string_a> ')
int_a = int(string_a)
string_b = input('string_b> ')
int_b = int(string_b)

print('변환전 문자열 자료 string_a, string_b =>',type(string_a),',',type(string_b))
print('변환된 숫자열 자료 int(string_a), int(string_b) =>',type(int_a),',',type(int_b))
print('int_a + int_b =', int_a+int_b)
print('int_a - int_b =', int_a-int_b)
print('int_a * int_b =', int_a*int_b)
print('int_a / int_b =', int_a/int_b)
print()

print('# 두 수 실수/부동소수점 입력 하세요')
string_a = input('string_a> ')
float_a = float(string_a)
string_b = input('string_b> ')
float_b = float(string_b)

print('변환전 문자열 자료 string_a, string_b =>',type(string_a),',',type(string_b))
print('변환된 숫자열 자료 float(string_a), float(string_b) =>',type(float_a),',',type(float_b))
print('float_a + float_b =', float_a+float_b)
print('float_a - float_b =', float_a-float_b)
print('float_a * float_b =', float_a*float_b)
print('float_a / float_b =', float_a/float_b)