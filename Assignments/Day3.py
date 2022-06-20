
# 1.Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included)

l = []
for e in range(1500,2701):
    if(e%7 == 0) and (e%5 == 0):
        l.append(str(e))
    result = (','.join(l))
print('The range of nos :', result)


# 2.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.


for x in range(0,6):
    if (x == 3):
        continue
    print(x, end=' ')


# 3. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz"
# instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both
# three and five print "FizzBuzz".

for x in range(0,51):
    if (x%3 == 0 and x%5 == 0):
        print('Fizzbuzz')
        continue
    elif (x%3 == 0):
        print('Fizz')
        continue
    elif (x%5 == 0):
        print('Buzz')
        continue
    print(x)


# 4. Write a Python program to check a triangle is equilateral, isosceles or scalene.

print('Enter the lengths of sides of the triangle')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if (x == y == z) :
    print('Equilateral triangle')
elif (x == y or x== z or y == z):
    print('Isosceles triangle')
else:
    print('Scalene triangle')


# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user).
# Input 0 to finish

print('Input some integers to calculate their sum and average. Input 0 to exit.')

count =0
sum = 0
number = 1

while number != 0:
    number = int(input(''))
    sum = sum + number
    count += 1
if count == 0:
    print('Input some numbers')
else:
    print('Sum of the numbers: ', sum)
    print('Average of the numbers: ', sum/(count-1))


# 6. Write a Python program to construct the following pattern, using a nested loop number.

for i in range (1,10):
    print(str(i) * i)


# 7. Write a Python program that counts the number of elements within a list that are greater than 30

def count_elements(l, min):
    n = 0
    for e in l:
        if min < e:
            n += 1
    return n

l1 = [10,20,30,40,50,60,70,80,90,100]
print(count_elements(l1, 30))


# 8.Take values of length and breadth of a rectangle from user and check if it is square or not.

x = int(input('Enter the length of the rectangle: '))
y = int(input('Enter the breadth of the rectangle: '))

if x == y:
    print('This is a square!!')
else:
    print('This is not a square!!')


# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity

quantity = int(input('Enter the quantity: '))
amount = quantity * 100

if quantity > 1000:
    discount = amount * 0.1
else:
    discount = 0

net_amount = amount - discount

print('The total cost is: ', net_amount)


# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

sal = int(input('Enter the salary: '))
year = int(input('Enter the years of service: '))

if year > 5:
    net_bonus = sal * 0.05
else:
    net_bonus = 0

print('The Net bonus amount is : ', net_bonus)


# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = int(input('Enter the marks obtained: '))

if marks < 25:
    grade = 'F'
elif 25 <= marks < 45:
    grade = 'E'
elif 45 <= marks < 50:
    grade = 'D'
elif 50 <= marks < 60:
    grade = 'C'
elif 60 <= marks <=80:
    grade = 'B'
else:
    grade = 'A'

print('The Grade obtained is: ', grade)


# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = int(input('Enter the number of classes held: '))
classes_attended = int(input('Enter the number of classes attended: '))
margin = classes_held * 0.75

if classes_attended >= margin:
    print('The student is eligible to attend the exam!!')

else:
    print('The student is not eligible to attend the exam!!')


# 13. Take 10 integers from keyboard using loop and print their average value on the screen.


sum = 0
for i in range(0,10):
     n = float(input('Enter the number: '))
     sum += n

avg = sum / 10
print('The average of numbers = ', avg)


# 14. Print multiplication table of 24, 50 and 29 using loop.

num = int(input('Enter the table: '))
print('Multiplication table of {}'.format(num))
i = 1
while i <= 10:
    print(num, '*', i, '=', num * i)
    i += 1


# 15.Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.

print('Input some numbers to calculate their average and product. Input q to exit')
count = 0
sum = 0
prod = 1

while True:
    number = input('Enter the number: ')
    if number == 'q':
        break
    number = int(number)
    sum = sum + int(number)
    prod = prod * int(number)
    count += 1

if count == 0:
    print("Enter some numbers: ")
else:
    print('The Average of the numbers is: ', sum/(count-1))
    print('The Product of the numbers is: ', prod)


# 16.Take inputs from user to make a list.
# Again take one input from user and search it in the list and delete that element, if found.
# Iterate over list using for loop.

number_list = []
x = int(input('Enter the number of elements in the list: '))
for i in range(x):
    number_list.append(int(input()))

del_num = int(input('Enter the number to be deleted: '))

i = 0
for e in number_list:
    if (e == del_num):
        number_list.remove(e)
        x = x-1
        i = i-1
print(number_list)


# 17. Using range(1,101), make three list,
# one containing all even numbers
# one containing all odd numbers
# One containing only prime numbers..

prime_list = []
even_list = []
odd_list = []


for num in range(1,101):
    if (num % 2 == 0):
        even_list.append(num)
    else:
        odd_list.append(num)

for e in range(1,101):
    if e > 1:
        for i in range(2, e):
            if (e % i == 0):
                break
        else:
            prime_list.append(e)



print('The list of prime numbers are: ', prime_list)
print('The list of even numbers are: ', even_list)
print('The list of odd numbers are: ', odd_list)


# 18. From the two list obtained in previous question, make new lists, containing only numbers which are
# divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists

div_4 = []
div_6 = []
div_8 = []
div_10 = []
div_3 = []
div_5 = []
div_7 = []
div_9 = []
even_list.extend(odd_list)
even_list.sort()

for n in even_list:
    if (n % 4) == 0:
        div_4.append(n)
    if (n % 6) == 0:
        div_6.append(n)
    if (n % 8) == 0:
        div_8.append(n)
    if (n % 10) == 0:
        div_10.append(n)
    if (n % 3) == 0:
        div_3.append(n)
    if (n % 5) == 0:
        div_5.append(n)
    if (n % 7) == 0:
        div_7.append(n)
    if (n % 9) == 0:
        div_9.append(n)


print('The list of numbers divisible by 4 are : ', div_4)
print('The list of numbers divisible by 6 are : ', div_6)
print('The list of numbers divisible by 8 are : ', div_8)
print('The list of numbers divisible by 10 are : ', div_10)
print('The list of numbers divisible by 3 are : ', div_3)
print('The list of numbers divisible by 5 are : ', div_5)
print('The list of numbers divisible by 7 are : ', div_7)
print('The list of numbers divisible by 9 are : ', div_9)


# 19.  From a list containing ints, strings and floats, make three lists to store them separately

l = [2, 3.5, 'python', 7.8, 'hello', 6]

x = []
y = []
z = []

for i in l:
    if type(i) == int:
        x.append(i)
    elif type(i) == float:
        y.append(i)
    elif type(i) == str:
        z.append(i)

print('The list of integers is: ', x)
print('The list of floats is: ', y)
print('The list of strings is: ', z)


# 20. You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

l1 = [1, 2, 3, 4]
l2 = []

for i in l1:
    l2.append(i*i)

print('The given list is : ', l1)
print(('The obtained square list is : ', l2))





