# WAP count each occurance of a vowel from the given string


str1 = "banaglore"

d = {}  # place holder to store the output
vowels = "aeiou"
for ch in str1:
    if ch in vowels:
        if ch not in d:
            d[ch] = 1  #--> d --{'a':1}
        else:
            d[ch] = d[ch] +1
print(d)
        
    
