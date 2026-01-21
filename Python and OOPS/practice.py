def List_Rotation(list1,list2):
    if len(list1) != len(list2):
        return False
    parent = list1 + list1
    for i in range(len(list1)):
        match = True
        for j in range(len(list2)):
            if parent[i+j] != list2[j]:
                match = False
                break
        
        if match:
            return True
    return False
a =[]
for i in range(int(input('Enter the number of element of A:'))):
    a.append(int(input()))
b =[]
for i in range((int(input('Enter the number of element of B:')))):
    b.append(int(input()))

result = List_Rotation(a,b)
print(result)