list_a = ['원숭이','닭','개','돼지','쥐','소','범','토끼','용','뱀','말','양']

str_input = input('태어난 해을 입력해 주세요> ')
birth_year = int(str_input) % 12
print(list_a[birth_year], '띠입니다.')