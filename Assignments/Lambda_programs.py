
# 1.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.

sum = lambda n: n + 15
prod = lambda x, y: x * y

print('Sum of the numbers is: ', sum(10))
print('Product of the numbers is: ', prod(12, 4))


# 2.Write a Python program to sort a list of tuples using Lambda.

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social science', 82)]
print('Original list of tuples: ')
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print('Sorting the List of Tuples: ')
print(subject_marks)


# 3.Write a Python program to sort a list of dictionaries using Lambda.

original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
                 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print('Original list of dictionaries :')
print(original_list)
sorted_list = sorted(original_list, key=lambda x: x['color'])
print('Sorting the List of dictionaries :')
print(sorted_list)


# 4. Write a Python program to find if a given string starts with a given character using Lambda.

given_char = input('Enter the character to check: ')
str1 = lambda x: True if x.startswith(given_char) else False
print(str1('Lambda'))
print(str1('Python'))


# 5.Write a Python program to check whether a given string is number or not using Lambda.

is_num = lambda x: x.replace('.', '', 1).isdigit()
print(is_num('-2.13'))
print(is_num('423'))
print(is_num('AD1'))
print(is_num('1DF'))
is_num1 = lambda y: is_num(y[1:]) if y[0] == '-' else is_num(y)
print(is_num1('-2.13'))


# 6.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda

l = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print('Original list: ')
print(l)
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), l))
print('Numbers of the above list divisible by nineteen or thirteen: ')
print(result)


# 7.  Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.

def matrix_sort(m):
    result = sorted(m, key=lambda matrix_row: sum(matrix_row))
    return result


m1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
m2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

print('Original Matrix: ')
print(m1)
print('Sort the said matrix in ascending order according to the sum of its rows: ')
print(matrix_sort(m1))
print('Original Matrix: ')
print(m2)
print('Sort the said matrix in ascending order according to the sum of its rows: ')
print(matrix_sort(m2))


# 8.Write a Python program to check whether a given string contains a capital letter, a lower case letter,
# a number and a minimum length using lambda.

def check_string(str1):
    mesg = [
        lambda str1: any(x.isupper() for x in str1) or 'String must have atleast one uppercase character',
        lambda str1: any(x.islower() for x in str1) or 'String must have atleast one lowercase character',
        lambda str1: any(x.isdigit() for x in str1) or 'String must have atleast one number',
        lambda str1: len(str1) >= 9 or 'String must have atleast 10 characters'
    ]
    result = [x for x in [i(str1) for i in mesg] if x != True]
    if not result:
        result.append('Valid string')
    return result

print(check_string('PaceWisd0m'))
print(check_string('PaceWisdom'))


# 9.Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.


def find_elements(str1, eles):
    result = list(filter(lambda x: eles in x, str1))
    return result


l = ['red', 'black', 'white', 'green', 'orange']
sub_string1 = 'ack'
sub_string2 = 'abc'

print('Original list: ')
print(l)
print('Substring to search: ')
print(sub_string1)
print('Elements of the said list that contain specific substring: ')
print(find_elements(l, sub_string1))
print('Substring to search: ')
print(sub_string2)
print('Elements of the said list that contain specific substring: ')
print(find_elements(l, sub_string2))


# 10. Write a Python program to sort a given mixed list of integers and strings using lambda.
# Numbers must be sorted before strings.


def sort_list(mixedlist):
    mixedlist.sort(key=lambda e: (isinstance(e, str), e))
    return mixedlist


l = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print('Original list: ')
print(l)
print('Sort the said mixed list of integers and strings: ')
print(sort_list(l))






















