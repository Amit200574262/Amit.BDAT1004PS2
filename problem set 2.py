#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 
# Consider the following Python module:
# a=0
# def b():
#     global a
# a = c(a)
# def c(a):
#     return a + 2
# After importing the module into the interpreter, you execute:
# 
#  b()
# b()
# b()
# a
# ?
# What value is displayed when the last expression (a) is evaluated? Explain your answer by indicating what happens in every executed statement

# In[3]:


a = 0  

def b():
    global a  
    a = c(a)

def c(a):
    return a + 2  


# In[4]:


b()

# this will run the b function and change the value of a = 2


# In[5]:


b()

# this will again run the function b and change the value of a = 4


# In[6]:


b()

# this will once again run the function b and change the value of a = 6


# In[7]:


a

# this will print the value of a that is 6


# # Question 2
# 
# Function fileLength(), given to you, takes the name of a file as input and returns
# 
# fileLength('midterm.py')
# 
# 284
# 
# fileLength('idterm.py')
# 
# Traceback (most recent call last):
# File "<pyshell#34>", line 1, in < module >
#     
# fileLength('idterm.py')
#   
# File "/Users/me/midterm.py", line 3, in fileLength
#     infile = open(filename)
# FileNotFoundError: [Errno 2] No such file or directory:
# 'idterm.py'
# 
# 
# As shown above, if the file cannot be found by the interpreter or if it cannot be read
# as a text file, an exception will be raised. Modify function fileLength() so that a
# friendly message is printed instead:
# 
# fileLength('midterm.py')
# 358
# 
# fileLength('idterm.py')
# File idterm.py not found.
#     

# # Answer 
# 
# Just change the function filelength as 
# 
# except FileNotFoundError:
# 
# print(f"File {filename} not found.")           
# 

# # Question 3
# 
# Write a class named Marsupial that can be used as shown below:
# 
# m = Marsupial()
# m.put_in_pouch('doll')
# m.put_in_pouch('firetruck')
# m.put_in_pouch('kitten')
# m.pouch_contents()
# 
# ['doll', 'firetruck', 'kitten']
# 
# Now write  Kangaroo as a subclass of Marsupial that inherits all the Marsupial
# 
# extends the Marsupial __init__ constructor to take, as input, the coordinates x and y of the Kangaroo object,
# supports method jump that takes number values dx and dy as input and moves the kangaroo by dx units along the x-axis and by dy units along the y- axis, and
# overloads the __str__ operator so it behaves as shown below.
# rite a class named

# In[8]:


class Marsupial:
    def __init__(self):
        self.pouch = []

    def put_in_pouch(self, item):
        self.pouch.append(item)

    def pouch_contents(self):
        return self.pouch

class Kangaroo(Marsupial):
    def __init__(self, x, y):
        super().__init__()  # Call the constructor of the base class
        self.x = x
        self.y = y

    def jump(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"


# In[9]:


m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
print(m.pouch_contents())


# In[10]:


k = Kangaroo(0, 0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())


# In[11]:


k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)
print(k)


# # Question 4 
# 
# Write function collatz() that takes a positive integer x as input and prints the Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying this rule to the previous number x in the sequence:
# x={ 𝑥/2 𝑖𝑓𝑥𝑖𝑠𝑒𝑣𝑒𝑛 3𝑥 + 1 𝑖𝑓 𝑥 𝑖𝑠 𝑜𝑑𝑑
# Your function should stop when the sequence gets to number 1. Your implementation must be recursive, without any loops.
# 
# collatz(1)
# 1
# 
# collatz(10)
# 10
# 5 
# 16 
# 8 
# 4 
# 2 
# 1

# In[12]:


def collatz(x):
    print(x)
    if x == 1:
        return
    if x % 2 == 0:
        collatz(x // 2)
    else:
        collatz(3 * x + 1)


# In[13]:


collatz(1)


# In[14]:


collatz(10)


# # Question 5 
# 
# Write a recursive method binary() that takes a non-negative integer n and prints  the binary representation of integer n. 
# 
# binary(0)
# 0
# 
# binary(1)
# 1
# 
# binary(3)
# 11
# 
# binary(9)
# 1001

# In[15]:


def binary(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        binary(n // 2)
        print(n % 2)


# In[16]:


binary(0)


# In[17]:


binary(1)


# In[18]:


binary(3)


# In[19]:


binary(9)


# # Question 6
# 
# 
# in python Implement a class named HeadingParser that can be used to parse an HTML document, and retrieve and print all the headings in the document. You should implement your class as a subclass of HTMLParser, defined in Standard Library module html.parser. When fed a string containing HTML code, your class should print the headings, one per line and in the order in which they appear in the document. Each heading should be indented as follows: an h1 heading should have  indentation 0, and h2 heading should have indentation 1, etc. Test your implementation using w3c.html.
# 
# infile = open('w3c.html')
# content = infile.read()
# infile.close()
# hp = HeadingParser()
# hp.feed(content)

# In[21]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside_heading = False
        self.heading_level = 0

    def handle_starttag(self, tag, attrs):
        if tag.startswith("h") and tag[1:].isdigit():
            self.inside_heading = True
            self.heading_level = int(tag[1])

    def handle_data(self, data):
        if self.inside_heading:
            indentation = " " * self.heading_level
            print(f"{indentation}{data}")

    def handle_endtag(self, tag):
        if self.inside_heading:
            self.inside_heading = False


# # Question 7

# The url is not working i tried multiple times.

# # Question 8
# 
# 

# In[22]:


import sqlite3
con=sqlite3.connect('ClimatD.db')
cur=con.cursor()
cur.execute("CREATE TABLE WeatherTable (City text, Country text, Season text, Temperature float, Rainfall float)")


# In[23]:


cur.execute("INSERT INTO WeatherTable VALUES ('Mumbai', 'India', 'Winter', 24.8, 5.9)")
cur.execute("INSERT INTO WeatherTable VALUES ('Mumbai', 'India', 'Spring', 28.4, 16.2)")
cur.execute("INSERT INTO WeatherTable VALUES ('Mumbai', 'India', 'Summer', 27.9, 1549.4)")
cur.execute("INSERT INTO WeatherTable VALUES ('Mumbai', 'India', 'Fall', 27.6, 346.0)")
cur.execute("INSERT INTO WeatherTable VALUES ('London', 'United Kingdom', 'Winter', 4.2, 207.7)")
cur.execute("INSERT INTO WeatherTable VALUES ('London', 'United Kingdom', 'Spring', 8.3, 169.6)")
cur.execute("INSERT INTO WeatherTable VALUES ('London', 'United Kingdom', 'Summer', 15.7, 157.0)")
cur.execute("INSERT INTO WeatherTable VALUES ('London', 'United Kingdom', 'Fall', 10.4, 218.5)")
cur.execute("INSERT INTO WeatherTable VALUES ('Cairo', 'Egypt', 'Winter', 13.6, 16.5)")
cur.execute("INSERT INTO WeatherTable VALUES ('Cairo', 'Egypt', 'Spring', 20.7, 6.5)")
cur.execute("INSERT INTO WeatherTable VALUES ('Cairo', 'Egypt', 'Summer', 27.7, 0.1)")
cur.execute("INSERT INTO WeatherTable VALUES ('Cairo', 'Egypt', 'Fall', 22.2, 4.5)") 


# In[24]:


# Print all the data of the table 

cur.execute("SELECT * FROM WeatherTable")
for i in cur:
    print (i)


# In[25]:


#Q-8(a) All the temperature data.

cur.execute("SELECT Temperature FROM WeatherTable")
for i in cur:
    print (i[0])


# In[26]:


#Q-8(b) All the cities, but without repetition.

cur.execute("SELECT DISTINCT(City) FROM WeatherTable")
for i in cur:
    print (i[0])


# In[27]:


#Q-8(c) All the records for India.
cur.execute("SELECT * FROM WeatherTable WHERE Country='India'")
for i in cur:
    print (i)


# In[32]:


#Q-8(d) All the Fall records.
cur.execute("SELECT * FROM WeatherTable WHERE Season='Fall'")
for i in cur:
    print (i)


# In[28]:


#Q-8(e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
cur.execute("SELECT City,Country,Season FROM WeatherTable WHERE Rainfall>200 AND Rainfall<400")
for i in cur:
    print (i)


# In[33]:


#Q-8(f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.
cur.execute("SELECT city, country FROM WeatherTable WHERE Season='Fall' AND temperature>20 ORDER BY Temperature")
for i in cur:
    print (i)


# In[29]:


#Q-8(g) The total annual rainfall for Cairo.
cur.execute("SELECT sum(Rainfall) FROM WeatherTable WHERE City='Cairo'")
for i in cur:
    print (i)


# In[31]:


#Q-8(h) The total rainfall for each season.
cur.execute("SELECT Season, round(sum(Rainfall),2) FROM WeatherTable GROUP BY Season")
for i in cur:
    print (i)


# # Question 9

# In[34]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over',
'the', 'lazy', 'dog']


# In[35]:


# 9(A)
newlist = [x.upper() for x in words]
print(newlist)


# In[36]:


# 9(B)
newlist = [x.lower() for x in words]
print(newlist)


# In[37]:


# 9(C)
newlist = [len(x) for x in words]
print(newlist)


# In[38]:


# 9(D)
newlist = [[x.upper(),x.lower(),len(x)] for x in words]
print(newlist)


# In[39]:


# 9(E)
newlist = [x for x in words if len(x)>=4]
print(newlist)


# In[ ]:




