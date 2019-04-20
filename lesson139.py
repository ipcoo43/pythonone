print('''[ 리스트에 요소 추가하기]
<리스트>.append(<요소>) : 뒷에 추가 한다.
<리스트>.insert(<위치>,<요소>) : 원하는 위치에 추가 한다.
<리스트>.extend(<리스트>) : 배열을 풀어서 뒷에 추가 한다.
''')

list_a = [1,2,3]
print(list_a)
list_a.append(4)    # list_a=[1,2,3,4]
print(list_a)
list_a.insert(0,0)  # list_a=[0,1,2,3,4]
print(list_a)
list_a.insert(1,10) # list_a=[0,10,1,2,3,4]
print(list_a)
list_a.extend([1,2,3,4]) # list_a=[0,10,1,2,3,4,1,2,3,4]
print(list_a)
list_a.append([1,2,3,4]) # list_a=[0,10,1,2,3,4,1,2,3,4,[1,2,3,4]]
print(list_a)