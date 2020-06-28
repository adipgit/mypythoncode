# WAP count vowels from the given string

#str_input = input("Enter a string: ") # bangalore

str_input = 'bangalore'
# Traverse the string using for loop

#vowels = ['a', 'e', 'i', 'o', 'u']

#vowels = ('a', 'e', 'i', 'o', 'u')
vowels = "aeiou"
count = 0
for ch in str_input:
    if ch in vowels:
        count = count + 1
print(str_input)
print("vowels count ", count)
