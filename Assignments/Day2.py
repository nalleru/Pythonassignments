
# 9.Write a Python program to remove the nth index character from a nonempty string.

def remove_char(str, n):
    if str == ' ':
        print('The string is empty')

    else:
        start_string = str[:n]
        end_string = str[n + 1:]
        req_string = start_string + end_string
        return req_string


print(remove_char('Functions', 3))
print(remove_char(' ', 3))

# 10.Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
# in sorted form (alphanumerically).

words_input = input('Enter the sequence of words: ')
l = [e for e in words_input.split(',')]
result = ','.join(sorted(list(set(l))))
print('The sorted result is: ', result)


# 11. Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_string(str):
    if len(str) % 4 == 0:
        return ''.join(reversed(str))
    return str

print(reverse_string('Python'))
print(reverse_string('Learning'))

# 12.Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters
# in the first 4 characters

def upper_case(str):
    n = 0
    for e in str[:4]:
        if e.upper() == e:
            n = n+1

    if n >= 2:
        return str.upper()
    else:
        return str


print(upper_case('Python'))
print(upper_case('PytHon'))

# 13. Write a Python program to check whether a string starts with specified characters.

sw_str = 'Python is awesome'
print(sw_str.startswith('Python'))


# 14. Write a Python program to print the following floating numbers upto 2 decimal places.

n = 3.12345
print('The given number is : ', n)
print('The required number is: '+'{:.2f}'.format(n))


# 15.  Write a Python program to count repeated characters in a string.

import collections

str = 'Python is awesome'
d = collections.defaultdict(int)
for e in str:
    d[e] += 1

for e in sorted(d, key=d.get, reverse=True):
    if d[e] > 1:
        print('%s %d'%(e,d[e]))


# 16.Write a Python program to print the index of the character in a string.

str = 'Pace wisdom'
for index, char in enumerate(str):
    print('Character', char, 'Positioning at', index)


# 17.  Write a Python program to convert a string in a list.

def conv(str):
    l = list(str.split(' '))
    return l
print(conv('Alive is Awesome'))

# 18. Write a Python program to swap comma and dot in a string.

str = 'goo,gle.com'
temp = str.maketrans
result = str.translate(temp(',.', '.,'))
print(result)


# 19. Write a Python program to find smallest and largest word in a given string.

def minmaxlen_words(str):
    word =''
    words = []
    str = str + ' '
    for i in range(0, len(str)):
        if (str[i] != ' '):
            word = word + str[i]
        else:
            words.append(word)
            word = ''
    small = large = words[0]

    for e in range(0, len(words)):
        if (len(small) > len(words[e])):
            small = words[e]
        if (len(large) < len(words[e])):
            large = words[e]
    return small, large

str = 'Write a Python program'
print('The given string is:', str)
small, large = minmaxlen_words(str)
print('Smallest number is:', small)
print('largest number is:',  large)


# 20.Write a Python program to remove all consecutive duplicates of a given string.

from itertools import groupby

def rem_cons_dup(str):
    result = []
    for (key, group) in groupby(str):
        result.append(key)
    return ''.join(result)

str = 'xxxxxxyyyyyyyyyyyz'
print('The given string is:', str)
print('The required string is:', rem_cons_dup(str))









