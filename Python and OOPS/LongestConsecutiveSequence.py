def longest_consec(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for i in num_set:
        if i-1 not in num_set:
            start = i
            length = 1
            while start +1 in num_set:
                start += 1
                length += 1
            longest = max(longest,length)
    return longest

num = []
n =int(input("Enter number of elements in list:"))
for i in range(n):
    num.append(int(input()))
result = longest_consec(num)
if result:
    print(f'The longest Consecutive sequence in you list is of lenght: {result}')
else:
    print('List can not be empty.')