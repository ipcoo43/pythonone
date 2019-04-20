list_a = [0,1,2]
print('list_a = ', end='')
for item in list_a:
	print(item,end=',' )
print()

dict_a = {'item': 0}
print('dict_a = ', end='')
for key in dict_a:
	print(key,':',dict_a[key],end=',')
print()

print('range(10) = ', end='')
for i in range(10):
	print(i, end=',')
print()
