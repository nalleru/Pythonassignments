

# 1. Write a python class to convert an integer into a roman numeral and viceversa.

class Convert:
    def int_roman(self, num):
        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        result = ''
        for (n, roman) in lookup:
            (d, num) = divmod(num, n)
            result = result + roman * d

        return result

    def roman_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(0, len(s)):
            if (i > 0 and rom_val[s[i]] > rom_val[s[i-1]]):
                int_val = int_val + rom_val[s[i]] - 2 * rom_val[s[i-1]]

            else:
                int_val = rom_val[s[i]]
        return int_val


#print(Convert().int_roman(755))
#print(Convert().roman_int('CM'))

# 2.  Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class ValidParanthesis:

    def is_valid_paranthesis(self, str1):
        stack, pchar = [], {'(': ')', '{': '}', '[': ']'}
        for paranthesis in str1:
            if paranthesis in pchar:
                stack.append(paranthesis)
            elif len(stack) == 0 or pchar[stack.pop()] != paranthesis:
                return False

        return len(stack) == 0


#print(ValidParanthesis().is_valid_paranthesis('()'))
#print(ValidParanthesis().is_valid_paranthesis('({['))


# 3.Write a Python class to get all possible unique subsets from a set of distinct integers

class Subsets:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]


#print(Subsets().sub_sets([1, 4, 8]))


# 4.  Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number.

class Target:
    def pair_elements(self, numbers, target):
        lookup = {}
        for i, num in enumerate(numbers):
            if (target - num) in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

#print(Target().pair_elements((1,2,3,4,5), 5))


# 5.Write a Python class to find the three elements that sum to zero from a set of n real numbers.

class Realnumbers:
    def zerosum(self,nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) -2:
            j, k = i+1, len(nums) - 2
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        return result


#print(Realnumbers().zerosum([-2, -3, -7, 5, 10, -25, 2, 8]))


# 6.Write a Python class to implement pow(x, n)

class Powers:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        val = self.pow(x, n//2)
        if n % 2 == 0:
            return val * val
        return val * val * x

#print(Powers().pow(2, 2))
#print(Powers().pow(2,-1))
#print(Powers().pow(5,-3))


# 7.  Write a Python class to reverse a string word by word.

class Reverse:
    def reverse_str(self, str1):
        l1 = str1.split()
        l2 = reversed(l1)
        result = ' '.join(l2)
        return result


#print(Reverse().reverse_str('hello .py'))
#print(Reverse().reverse_str('python programming is awesome'))


# 8. Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user
# and print_string prints the string in reverse order

class StringIO:
    def __int__(self):
        self.str1 = ''

    def get_string(self):
        self.str1 = input('Enter the string: ')
        return self.str1

    def print_string(self, str1):
        s = str1.split()
        print(' '.join(reversed(s)))


'''
str1 = StringIO()
str2= str1.get_string()
str1.print_string(str2)
'''

# 9. Write a Python class named Circle constructed by a radius
# and two methods which will compute the area and the perimeter of a circle.


class Circle:
    def __int__(self, r):
        self.r = r
    def area(self):
        return self.r**2*3.14
    def perimeter(self):
        return self.r*2*3.14

'''
NewCircle = Circle(4)
print(NewCircle.area())
print(NewCircle.perimeter())
'''

# 10. Write a Python program to get the class name of an instance in Python.

class Car:
    def name(self, name):
        return name
    
c = Car()
print(c.__class__.__name__)























