str_input = input('태어난 해를 입력해주세요> ')
birth_year = int(str_input) % 12
lst = ['원숭이','닭','개','돼지','쥐','소','범','토끼','용','뱀','말','양']

print(lst[birth_year], "띠입니다.")

