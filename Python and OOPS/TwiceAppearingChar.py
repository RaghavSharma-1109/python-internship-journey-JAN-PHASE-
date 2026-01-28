def twice_appear_char(s):
    freq = {}
    s = s.lower()
    for i in s:
        freq[i] = freq.get(i,0)+ 1
    for ch in s:
        if freq[ch] == 2:
            return ch
    return None

s = input('Enter your String:')
if twice_appear_char(s):
    print(f'The first character that appear twice is: {twice_appear_char(s)}')
else:
    print('No character that appear twice.')