# 1  What is List ? how to revers a list
# A list in Python is used to store the sequence of various types of data.
# A list can be defined as a collection of values or items of different types.
import random

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

# guess number
# import  random
# num = random.randint(1,20)
# while True:
#     guess = int(input("guess the number between 1 to 20"))
#     if guess == num:
#         print("guess success")
#     else:
#         print("your guess is wrong")

