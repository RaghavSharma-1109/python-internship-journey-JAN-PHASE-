def first_non_repeating(s):
    s = s.replace(' ', '').lower()
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0) +1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
s = input('Enter your string:')
result = first_non_repeating(s)
if result :
    print(f'First non repeating character in you string is: {result}')
else:
    print('No first non repeating character in your stiring.')