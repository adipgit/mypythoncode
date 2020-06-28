Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # List Object (cont...)
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> x
[10, 20, 30, 40]
>>> 
>>> # Add the element at the end --> append(obejct)
>>> 
>>> x.append(50)
>>> x
[10, 20, 30, 40, 50]
>>> x.append(25)
>>> x
[10, 20, 30, 40, 50, 25]
>>> x.append(5)
>>> x
[10, 20, 30, 40, 50, 25, 5]
>>> # Add the element at the given index position --> insert(index, object)
>>> x.insert(35)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x.insert(35)
TypeError: insert expected 2 arguments, got 1
>>> x.insert(2, 35)
>>> 
>>> x
[10, 20, 35, 30, 40, 50, 25, 5]
>>> 
>>> 
>>> x.insert(5, 35)
>>> x
[10, 20, 35, 30, 40, 35, 50, 25, 5]
>>> 
>>> x.insert(7, 35)
>>> x
[10, 20, 35, 30, 40, 35, 50, 35, 25, 5]
>>> 
>>> 
>>> # To delete the element with given postion --> pop()
>>> 
>>> # pop([index]) --> index = size-1
>>> 
>>> x
[10, 20, 35, 30, 40, 35, 50, 35, 25, 5]
>>> 
>>> x.pop(3)
30
>>> x
[10, 20, 35, 40, 35, 50, 35, 25, 5]
>>> 
>>> 
>>> x.pop() # removes last element
5
>>> 
>>> x
[10, 20, 35, 40, 35, 50, 35, 25]
>>> 
>>> x.remove(10)
>>> x
[20, 35, 40, 35, 50, 35, 25]
>>> 
>>> 
>>> x.remove(35)# 1st occurance of 35
>>> x
[20, 40, 35, 50, 35, 25]
>>> 
>>> 
>>> x
[20, 40, 35, 50, 35, 25]

>>> x.sort()
>>> 
>>> x
[20, 25, 35, 35, 40, 50]
>>> 
>>> 
>>> x.reverse()
>>> x
[50, 40, 35, 35, 25, 20]
>>> 
>>> 
>>> x.index(25)
4
>>> 
>>> x.index(35)
2
>>> 
>>> x.count(20)
1
>>> x
[50, 40, 35, 35, 25, 20]

>>> x.count(35)
2
>>> 
>>> # Ask interpreter what properties are defined for the object
>>> # by using dir() ----> list the object properties
>>> 
>>> 
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> help(x.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> 
>>> 
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
