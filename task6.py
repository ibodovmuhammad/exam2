list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
new_list = []
for i in range(len(list1)):
    new_list.append(str(list1[i]) + list2[i])

print(new_list)