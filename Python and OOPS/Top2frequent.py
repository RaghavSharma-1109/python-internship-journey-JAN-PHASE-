def two_frequents(arr):

    first = -1
    second = -1
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) +1
    most_freq = None
    sec_most_freq = None
    for ch,value in freq.items():
        if value>first:
            second = first
            first = value

            sec_most_freq = most_freq
            most_freq = ch

        elif value>second and ch!= most_freq:
            sec_most_freq = ch
            second = value
    if len(arr)<2:
        return most_freq,None
    return most_freq,sec_most_freq
n = int (input('Enter number of elements for list:'))
arr = []
for i in range(n):
    arr.append(int(input()))


print(two_frequents(arr))
