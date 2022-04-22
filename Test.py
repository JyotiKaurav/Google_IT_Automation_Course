# Program to reverse a string in python

from operator import length_hint
from tkinter import END


seq_string = 'Hello'
print(list(reversed(seq_string)))

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))

i = [1,2,3]
j = i
i[0] = 5
print(j)

i = 10
j = i
j = 3
print(i)

# Arithematic operators in Python
def Operators(i,j) :
    print(i+j)
    print(i-j)
    print(i*j)
    print(i/j)
    print(i//j)
    print(i%j)
    print(i**j)

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", 'abc')

ratio = ( 1+ (5 ** (1/2))/2)
print("ratio", ratio)
#Operators(10,4)

# To find the type of data type
print(type(2))
print(type('A'))
print(type(2.5))

# print area of rectangle

length =8
width =9
area= length*width
print("the area of rectangle is "+ str(area))

# implicit conversion
print(7+2.8)

# Total seconds
def seconds(hours, minutes, seconds):
  print((hours*3600) +(minutes*60) + seconds)

seconds(1,2,3)

# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")


def lucky_number(name):
  number = len(name) * 9
  Msg = "Hello " + name + ". Your lucky number is " + str(number)
  return(Msg)
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))


#comparator operators
def com_op():
    print(10<1)
    print(10>1)
    print(10 ==1)
    print(10 == "10")
    #print(10<'10')
com_op()

#Branching
print("***")
def is_positive(number):
  if (number > 0):
    print("True")
  END
END

print("branching")
is_positive(2)

def number_group(number):
  if (number>0):
    return "Positive"
  elif (number<0):
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#####
number = 10
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)


  ####
#Question 5
#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still 
# use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this,
#  can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes 
# needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size 
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
   # print("remainder =" + str(partial_block_remainder) + "full blocks =" + str(full_blocks))
    if partial_block_remainder > 0:
        #number of bytes
        return ((full_blocks + 1)* block_size)   
    return((full_blocks * block_size))


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


###
print((10 >= 5*2) and (10 <= 5*2))

###
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))


#####
def format_name(first_name, last_name):
	# code goes here
	
	if ((first_name == "") and (last_name != "")):
		string = ("Name: " + str(last_name))
	elif ((first_name != "") and (last_name == "")):
		string = ("Name: " + str(first_name))
	elif ((first_name !="") and (last_name !="")):
	    string = ("Name: " + str(last_name) + " " + str(first_name))
	else:
	    string = print(" ")
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

#####
10.
#Question 10
#The fractional_part function divides the numerator by the denominator, 
# and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
#Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	# keep just the fractional part of the quotient
	if (denominator==0):
		fraction = 0
		quotient = 0
	else:
		quotient = numerator/denominator
		division = numerator//denominator
		remainder = numerator%denominator
		fraction = quotient - division
	return fraction

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
#print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0