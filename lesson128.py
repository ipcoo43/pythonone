print('''
[ 컴퓨터의 조건 ]
if <불 값>:
	<참일 때 실행할 문장>
< 불 값 사용 방법 >
- 홀수와 짝수 구분 방법
 > 4567 : 마지막의 자리 수의 숫자가 02468이면 짝수
''')

number = input('정수 입력> ')
last_character = number[-1]
last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
	or last_number == 4 \
	or last_number == 6 \
	or last_number == 8:
	print('짝수 입니다...')

if last_number == 1 \
    or last_number == 3 \
	or last_number == 5 \
	or last_number == 7 \
	or last_number == 8:
	print('홀수 입니다...')
