
# 1. Write a Python program to calculate the length of a string.
'''
strln = 'gmail.com'
count = 0
for char in strln:
    count += 1
print('The length of the string is:', count)
'''

# 2. Write a Python program to count the number of characters (character frequency) in a string.
'''
freqstr = 'google.com'
freq = {}
for i in freqstr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print('The frequency of the characters is:', str(freq))
'''
# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#     If the string length is less than 2, return instead of the empty string.
'''
str = input('Enter the string:')
newstr = ''

if len(str) >= 2:
    newstr = str[0:2] + str[-2:]

print('The new string is:', newstr)
'''

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.

strfo = input('Enter the string: ')

char = strfo[0]
strfo = strfo.replace(char, '$')
strfo = char + strfo[1:]

print('The required string is:', strfo)

