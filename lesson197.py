import random

print('random.random() =>0부터 1사이 =',random.random())
print('random.uniform(10,20) =>10부터 20사이 =',random.uniform(10,20))
print('random.randrange(10) =>0부터 10까지 정수 =',random.randrange(10))
print('random.randrange(0,11,2) =>1부터 10까지중 짝수  =',random.randrange(0,11,2))
print('random.choice(["a","b","c"]) => 리스트 중에서 뽑기 =',random.choice(['a','b','c']))
a=[1,2,3,4,5,6,7,8]
random.shuffle(a)
print('random.shuffle([range(1,8)]) => 리스트 섞기 =',a)