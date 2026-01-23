def len_longest_substring(s):
    left = 0
    seen =set()
    max_length = 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[i])
        max_length = max(max_length, i-left+1)

    return max_length
s = input('Enter your string:')
result = len_longest_substring(s)
print(result)