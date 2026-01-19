def SecondSmallest(arr):
    if len(arr)<2:
        print(f'No Second smallest in list.')
        return None
    sec_smallest = float('inf')
    smallest = float('inf')
    for i in arr:
        if i<smallest:
            sec_smallest = smallest
            smallest = i
        elif smallest < i < sec_smallest:
            sec_smallest = i
    if sec_smallest == float('inf'):
        return None
    
    return sec_smallest
    
n = int(input("enter number of element in list:"))
arr = []
for i in range(n):
    arr.append(int(input()))

second_small = SecondSmallest(arr)
if second_small == float('inf') or second_small == None :
    print("No second smallest.")
else:
    print(f"Second smallest : {second_small}")
    

