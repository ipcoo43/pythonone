print('''[ 리스트에 요소 제거하기]
<리스트>.pop(<제거할 위치>) : 하나만 제거
del <리스트>[<인덱스>]
[ 리스트의 요소 모두 제거하기]
<리스트>.clear() : 모두 제거
''')

list_a = [1,2,3]
print(list_a)
list_a.pop(0)  # list_a = [2,3]
print(list_a)
list_a.pop()   # list_a = [2]
print(list_a)
list_a.clear() # list_a =[]
print(list_a)

# del <list>[<index>]
list_a=[1,2,3]
del list_a[2]  # list_a= [1,2]
del list_a[0]  # list_a= [2] 
print(list_a)

list_a=[1,2,3]
list_a.pop(-2) # [1,3]
print(list_a)  
del list_a[-1] # [1]
print(list_a)

# in 연산자
list_a=[1,2,3]
print( 1 in list_a)