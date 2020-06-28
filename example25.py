# Write a program count all the words from  the file1.txt which are starts with
# letter 'c' and count all the words which are strats with s from file2.txt

f = open('file1.txt', 'r')   # file1
data = f.read()
f.close()

words = data.split()
for word in words:
    if word.startswith('c'):
        print(word)

print("="*40)
f = open('file2.txt', 'r')  # file2
data = f.read()
f.close()

words = data.split()
for word in words:
    if word.startswith('s'):
        print(word)







