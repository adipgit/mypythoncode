# Write a program read all the words from  the file which are starts with
# letter 'c'


f = open('file1.txt', 'r')
data = f.read()
f.close()

#print(data)

words = data.split()


for word in words:
    word = word.lower() # convets given string to lowerccase
    if word[0] == 'c':
        print(word)
