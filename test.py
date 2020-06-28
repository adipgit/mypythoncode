file = open('PythonImport.txt', 'r')
data = file.read();
file.close();
print("reading a file")
#print(data);

# write a program to read all the words from the file 
# which starts with letter c

fileData = data.split(' ')

for i in fileData:
    
    if(i[0] == 'c'):
        print(i, i[0])
        #print(i)
