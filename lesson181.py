list_a = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x*x, list_a)))
print(list(filter(lambda x:x<3, list_a)))