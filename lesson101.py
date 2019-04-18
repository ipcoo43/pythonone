print('''
[ 표현식(expression) 과 문장(statement)]
 값을 만들어내는 간단한 코드를 표현식이라고 한다. ( 값을 만들어내는 코드 )
 표현식이 하나 이상 모이면 문장이 되는데, 한 줄이 하나의 문장인 된다.
 문장이 모여 프로그램이 된다. 
 표현식이 모여 문장, 문장이 모여 프로그램이 된다.
  > 10
  > 10 + 20
  > '안녕하세요'

[ 키워드(keyword) ]
 키워드는 특별한 의미가 부여된 단어이다.
 파이썬이 만들어질 때 정해졌다.
  > Fasle, None, True, and, as, assert
  > break, class, continue, def, del, elif
  > else, except, finally, for, from, global
  > if, import, in, is, lambda, nonlocal
  > not, or, pass, raise, return, try
  > while, with, yield

[ 식별자(identifier) ]
 식별자는 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어
 주로 변수 또는 함수 이름등으로 사용된다.
 식별자는 기본적으로 아래와 같은 규칙을 지켜야 한다.
   > 키워드는 사용하면 안된다.
   > 특수 문자는 _만 허용된다.
   > 숫자로 시작하면 안 된다.
   > 공백을 포함할 수 없다.
 스네이크 케이스와 캐멀 케이스
   > i_am_a_boy : sanke_case (뱀처럼 생김)
   > IAmABoy : CamelCase (낙타등처럼 생김)
 sanke_case : 
   > hello_coding
   > hello_python
   > we_are_the_world
 CamelCase
   > HelloCoding
   > HelloPython
   > WeAreTheWorld
 snake_case : 변수(Variable) 
 snake_case() : 함수(Function)
 CamelCase : 클래스(Class)

[ 주석(comment) ]
 주석은 프로그램의 진해에 전혀 영향을 주지 않는 코드이다.
 프로그램을 설명하는 데 사용된다.
 파이썬에서는 '#' 기호를 붙여 주석 처리 한다.
   > # print()는 출력 함수 입니다.
   > print('Hello Welcome')

[ 연산자(Operator) ]
 단독으로 사용 할 때는 의미가 없지만 값과 값을 연결 할 때 의미가 생겨남
   > 1 + 1
   > 10 - 10

[ 자료[리터럴(Literal)] ] 
 값의 자체를 자료(리터럴)이라고 한다.
   > 10
   > 'Hello'
''')