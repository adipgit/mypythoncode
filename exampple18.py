Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # dict
>>> d = {}
>>> 
>>> type(d)
<class 'dict'>
>>> 
>>> d = {"A": 65, "B": 66, "C": 67}
>>> 
>>> type(d)
<class 'dict'>
>>> 
>>> d.keys()
dict_keys(['A', 'B', 'C'])
>>> d.values()
dict_values([65, 66, 67])
>>> d
{'A': 65, 'B': 66, 'C': 67}
>>> # Dict are unordered or non-sequential data types in python
>>> d["A"]
65
>>> d["B"]
66
>>> d["M"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d["M"]
KeyError: 'M'
>>> 
>>> 
>>> 
>>> # dict is mutable object
>>> 
>>> 
>>> ist = {"KA": "BANAGLORE", "KL": "TRIVENDRUM", "TN": "CHENNI"}
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNI'}

>>> ist["KA"]
'BANAGLORE'
>>> 
>>> 
>>> # How to add new key value pair existing dict
>>> 
>>> # SYNTAX : dict[KEY] = <VALUE>
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNI'}
>>> ist["TS"] = "HYDERABAD"
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNI', 'TS': 'HYDERABAD'}
>>> 
>>> 
>>> ist["AP"] = "HYDERABAD"
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNI', 'TS': 'HYDERABAD', 'AP': 'HYDERABAD'}
>>> 
>>> 
>>> # Updating existing key value
>>> # SYNTAX  dict[KEY] = <VALUE>
>>> 
>>> ist['AP'] = "AMARAVATHI"
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNI', 'TS': 'HYDERABAD', 'AP': 'AMARAVATHI'}
>>> ist["AP"] = ["AMARAVATHI", "KURNUL", "VIZAG"]
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNI', 'TS': 'HYDERABAD', 'AP': ['AMARAVATHI', 'KURNUL', 'VIZAG']}
>>> 
>>> 
>>> ist["AP"]
['AMARAVATHI', 'KURNUL', 'VIZAG']
>>> 
>>> 
>>> # dict keys must be unique and it should immutable object
>>> 
>>> # dict values can be duplicated and it may any python object
>>> 
