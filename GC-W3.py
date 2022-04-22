#Python Course- Day 3

#Possible options
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

votes(['yes', 'no', 'maybe'])



#Question 9 What is the value of y at the end of the following code?
for x in range(10):
    for y in range(x):
        print(y)

#Question 8 What is the value of x at the end of the following code?
for x in range(1, 10, 3):
    print(x)

#Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
print("counting the digits in a number")

def digits(n):
	count = 0
	if n == 0:
		return 1
	else:
		while (n / 10 != 0):
			count += 1
			n = n // 10 
			#print(n) 
		return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

#Question 1 Fill in the blanks of this code to print out the numbers 1 through 7.
print("print out the numbers 1 through 7")
number = 1
while number < 7:
	print(number, end=" ")
	number+=1

#The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.
print("")
print("print out each letter of a word on a separate line")
def show_letters(word):
	for x in word :
		print(x)

show_letters("Hello")       # Should print one line per letter

#Question 4
#This function prints out a multiplication table (where each number is the result of multiplying the 
# first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3)
#  will print out: 1 2 3    2 4 6       3 6 9

def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()
		
multiplication_table(1, 3)
# Should print the multiplication table shown above


#Question 5
# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. 4
# Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if stop < start:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x  -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x  += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


#Question 7 The following code raises an error when executed. What's the reason for the error?
def decade_counter(year):
	while year < 50:
		year += 1
	return year
print("Decade Counter")
decade_counter(10)


#The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, 
# up to and including the maximum that's passed into the function. 
# For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1,2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


###Strings
#Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. 
# For example, double_word("hello") should return hellohello10.
def double_word(word):
   
    return (word*2  + str(len(word*2)) )

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#Method 2
def double_word(word):
  
    new_string = word*2 
    len_str= len(new_string)
    return(new_string + str(len_str))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter
#  of the string is the same as the last letter of the string, False if they’re different. 
# Remember that you can access characters using message[0] or message[-1].
#Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
def first_and_last(message):
    if (not message or message[0] == message[-1]):
        return True
    else: # (message[0] != message[-1] ):
        return False
    #else:
     #   return True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#Substring
fruit = "Pineapple"
print(fruit[0])
print(fruit[:4])
print(fruit[4:])
print(fruit[2:6])

message = " My name is Kyoti Kaurav"
#message[12] = 'J'

new_msg = message[:12] + 'J' + message[13:]
print(new_msg)

message = "I love Coding."
print (message)
 
message = "I want to be a fantastic programmer."
print(message)

#Fill in the gaps in the initials function so that it returns the initials of the words contained in 
# the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; 
# "local area network" should return "LAN”
def initials(phrase):
    words = phrase.split()
    result = ""
    for i in range(len(words)):
        result += words[i][0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


toys = "car & doll"
print(toys.index('&'))

# Python3 program for demonstration 
# of index() method
  
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
  
# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))
  
# Will print index of '1' in sublist
# having index from 1 to 7.
print(list1.index(1, 1, 7))
  
list2 = ['cat', 'bat', 'mat', 'cat', 
         'get', 'cat', 'sat', 'pet']
  
# Will print index of 'cat' in sublist
# having index from 2 to 6
print(list2.index('cat', 2,6))
Name= "jyoti"
print(Name.capitalize())


print("Jyoti".upper())
print(Name.upper())
#counts(), endswith(), split()