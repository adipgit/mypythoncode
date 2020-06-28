Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # WAP convert the given string from BANGALORE to MANGALORE
>>> 
>>> s1 = "BANGALORE"
>>> 
>>> a = 'U'
>>> b = "U"
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> s1[0] = "M"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1[0] = "M"
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> t = (10, 20, 30)
>>> t[0] = 100
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> s1[0] = 'M'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s1[0] = 'M'
TypeError: 'str' object does not support item assignment
>>> 
>>> s1 = "BANGALORE"
>>> 
>>> s1[1:]
'ANGALORE'
>>> 
>>> "M" + s1[1:]
'MANGALORE'
>>> 
>>> 
