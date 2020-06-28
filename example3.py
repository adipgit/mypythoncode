Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> x = ()
>>> 
>>> type(x)
<class 'tuple'>
>>> 
>>> x = (10, 20, 30, 40)
>>> x
(10, 20, 30, 40)
>>> x[0]
10
>>> x[1]
20
>>> x[len(x)-1]
40
>>> y = (50, 60, 70, 80)
>>> y
(50, 60, 70, 80)
>>> 
>>> x+y
(10, 20, 30, 40, 50, 60, 70, 80)
>>> 
>>> x[2:6]
(30, 40)
>>> x[:7]
(10, 20, 30, 40)
>>> 
>>> x*3
(10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)
>>> 
>>> 
>>> 
>>> 
>>> # Diff b/w list and tuple
>>> 
>>> x = [10, 20, 30]
>>> x
[10, 20, 30]
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> y = (10, 20, 30)
>>> 
>>> y
(10, 20, 30)
>>> type(y)
<class 'tuple'>
>>> x = [10, 20.5, "ABC"]
>>> y = (10, 20.5, "ABC")
>>> x
[10, 20.5, 'ABC']
>>> y
(10, 20.5, 'ABC')
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> x
[10, 20, 30, 40]
>>> 
>>> # Change the 1st elemnet from the list
>>> 
>>> x[0] = 100
>>> x
[100, 20, 30, 40]
>>> 
>>> x[1] = 200
>>> x
[100, 200, 30, 40]
>>> 
>>> y = (10, 20, 30, 40)
>>> 
>>> y
(10, 20, 30, 40)
>>> type(y)
<class 'tuple'>
>>> y[0] = 1000
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    y[0] = 1000
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # Mutable Objects vs Immutable Objects
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> y = (50, 50, 70, 90)
>>> x
[10, 20, 30, 40]
>>> y
(50, 50, 70, 90)
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> tuple(x)
(10, 20, 30, 40)
>>> list(y)
[50, 50, 70, 90]
>>> 
