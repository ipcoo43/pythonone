print('''
[ 입력 ]
 - input() : 문자열 출력
 - 입력을 기다리는 현상을 불럭 이라고 한다.
 - 함수의 결과 값은 문자열로 리턴 된다.
''')

string = input('입력> ')
print(string, type(string))
print('input에 입력된 모든 값은 str(문자열)로 리턴 된다.')
print('숫자 123을 입력해도 리턴 값은 문자열')
print('불린 True, False를 입력해도 리턴 값은 문자열')
print()

print('두개의 입력 값을 받아서 계산')
string_a=input('입력A> ')
string_b=input('입력B> ')
print('string_a + string_b = ', string_a + string_b)
print('type(string_a) + type(string_b) = ', type(string_a),'+',type(string_b))