Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # String
>>> 
>>> s1 = "Single Quotes"
>>> s1 = "Double Quotes"
>>> s2 = 'Single Quotes'
>>> type(s1)
<class 'str'>
>>> type(s2)
<class 'str'>
>>> str1 = "BANGALORE"
>>> 
>>> type(str1)
<class 'str'>
>>> len(str1)
9
>>> # String is seq object
>>> str1[0]
'B'
>>> str1[1]
'A'
>>> str1[len(str1)-1]
'E'
>>> 
>>> str2 = " City"
>>> 
>>> str1+str2
'BANGALORE City'
>>> 
>>> 
>>> str3 = str1+str2
>>> 
>>> str3
'BANGALORE City'
>>> 
>>> str3[3:8]
'GALOR'
>>> 
>>> str3[0:8]
'BANGALOR'
>>> str3[0:]
'BANGALORE City'
>>> str1 * 4
'BANGALOREBANGALOREBANGALOREBANGALORE'
>>> 
>>> 
>>> a = 10
>>> 
>>> a
10
>>> 
>>> type(a)
<class 'int'>
>>> 
>>> a = 30
>>> 
>>> type(a)
<class 'int'>
>>> a
30
>>> 
