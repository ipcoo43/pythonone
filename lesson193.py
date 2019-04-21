print('''[예외를 강제로 발생 시키기]
raise <예외 객체>
raise NotADirectoryErro
https://github.com/keras-team/keras  -> search : raise
https://github.com/django/django  -> search : raise
raise NotImplementedError # 아직 구현 하지 않아서 생긴 에러
''')

try:
	raise NotADirectoryError('Message')
except NotADirectoryError as e:
	print(e)

def average_score(scores):
	for score in scores:
		if not 0 <= score <= 100:
			raise ValueError('점수이므로 0점과 100점 사이를 입력 해 주세요')
	return sum(scores) / len(scores)
	
average_score([100, 90, 30, 60, 50, 100])