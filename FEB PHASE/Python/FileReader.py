from StringCleaner import word_count

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:# open and read
            f_content= f.read()
            return f_content
                
    except FileNotFoundError:
        return None
def analyze_file(filepath):
    contents = read_file(filepath)
    if contents is None:
        return None

    return {
        "lines": len(contents.splitlines()),
        "words": len(contents.split()),
        "characters": len(contents)
    }
def most_frequent_word(filepath):
    contents = read_file(filepath)
    if contents is None:
        return None

    counts = word_count(contents)
    if not counts:
        return None

    return max(counts, key=counts.get)
