# 1. What is File function in python? What is keywords to create and write file.
# Python file object provides methods and attributes to access and manipulate files. Using file objects, we can read or write any files. 
# the keywod to create file is open() and for write file  file.write() 
# ex file = open("newfile.txt","w")
    #file.write(" my new file...")

# 2 Write a Python program to read an entire text file.


file = open("file.txt","w")
file.write("this is my new file" )
file.close()

file = open("file.txt","r")
print(file.read())
file.close()

# 3 Write a Python program to append text to a file and display the text.

file = open("tops1.txt","w")
file.write("this is file  input //output demo using python ")
file.close()
print("file written successfully")

file = open("tops1.txt","r")

print(file.read())
file.close

file = open("tops1.txt","a")
file.write("\nnow this file is appended")

file.close()


file= open("tops1.txt","r")
print(file.read())
file.close()

#4  Write a Python program to read first n lines of a file.

n = int(input("Enter Lines To Read : "))
file = open("text.txt","r")
for i in range(n):
    print(file.readline())

# 5 Write a Python program to read last n lines of a file.

# 6 Write a Python program to read a file line by line and store it into a list

fname = 'practice.txt'
def function(fname):
	with open(fname) as file:
		contenct_list = file.readlines()
		print(contenct_list)
function(fname)

#  7  Write a Python program to read a file line by line store it into a variable.

name = 'len.txt'

def longest_word(fname):
	with open(fname,"r") as f:
		words = f.read().spit()

	max_len = len(max(words,key = len))
	return[word for word in words if len(word)==max_len]
	print(longest_word('len.txt'))
	
# 8 Write a Python program to count the number of lines in a text file. 

fname ="practice.txt"

def count(fname):
	with open(fname,'r')as f:
		count1 = len(f.readlines())

		print(count1)
count(fname)

# 9 Write a Python program to count the frequency of words in a file.

file = open('file2.txt','w')

file.write("this is my new file .")
file.close()

file = open('file2.txt','r')
a =file.read()

dict ={}

lines = a.split()

for i in lines:
    keys = dict.keys()

    if  i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

# 10 Write a Python program to write a list to a file.

list1 = ["apple","banana","mango","cherry"]
with open('file3.txt','w') as a:
    for i in list1:
        a.write("%s\n" %i)
a.close()

with open('file3.txt',"r") as a:
    print(a.read())

# 11 Write a Python program to copy the contents of a file to another file. 

with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # write content to second file
             secondfile.write(line)

# 12 Explain Exception handling? What is an Error in Python?
# In Python, an error is a problem in a program that will stop the execution. On the other hand,
# exceptions are raised when some internal events occur which changes the normal flow of the program
# Python has many built-in exceptions which are raised when your program encounters an error (run-time error).
# You can handle these exceptions using try-except blocks

# try:
    # Your code here
# except ExceptionType:
    # Code to handle the exception


# 13 How many except statements can a try-except block have?/Name Some 
# built-in exception classes: 

# In Python, there has to be at least one except statement in a try-except block. A try statement may have more than one except clause, 
# to specify handlers for different exceptions. At most one handler will be executed

# 14 When will the else part of try-except-else be executed?

# When will the else part of try-except-else be executed? Explanation: The else part is executed when no exception occurs.

# 15 Can one block of except statements handle multiple exception? 
# yes

# 16 What happens when „1‟== 1 is executed?

# When ‘1’ == 1 is executed, it evaluates to False This is because one is a string and the other is an integer1. 
# The comparison is done using operator precedence2. The first (1,) == 1 groups like so: ((1,) == 1), so builds a tuple with a single element from the result of comparing the one-element tuple 1, to the integer 1 for equality.
#  They're not equal,  so you get the 1-tuple False, for a result.




