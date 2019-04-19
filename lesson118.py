print('''
[ 문자열의 추가적인 기능 ]
- dir(str)
- function : 사물의 기능을 갖음
- 문자열 기능 : 자기 자신을 변화 시키지 않음 (string)
  > string = 'Hello'
- 문자열에 추가적인 기능만 리턴함
  > returned = string.upper 
  > print(string) # Hello  자기 자신 변환 없음
  > print(returned) # HElLO 추가 기능을 넣어 리턴된 값만 변화
''')

class Sample:
	def __dir__(self):
		return dir('문자열')
v = Sample()
# print(dir(v))

string = 'Hello World'
returned = string.upper()
print("string = 'Hello World'")
print("returned = string.upper()")
print('자기자신(string) : ',string)
print('string.대문자(upper) :',returned)