# 1 Write a Python program to check if a number is positive, negative or zero.
a = int(input())

if a < 0:
    print(a, " : is Negative number")
elif a == 0:
    print(a, " : 0")
else:
    print(a, " is  Positive number")

# 2 Write a Python program to get the Factorial number of given number.

num = int(input())
factorial = 1
if num < 0:
    print("we can't find factorial")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)

#  3   Write a Python program to get the Fibonacci series of given range

inp = int(input("fibonacci :"))
n1, n2 = 0, 1
count = 0
if inp <= 0:
    print('please enter positive number')
elif inp == 1:
    print(n1)
    print(inp)
else:
    print("fibonacci")
    while count < inp:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# 4 How memory is managed in Python?
#  Python memory manager takes care of the bulk of the memory management work and allows us to concentrate on our code.

# 5 What is the purpose continue statement in python?
# The continue keyword is used to end the current iteration in a for loop (or a while loop),
# and continues to the next iteration.

# 6 Write python program that swap two number with temp variable and
# without temp variable.

x = int(input("enter the value of x :"))
y = int(input('enter the value of y:'))

temp = x
x = y
y = temp
print('not x value is :', x)
print('not y value is :', y)

# without temp variable

x = 20
y = 30

print("before swaping numbers: ", x, " ", y)
x, y = y, x
print("after swapig numbera:", x, " ", y)

# 7 Write a Python program to find whether a given number is even or odd,  print out an appropriate message to the user

x = int(input())


def evenodd(x):
    if x % 2 == 0:
        print("your value is even number")
        else:
        if x % 2 != 0:
            print("your value is even")


print(evenodd(x))

# 8  Write a Python program to test whether a passed letter is a vowel or not.

x = input('find ,the letter is vowel or not   :')
vowel = 'aeiouAEIOU'
if x in vowel:
    print('yes Typed letter is vowel')
else:
    print('it is not vowel')
#
# 9  Write a Python program to sum of three given integers. However, if  two values are equal sum will be zero

x, y, z = int(input()), int(input()), int(input())

if x == y or y == z or z == x:
    plus = 0
    print(plus)
else:
    plus = x + y + z
    print('sum: ', plus)

#  10 Write a Python program that will return true if the two given integer  values are equal or their sum or difference
#  is 5.

x = int(input())
y = int(input())

plus = x + y
dif = x - y


def function(x, y):
    if x == y or plus == 5 or dif == 5:
        print(True)


function(x, y)
#
# 11  Write a python program to sum of the first n positive integers.

n = int((input()))

s = (n + 1) * n / 2
print(s)

#  12 Write a Python program to calculate the length of a string.

string = input()
a = len(string)
print('the length of this string is : ', a)

#  13 Write a Python program to count the number of characters (character frequency) in a string

str = input()


def function(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)


function(str)


#  14 Write a Python program to count the number of characters (character frequency) in a string

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(char_frequency('google.com'))

#  15 Write a Python program to count occurrences of a substring in a string.

string = input()
sub = input()
count = 0
for i in range(0, len(string)):
    stat = i
    end = i + len(sub)
    count = count + string.count(sub, stat, end)
print(count)

# 16 Write a Python program to count the occurrences of each word in a given sentence

sentence = input('type your sentence:')
word = input()
a = sentence.split(' ')
for i in range(0, len(a)):
    if word == a[i]:
        count += 1
    else:
        count = 1
print('word comes ', count, 'times')

# 17 Write a Python program to get a single string from two given strings,  separated by a space and swap the first two characters of each string.

a = 'xyz'
b = 'abc'
print(a, ' ', b)


def function(a, b):
    new_a = a[:2] + b[2:]
    new_b = b[:2] + a[2:]
    print(new_a, ' ', new_b)


function(a, b)
#

# 16  Write a Python program to add 'ing' at the end of a given string (length  should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it unchanged

a = input()
if len(a) >= 3:
    print(a + "ing")
    if a[-1:-3] == 'ing':
        print(a, 'ly')
else:
    print(a)


# 17 Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string.
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


# 18 Write a Python function that takes a list of words and returns the length of the longest one.
# a = ["one", "two", "third", "four"]

def longest(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if len(i) > max1:
            max1 = len(i)
            temp = i
    print('longest number is :', temp, 'the length of this word is ', max1)


#
longest(a)

# 19 Write a Python function to reverses a string if its length is a multiple of 4

a = input()


def reverse(a):
    if len(a) % 4 == 0:
        print(a[::-1])
    else:
        pass


reverse(a)

# 20  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

a = input()


def addto(a):
    if len(a) > 2:
        print(a[0:2] + a[-2:len(a)])
    else:
        print(' ')


addto(a)

# 21 Write a Python function to insert a string in the middle of a string.

test_str = 'car is for race'

print('the original sring ' + str(test_str))

mid_str = 'good'

temp = test_str.split()
mid_pos = len(temp) // 2

res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]
res = ' '.join(res)
print('formated: ', res)
