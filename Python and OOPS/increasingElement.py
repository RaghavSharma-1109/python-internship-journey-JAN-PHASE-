def can_be_strictly_increasing(arr):
    removed = 0

    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            removed += 1
            if removed > 1:
                return False

            if i > 0 and arr[i - 1] >= arr[i + 1]:
                arr[i + 1] = arr[i]

    return True


n = int(input('Enter number of element for list:'))
arr = []
for i in range(n):
    arr.append(int(input('Enter element:')))
print(can_be_strictly_increasing(arr))
