Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "The Zen of Python, by Tim Peters"
>>> 
>>> str1.split(' ')
['The', 'Zen', 'of', 'Python,', 'by', 'Tim', 'Peters']
>>> str1.split('y')
['The Zen of P', 'thon, b', ' Tim Peters']
>>> ip = "10.221.49.88"
>>> 
>>> ip.split('.')
['10', '221', '49', '88']
>>> 
>>> # split vs join
>>> 
>>> x = ip.split('.')
>>> 
>>> x
['10', '221', '49', '88']
>>> "======".join(x)
'10======221======49======88'
>>> ".".join(x)
'10.221.49.88'
>>> 
>>> 
>>> 
>>> str1.split()
['The', 'Zen', 'of', 'Python,', 'by', 'Tim', 'Peters']
>>> 
>>> 
>>> 
