def twice_appear_char(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0)+ 1
    max_freq = max(freq.values())
    result = None
    sec_freq = float('-inf')
    for ch,frequency in freq.items():
        if  frequency == 2 and sec_freq<max_freq and frequency>sec_freq:
            result = ch
            sec_freq = frequency
    if result:
        return result
    else:
        return None
s = input('Enter your String:')
print(twice_appear_char(s))