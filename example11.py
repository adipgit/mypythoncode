# for - SYNATX
#Iteration statements (loops)
"""
        for  -- designed for sequnces (list, tuple, strings, dict)
        while -- count controlled operations , infinete loop
"""

"""
for <var> in <seq>:
    -------
    -------
    ------
"""
import time # modules

print("Iterating through list")
x = [10, 20, 30, 40]

for ele in x:
    # delay time 2 sec
    time.sleep(2) 
    print("Loop running with element ", ele)
print("="*50)
print("Traversing a tuple")
y =(10, 20, 30, 60)

for val in y:
    print(val)

print("="*50)
print("Traversing a string")

for ch in "BANGALORE":
    print(ch)
    



    


