
# 1. Write a Python program to calculate the length of a string.

strln = 'gmail.com'
count = 0
for char in strln:
    count += 1
print('The length of the string is:', count)


# 2. Write a Python program to count the number of characters (character frequency) in a string.

freqstr = 'google.com'
freq = {}
for i in freqstr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print('The frequency of the characters is:', str(freq))

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#     If the string length is less than 2, return instead of the empty string.

str = input('Enter the string:')
newstr = ''

if len(str) >= 2:
    newstr = str[0:2] + str[-2:]

print('The new string is:', newstr)


# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.

strfo = input('Enter the string: ')

char = strfo[0]
strfo = strfo.replace(char, '$')
strfo = char + strfo[1:]

print('The required string is:', strfo)


#  5.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
newstr1 = str2[:2] + str1[2:]
newstr2 = str1[:2] + str2[2:]
reqstr = newstr1 + ' ' + newstr2

print('The required string is: ', reqstr)


# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def add_str(str):
    if len(str) > 2:
        if str[-3:] == 'ing':
            str = str + 'ly'
        else:
            str = str + 'ing'

    return str

#print(add_str('st'))
#print(add_str('bat'))
#print(add_str('ping'))

# 7.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def add_good(str):
    inot = str.find('not')
    ipoor = str.find('poor')
    if ipoor > inot and inot > 0 and ipoor > 0:
        str = str.replace(str[inot:(ipoor+4)], 'good')
        return str
    else:
        return str

#print(add_good('The lyrics is not that poor'))
#print(add_good('The lyrics is poor'))

# 8.Write a Python function that takes a list of words and returns the length of the longest one.

def long_str(str):
    strlen = []
    for i in str:
        strlen.append((len(i), i))
    strlen.sort()
    return strlen[-1][0], strlen[-1][1]
#result = long_str(['Python', 'PHP', 'Django', 'Scala'])

#print('Longest word is: ', result[1])
#print('Length of th longest word is: ', result[0])

#







