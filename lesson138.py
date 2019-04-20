print('''
[ 리스트 ]
- 여러 가지 자료를 저장할 수 있는 자료
- 생성 방법 : [<요소(element)>,<요소>,<요소>,...]
- 사용 방법
 > 요소에 접근하기 : 리스트[인덱스] -> 0부터 시작
 > 리스트 결합하기 : 리스트 + 리스트 -> [1,2]+[3,4]
 > 리스트 반복하기 : 리스트 * 숫자 -> [1,2] * 2
 > 문자열과 비슷함
 > 요소의 범위를 벗어난 요소를 사용하면 에러 발생
''')

# 생성하기
list_a = []
list_b = [1,2,3,4,5,6]
list_c = [1,'반복문',3,True]
list_d = [[1,2,3],[4,5,6],[7,8,9]]

# 접근 연산자
print(list_b[0])
print(list_b[1])
print(list_b[-1])
print(list_b[-2])
print(list_c[1][0])
print(list_d)
print(list_d[1])
print(list_d[1][1])

# 결합/연결 연산자
print(list_b + list_c)

# 반복 연산자
print(list_b*3)