def Unique_Elements(arr):
    if arr == 0:
        return None
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    unique_elememt = []
    for key, value in freq.items():
        if value == 1:
            unique_elememt.append(key)
    if unique_elememt:
        return unique_elememt
    else:
        return None

element = []
n = int(input("Enter the number of elements:"))
for i in range(n):
    element.append(int(input("Enter your element:")))

result = Unique_Elements(element)
if result == None:
    print("The list is empty or no unique element.")
else: 
    for i in result:
        print(i, end=';')

