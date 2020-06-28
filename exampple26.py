def read_file(filepath):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data

def get_words_delim(str1, ch):
    words = str1.split()
    output = []
    for word in words:
       if word.startswith(ch):
           output.append(word)
    return output



data1 = read_file('file1.txt')
print(get_words_delim(data1, 'c'))
print("="*50)
data2 = read_file('file2.txt')
print(get_words_delim(data2, 's'))
