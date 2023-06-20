# 1  What is List ? how to revers a list
# A list in Python is used to store the sequence of various types of data.
# A list can be defined as a collection of values or items of different types.
# import random

# now reversing a list

# a = [1,2,3,"hitesh",0.5,6]
# print(a[::-1])


# 2  How will you remove last object from a list?  Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

# a = [1,2,3,4,5,'hitesh']
# a.pop()
# print(a)

# list1 = [2,33,222,14,25]
# print(list1[-1])
# (ans = 25)

# 3 Differentiate between append () and extend () methods?
# Python List Append VS Python List Extend – The Difference ...append() adds a single element to the end of the list while .
# extend() can add multiple individual elements to the end of the list.


# 4 Write a Python function to get the largest number, smallest num and sum  of all from a list.

# list1 = [1,28,20.3,30,70,111,200,35]

# def  large_small_sum(list1):
# for maximum number
# a = max(list1)

# for minimum number
# b = min(list1)

# for sum of all number
# c = sum(list1)

# print("maximum number:",a," minimum number:",b," sum of all number:",c)
# large_small_sum(list1)

# 5 How will you compare two lists?


# 6  Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given  list of strings.

# list1 = ['abc', 'xyz', 'aba', '1221']
# count = 0

# for i in list1:
#     if len(i)>= 2 and  i[0]==i[-1]:
#         count +=1
# print(count)


# 7 Write a Python program to remove duplicates from a list.

# ls1 = [1,2,515,'hnk',1.3,2,3,1]
# c = 0

# for i in ls1:
#     c = ls1.count(i)
#     if c >1:
#         ls1.remove(i)

# else:
#     pass
# print(ls1)

#  8 Write a Python program to check a list is empty or not

# a = list(input())
# def emty(a):
#     if len(a) ==0:
#         print("list is empty")
#     else:
#         print("list is not empty")
# emty(a)

#  9 Write a Python function that takes two lists and returns true if they have
# at least one common member.

# a = list(input())
# b = list(input())

# def function(a,b):
#     result = False
#     for i in a :
#         for j in b:
#             if i == j:
#                 result = True
#     print(result)
# function(a,b)


# 10 Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.

# def function():
#     l = list()
#     for i in range(2,30):
#         l.append(i**2)
#     print(l[:5])
#     print(l[-5:])
# function()

# 11 Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

# list1 = [1,2,3,3,3,3,4,5]
# x  = []

# def unique_list(list1):
#     for i in list1 :
#         if  i not in x:
#             x.append(i)
#     return x

# print(unique_list(list1))


# 12 Write a Python program to convert a list of characters into a string.


# list1 = ['hitesh','mahesh','ramesh']
# def converter(list1):
#  a = ",".join(list1)
#  return a
# print(converter(list1))


# 13 Write a Python program to select an item randomly from a list.

# import random
# list1 = [1,2,"hitesh","mahesh","ramesh",3,46,16,48,81,8,5]
# def function(list1):
#  print(random.choice(list1))
# function(list1)


#  14  Write a Python program to find the second smallest number in a list.


# ls = [1,2,3,4,9,8,55,225,4,45,515,5151,515,151,45,54,5,]

# def funation(ls):
#     max1 = ls.remove(max(ls))
#     max2 = max(ls)
#     return max2

# print(funation(ls))


# 15  Write a Python program to  get unique values from a list

# ls1 =  [1,2,3,3,3,3,4,5]
# unique =[]

# def function(ls1):
#     for i in ls1:
#         if i not in unique:
#             unique.append(i)
#     print(unique)
# function(ls1)

# 16  Write a Python program to check whether a list contains a sub list

# string = input("this is your string: ")
# sub = input("please enter your substring to know there is sub string present in string : ")
# count = 0

# for i in range(0,len(string)):
#     start = i
#     end = i + len(sub)
#     count = count + string.count(sub,start,end)
# if count ==0 :
#     print(True)
# else:
#     print(False)

# 17  Write a Python program to split a list into different variables.

# color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
#          ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# var1, var2, var3 = color
# print(var1)
# print(var2)
# print(var3)

# 18 What is tuple? Difference between list and tuple.

# a tuple is an ordered sequence of values. The values can be repeated, but their number is always finite.
# The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# 19 Write a Python program to create a tuple with different data types.

# tuplex = ("tuple", False, 3.2, 1)
# print(tuplex)

# 20 Write a Python program to create a tuple with numbers.

# tup = (1,2,3,4,5,5)
# print(tup)

# 20  Write a Python program to convert a tuple to a string.

# tup1 = ('1','hitesh',"agg","gsgd",'45','64')
# string1 = ''.join(tup1)
# print(string1)

# 21  Write a Python program to check whether an element exists within a
# tuple.

# a = ('1','2','3','4','3','hitesh','karen')
# b = (input())

# print(b in a)

# 22 Write a Python program to find the length of a tuple.

# a = (1,2,3,4,5,6)
# b = len(a)
# print("length of tuple :" , b)


# 23 Write a Python program to convert a list to a tuple.

# a = (1,2,3,4,5,6,7,8,9)
# b = list(a)
# print(b)

# 24 Write a Python program to reverse a tuple.

# a = (1,2,3,4,5,6,7)
# def rev(a):
#     b = a[::-1]
#     print(b)
# rev(a)


# 25 Write a Python program to replace last value of tuples in a list.

# a = (1,2,3,4,5,6,7,8,9)
# def removelast():
#  b = list(a)
#  c = b.pop(-1)

# d = tuple(b)
# return b
# print(removelast())


# 26 Write a Python program to find the repeated items of a tuple.

# a = list((1,2,3,4,5,6,6,1,3,'hitesh','hitesh'))
# x = []
# y = []

# for i in a:
#     if i not in x:
#         x.append(i)

# for n in x:
#     if a.count(n)> 1:
#         y.append(n)
# print(y)


# 27  Write a Python program to remove an empty tuple(s) from a list of tuples.

# a = [(1,2),(3,57),(3,'hitesh'),(),(4,3)]
# for i in a:

# if len(i)== 0:
#   a.remove(i)
# print(a)


# 28  Write a Python program to unzip a list of tuples into individual lists.

# l = [(1,2), (3,4), (8,9)]
# print(list(zip(*l)))

# 29  Write a Python program to convert a list of tuples into a dictionary.

# a = [(1,2),(6,57),(3,'hitesh'),(4,3)]
# b = dict(a)
# print(b)

# 30 How will you create a dictionary using tuples in python?
# use the dict() function to convert a tuple to a dictionary

# 31 Write a Python script to sort (ascending and descending) a dictionary by  value.

# dict = {"maths":30,"guj":35,"science":40}



# 32 Write a Python script to concatenate following dictionaries to create a
# new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic4)

# 33  Write a Python script to check if a given key already exists in a
# dictionary.

# dict = {"maths":30,"guj":35,"science":40}

# if "maths" in dict:
#     print("yes maths key exist in dict")
# else:
#     print("it is not exiest in dict")


# 34  How Do You Traverse Through A Dictionary Object In Python?

# dict = {"maths": 30, "guj": 35, "science": 40}
# keys = dict.keys()
# for i in keys:
#     print(i)

# 35  How Do You Check The Presence Of A Key In A Dictionary?

# dict =  {"maths": 30, "guj": 35, "science": 40}
# key = input("type your key here: ")
# def find_keys():
#     keys = dict.keys()
#     if key in keys:
#         print(key," exist in dict")
#     else:
#         print(key," does not exist in dict")
# find_keys()

# 36  Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15.

# dict = dict()
# for x in range(1,16):
#     dict[x] = x*x
# print(dict)

# 37 Write a Python program to check multiple keys exists in a dictionary

# sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}
# print(sports.keys()>={'geeksorgeeks','practice'})
# print(sports.keys()>={'practice','contribute'})

# 38  Write a Python script to merge two Python dictionaries

# sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}
# dict = {"maths": 30, "guj": 35, "science": 40}
# merge = sports.update(dict)
# print(sports)

# 39 Write a Python program to map two lists into a dictionary

# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
# ser = dict(zip(test_keys,test_values))
# print(ser)

# 40 Write a Python program to combine two dictionary adding values for
# common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}/
# d2 = {'a': 300, 'b': 200,'d':400}

# for key in d1:
#     if key in d2:
#         d1[key]= d1[key]+d2[key]
#     else:
#         pass
# print(d1)

# 41 Write a Python program to print all unique values in a dictionary.

# a = {'a':20, 'b' :20, 'c' : 20 ,'d':30,}

# b = set(a.values())
# print("this are some uniq values for a dict : ",b)

# 42 Why Do You Use the Zip () Method in Python?
# Python's zip() function creates an iterator that will aggregate elements from two or more iterables.


# 43 Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.



# 44 Write a Python program to find the highest 3 values in a dictionary





# 45  Write a Python program to combine values in python list of dictionaries.

# a,b,c= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# d = {}
# d['item1'] = a['amount'] + c['amount']
# d['item2'] = b['amount']
# print(d)

# 46 Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource'

# string = 'w3resource'

# dict = {}
# for i in string:
#     keys = dict.keys()
#     if i in keys:
#         dict[i]+= 1
#     else:
#         dict[i]= 1
# print(dict)

# 47 Write a Python function to calculate the factorial of a number (a
# nonnegative integer)

# a = int(input("find the factorial num : "))
# factorial = 1
# for i in range(1,a+1):
#     factorial = factorial * i
# print(factorial)

# 48  Write a Python function to check whether a number is in a given range

# a = int(input("find your num is in range or not: "))

# def rangefinder(a):
#     if  a in range(0,20):
#         print("your number is in the range")
#     else:
#         print("your number is not in the range")
# rangefinder(a)

# 49 Write a Python function to check whether a number is perfect or not.



#  50 Write a Python function that checks whether a passed string is
# palindrome or not

# a = input("type your word : ")

# def palindrome(a):
#     if  a == a[::-1]:
#         print("your string is palindrome")
#     else:
#         print("your string is not palindrome")
# palindrome(a)

# 51 How Many Basic Types Of Functions Are Available In Python?
# There are 2 types of basic Functions (1) Userdefind function (2) Built-in Functions
#---- User-defind function : these types of functions are defined by the user to perform any specific task
#-----Built-in Functions : These are pre-defined functions in python.


# 52 How can you pick a random item from a list or tuple?

# import random

# l = [1,2,3,4,5,6,7,8,9]

# print(random.choice(l))

# 53 How can you pick a random item from a range?

# import random

# print(random.randint(0,9))

# 54 How can you get a random number in python?
# To generate random number in Python, randint() function is used. This function is defined in random module.

# 55 How will you set the starting value in generating random numbers?

# The random number generator needs a number to start with (a seed value),
# to be able to generate a random number. By default the random number generator uses the current system time.
# Use the seed() method to customize the start number of the random number generator.

# 56  How will you randomizes the items of a list in place?
# The shuffle() method randomizes the items of a list in place.

# import random

# list = [20, 16, 10, 5]
# random.shuffle(list)
# print(list)

# 57 Write a Python program to read a random line from a file.
# import random
# def random_line(fname):
#     lines = open(fname).read().splitlines()
#     return random.choice(lines)
# print(random_line('test.txt'))

# 55 Write a Python program to convert degree to radian
# import math
# degree = int(input())
# print(math.radians(degree))

# 56 Write a Python program to calculate the area of a trapezoid

# a = int(input("base : "))
# b = int(input("base : "))
# h = int(input("height :"))

# def area(a,b,h):
#     area = ((a+b)/2)*h
#     print(area)

# area(a,b,h)

# 57 Write a Python program to calculate the area of a parallelogram

# b = int(input())
# h = int(input())
# def fuantion(b,h):
#     area = b*h
#     print(area)
# fuantion(b,h)

# 58 Write a Python program to calculate surface volume and area of a
# cylinder
# import math
# r = int(input("radius : "))
# h = int(input("hight : "))

# voume_of_cylinder = math.pi*math.pow(r,2)*h
# area = 2*math.pi*r*(h + r)

# print("volume of cylinder : ",voume_of_cylinder)
# print("area",area)

# 59 Write a Python program to returns sum of all divisors of a number
# num = int(input())
# def sumdiv(num):
#     d = [1]
#     for i in range(2,num):
#         if num % i== 0:
#             d.append(i)
#     return sum(d)
# print(sumdiv(num))



# 60 Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.

# dec = input("").split(",")
# print("Maximum: ", max(dec))
# print("Minimum: ", min(dec))