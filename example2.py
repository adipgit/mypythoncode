Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # List demo
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> x
[10, 20, 30, 40]
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> # Indexing --> Access individual elements
>>> x[0]
10
>>> x[1]
20
>>> # To get the size of list object --> len(<objet>)
>>> len(x)
4
>>> x[len(x)-1]
40
>>> x[3]
40
>>> 
>>> # Concatenation
>>> x
[10, 20, 30, 40]
>>> y = [50, 60, 70, 80]
>>> y
[50, 60, 70, 80]
>>> x
[10, 20, 30, 40]
>>> y
[50, 60, 70, 80]
>>> x+y
[10, 20, 30, 40, 50, 60, 70, 80]
>>> z = x+y
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> # Slicing:
>>> 
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> z[2:5]
[30, 40, 50]
>>> z[2:]
[30, 40, 50, 60, 70, 80]
>>> z[:5]
[10, 20, 30, 40, 50]
>>> z[:]
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> 
>>> # Repetation
>>> x
[10, 20, 30, 40]
>>> x*3
[10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40]
>>> 
