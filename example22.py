"""
open -- read -- close

open -- update -- close

open -- write -- close


open --> read/write/append --> close
"""

# <file_object> open(<filepath>, mode)
# mode - read(r) write(w)  append(a)
"""
open() function retunrns a file object

"""

f = open('file1.txt', 'r')
data = f.read() # returns entire data from the file as a string
f.close()

print(type(data))
print(data)
