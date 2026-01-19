def is_anagram(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    freq1 = {}
    freq2 = {}
    for i in s1.lower():
        if i not in freq1 :
            freq1[i] = 1

        else:
            freq1[i] += 1
    for i in s2.lower():
        if i not in freq2:
            freq2[i] = 1

        else:
            freq2[i] += 1
    if freq1.items() == freq2.items():
        return True
    else:
        return False

str1 = input("Enter first string:")
str2 = input("Enter second string:")
print(is_anagram(str1, str2))