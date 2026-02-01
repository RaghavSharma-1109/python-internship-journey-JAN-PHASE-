def clean_string(s):
    if not s:
        return None
    s = s.lower()
    punctuation = '.,!?'
    for ch in punctuation:
        s = s.replace(ch,'')
    s = " ".join(s.split())
    return s

def word_count(s):
    cleaned = clean_string(s)
    if not cleaned:
        return {}
    cleaned = cleaned.split()
    count = {}
    for word in cleaned:
        count[word] = count.get(word,0) +1
    return count
s= input('Enter your string:')
cleaned_string = clean_string(s)
print(cleaned_string)
print(word_count(s))

