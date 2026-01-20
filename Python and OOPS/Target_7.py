def target(arr, target):
    checked = set()
    pairs = []
    for num in arr:
        complement = target - num
        if complement in checked:
            pairs.append((complement,num))
        checked.add(num)
    
    return pairs

n = int(input('Enter number of elements for liat:'))
target_num = int(input('Enter you target number:'))
arr =[]
for i in range(n):
    arr.append(int(input('Enter element for list:')))

pairs = target(arr, target_num)
for pair in pairs:
    print('The target is achieved in',pair, end=';')
    
