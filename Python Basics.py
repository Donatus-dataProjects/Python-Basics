#!/usr/bin/env python
# coding: utf-8

# # Variables

# In[ ]:


#variables are numbers asigned to numbers. e.g


# In[1]:


a = 10
x = 4
print(a)
print(x)


# In[2]:


x, y, z = (5, 10, 15)

print(x, y, z)


# In[3]:


x = 'Hello'
y = x
y = y.lower()

print(x)
print(y)
#if you notice 'y' changes the 'Hello' to 'hello' because of the 'y.lower'


# In[5]:


x = [1, 2, 3]
y = x
y. append(4)

print(x)
print(y)

#the append function adds letter '4' both to y and x because y equals x'


# In[ ]:





# # Basic Data Types

# In[ ]:


# the data types are 
#integers
#floats
#Booleans
#strings
#None


# In[6]:


#is a whole number and to know if is an integer, you use the 'type function'
#integer supports all the basic maths operations.
type(10)


# In[7]:


#floats are numbers with decimal values.
any number with a decimal number is a float
type(1/3)


# In[8]:


5.0 + 1


# In[9]:


#Converting float to integer.

int(6.0)


# In[10]:


#converting integer to a float.
float(6)


# In[12]:


#NAN is sometimes used as a placeholder for a missing value. 


# In[13]:


#Booleans or bools true/false values that result  from logical statements.
#the first letters are always capitalize.
20 > 10


# In[18]:


10 != 10


# In[19]:


#Note Equivalent ints and floats are considered to be equal.
40 == 40.0


# In[20]:


#using the and operator

#frr this example to be true both conditions must be true

(2 > 1) and (10 > 11)


# In[21]:


for this condition to return true one of the conditions must be true
(2 > 1) and (10 > 11)


# In[ ]:


#strings 
#tetxs surrounded by quotation marks


# In[22]:


type('30')


# In[ ]:


#the two single or  quotes is an empty string and it represent and empty value
"" or ''


# In[ ]:


#None
#used to represent  a missing value


# In[ ]:





# In[23]:


type(None)


# In[ ]:





# # Operations

# In[24]:


#addition
10 + 5 


# In[25]:


#multiplication
10 * 5


# In[27]:


#division
10 / 3


# In[29]:


#floor division whaen you divide you throw away the reminder, use double slash.

10 // 3


# In[30]:


#exponential ie to rasie a certain number to a power of any number 

10 ** 3


# In[32]:


#BODMAS 
2 + 3 * 5 ** 2


# In[34]:


#modulus divides a number and returs only the reminder.

10 % 4


# In[36]:


#the math module will return some math module from external package

import math


# In[40]:


#it takes the natural log of its argument
math.log(5)


# In[48]:


#add a second argument to specify the log base

math.log(100, 10)


# In[49]:


#exponential
math.exp(2)


# In[51]:


#square root
math.sqrt(16)


# In[52]:


#absolute value of a numvber is a base python function so you dont use math package
abs(30)


# In[53]:


math.pi


# In[ ]:


#Rounding Numbers to their nearest holdnumbers


# In[56]:


round(7346.52367)


# In[59]:


#to keep a certain amount of decimal so you can specify that by putting a comma and addind the decimal  number you want to keep
round(7346.52367, 1)


# In[60]:


#to round to the left of the number enter a negative number you want to round up to.
#so it will remove the decimall numbers and and change the last whole numbers to 'zero'
#the example here i used -2
round(7346.52367, -2)


# In[62]:


#math.floor you round down

math.floor(2.8)


# In[63]:


#ceiling round you round up
math.ceil(2.8)


# In[64]:


#calculating the number of seconds in a year
60*60*24*365


# In[ ]:





# # Control Flow 
# 

# In[ ]:


#The control statement inpython checks whether some logical expressions evaluates to true or false and then then executes a code block if the expression is true.
#There are many staements 
#if
#elif#else


# In[74]:


#if statement
x = 10
y = 5

if x > y:
    print('x  is greater than y')
    


# In[75]:


#using if and else statement
y = 25
x = 10

if x > y:
    print('x is greater than y')
else:
    print('y is greater than x')


# In[91]:


#using if, elif and else statement

z = 10

if z > y:
    print('x is greater than y')
    
elif z == y:
    print('x and y are equal')
    
else:
    print('y is greater than x')


# # Loops

# In[ ]:


#two types of loops
#for loops
#while loops


# In[92]:


#for loops are programming constructs that lets you go through each item in a sequence and then perform some operation on each of them.
#e.g of a for loop.


my_sequence = list(range(0, 101, 10))


#you start a loop with its name and then give a nick name after its name.
#numbers is the nick name I used.
#the numbers starts with 10 to 100 and 10 is the steps it skips before it gets to another number.
for numbers  in my_sequence:
    print(numbers)


# In[ ]:


#for loops  supports a few special numbers namely Break, Continue


# In[141]:


#continue e.g
#the continue statement skips all the numbers untill it gets to 50 before it starts to print the numbers in sequence.
my_sequence = list(range(0, 101, 10))

for numbas in my_sequence:
    if numbas < 50:
        continue
    print(numbas)
    
        
        

    



# In[175]:


#break will count from zero(0) till it gets to 50 and will stop
my_sequence = list(range(0, 101, 10))

for nums in my_sequence:
    if nums > 50:
        break
    print(nums)


# In[ ]:





# In[151]:


#while loop is similar to for loop but if not careful it can keep iterating till the program crashes.
#You only use while loop when you dont know how many times you ave to do something before exiting the loop.
#Yu will continue to use it until logical staement becomes true and then you stop.

#to make a while loop you start with the keyword 'while'


x = 5
iters = 0


while iters < x:
    print('print')
    iters = iters+1
    

#when iters is greater than x it will exit



# In[158]:


import numpy as np


# In[167]:


#using numply to generate 25 random numbers inform of a loop.
#It is faster than thr for loop
my_data = np.random.uniform(-1, 1, 25)

my_data = np.where(my_data < 0,
                  1,
                  my_data)
             

print(my_data)


# In[ ]:





# # Functions

# In[189]:


#Funcions are been written using control flow staement.
#FUNCTIONS
#To form a funtion in python you start witha key word 'def'  followed by the name you want to give your function.
#After that your function name you have parameters in parenthesis and specify all the arguments that the function has to take. e,g below
#with a colon

def my_function(arg1, arg2):
    return arg1 + arg2


my_function(5, 10)



# In[191]:


def many_args(*args):       #The *means many arguments
       print(type(args))    #types means typ of argument
       return(sum(args))

many_args(1, 5, 6)


# In[197]:


def my_numbers(*args):
       print(type(args))
       return(sum(args))
   
my_numbers(1, 2)


# # lambda

# In[ ]:


#lambda functions are great functions that can be reused several time


# In[199]:


lambda x, y: x + y


# In[201]:


my_func = lambda x, y: x + y

my_func(4,6)


# In[204]:


#map function with lambda

my_map = map(lambda x : x**3, [1, 2, 3, 4, 5])
for item in my_map:
    print(item)


# In[ ]:





# # List

# In[ ]:


#List sequential data type.
#you cal alter list. it holds different types of data.
#it uses a square bracket []


# In[6]:


my_list = ["python",  "class"]

print(my_list)


# In[9]:


#if you wan to split the numbers
second_list = list("python class")

print(second_list)


# In[17]:


my_list.append(5)
my_list


# In[21]:


#my_list.pop(4)
my_list


# In[32]:


#nested_list
#the list below has three list but the print statement will delete the first list from zero '0' to 3 index values and print the reminder.  

nested_list= [[1, 2, 0, 3], [4, 5, 6], [7,8, 9]]
print(nested_list[0] [3])


# In[33]:


#using a step size to slice an index

my_slice = ['Python', 'is', 'the', 'best', 'tool', 'for', 'data', 'analysis']
my_slice


# In[43]:


#it slice the list but use step size 2 to get every other item.
#so is going to take the things in index 0, 2, 4 6, ....
new_slice = my_slice[0:8:2]
new_slice


# In[ ]:


#slicing everything to a certain index
#you use the slicing notation you don't specify your start but where you want to end


# In[46]:


n_slice = my_slice[: 4]
n_slice


# In[47]:


#slicing and index from where you want to start withouth given and end point.

m_slice = my_slice[3:]

m_slice


# In[64]:


#slicing backward is done using a negative number.
# 4 is the start of the index from the back
#2 is the end point of the index from the start
#-1 means starting from the back

negative_slice = my_slice[4:2:-1]
negative_slice


# In[54]:


my_slice


# In[66]:


#the colon insine the scuare is to make a copy of the entire list.

my_slice[:]


# In[85]:


#to reverse the list an slice it backward.

reverse_list = my_slice[:: -1]
reverse_list


# In[84]:


#replacing a value in a list
my_slice[0] = 'Java'     #it changes the value of index zero'0' to 'Java'

my_slice


# In[79]:


How to Delete 
#del(my_slice[0])


# In[ ]:


#to delete the last item in the list

#lizt_slice = my_slice.pop()


# In[86]:


#to add values in a list
#my_slice.append('and data science')
#my_slice


# In[87]:


#to remove values from a list
#my_slice.remove('and data science')
#my_slice


# In[ ]:


#there is a copy package in pyton 
#import copy
#you can check that also


# In[ ]:





# # Tuples
# 

# In[ ]:


#usually starts with a parenthesis or normal bracket () #they are immutable that you cannot add or delete elements of a tuple. 
#so mainly they are used for data that you know you won't adjust.


# In[89]:


my_tuple=('apple', 'ball', 1, 0)
my_tuple


# In[90]:


my_tuple2 = ('python', 'for', 'data', 'analysis')
my_tuple2


# In[ ]:





# # Dictionary

# In[ ]:


#usually starts with curly braces '{}' #elements in a dictionary come in key to value pairs separated with a ':'
#because of this dictionaries are mutable


# In[91]:


dict={'trainer':'DON', 'student': 'fiyin', 'course':'python'}
dict


# In[92]:


#To figure out the keys of a dictionary.
dict.keys()


# In[93]:


#To figure out the values in a dictionary.
dict.values()


# In[94]:


my_dict = {'Course': 'Python', 'Instructor': 'Titus', 'Student': 'Donatus'}

my_dict.keys()


# In[95]:


my_dict.values()


# In[ ]:





# # This is how to create a list inside a dictionary.

# In[96]:


my_list = {'furniture': ['chairs', 'tables', 'doors'], 'electronics': ['television', 'radio', 'sound-box'], 'food':  ['rice', 'beans', 'eggs'], 'numbers': [10, 15, 20.5]}
my_list


# In[97]:


my_list.keys()


# In[98]:


my_list.values()


# In[99]:


my_list3 = {'school': ['bag', 'books', 'pen', 'eraiser'], 'hotel': ['food', 'drinks', 'snacks'], 'kitchen': ['rice', 'beans', 'oil']}

my_list3


# In[100]:


my_list3.keys()


# In[101]:


my_list3.values()


# In[ ]:





# # HOW TO CHANE A LIST INTO A TABLE

# In[102]:


lista=[10,20,30, 40]
listb=[1,2,3,4]
#print a table for me using these two list


# In[103]:


new_list= {'lista': [10, 20, 30,40], 'listb': [1, 2, 3, 4]}
new_list


# In[104]:


import pandas as pd


# In[105]:


newlist=pd.DataFrame(new_list)
print(newlist)


# In[106]:


students = ['Victor','Daniel', 'Peter', 'Godswill', 'Donatus', ]
course = ['Python', 'Javascript', 'Vue3', 'React', 'Dart']
grade = [80, 76, 67, 84, 75]


# In[107]:


resultsheet = {'students': ['Victor', 'Daniel', 'Peter', 'Godswill', 'Donatus', ], 'course': ['Python', 'Javascript', 'Vue3', 'React', 'Dart'], 'grade': [80, 76, 67, 84, 75] }


# In[108]:


resultsheet


# In[109]:


resultsheet=pd.DataFrame(resultsheet)
resultsheet


# In[ ]:





# In[ ]:




