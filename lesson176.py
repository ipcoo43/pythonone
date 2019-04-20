print('''
[ 메모화 ]
- 재귀 함수를 사용하면 코드가 간결 해진다.
- 문제점음 같은 값을 구하는 연산을 반복하고 있기 때문에 발생한다.
- 이런 문제점을 해결하기 위해 수정하는 방법이 메모화 이다.
- 메모화는 한번 구한 값을 어디엔가 메모 해 두는 것이다.
''')

# 메모 저장 할 수 있는 딕셔너리
dictionary = {
	1:1,
	2:1
}

# 함수 선언
def fibonacci(n):
	if n in dictionary:
		return dictionary[n]
	else:
		output = fibonacci(n-1) + fibonacci(n-2)
		dictionary[n] = output
		return output

# 함수 호출
print(fibonacci(10))
