print('''
[ IndexError(index out of range) 예외 ]
- 리스트/문자열의 수를 넘는 요소/글자를 선택할 때 발생하는 에러
 > print('안녕하세요'[10])  # IndexError: string index out of range (문자열 인덱스 범위 넘음)
 > print('안녕하세요'[10])
          0 1 2 3 4 라는 인덱스를 갖고있는데 10이라는 넘는 숫자를 요구해서 에러 발생 
- IndexError 발생하면 선택 범위를 벗어나지 않았는지 확인
''')

print('''
[ Error ]
- SyntaxError : 구문 자체를 잘못 사용
 > print('안녕하세요'  # )를 닫지 않아서 SyntaxError

- TypeError : 연산자가 적용되는 자료형을 잘못 사용
 > Stringe('안녕하세요') + Integer(50) # TypeError

- IndexError : 범위를 넘는 부분을 선택 할 경우 발생
 > '안녕하세요'[10] # IndexError
''')
