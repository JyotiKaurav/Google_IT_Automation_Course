#Fill in the gaps in the initials function so that it returns the initials of the words contained in 
# the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; 
# "local area network" should return "LAN”
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in range(len(words)):
        result += words[word][0].upper()
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

print(" ".join(["This","is","a","sentence"]))

name ="Jyoti"
number = len(name)*3
print("Hello{}, your lucky number is {}.".format(name,number))
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

#Modify the student_grade function using the format method, so that it returns 
# the phrase "X received Y% on the exam".
#  For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	return ("{} recieved {}% on the exam".format(name,grade))
    #return ("{name} recieved {grade}% on the exam".format(name=name,grade=grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#Temperature conversion
def to_celcius(x):
    return (x-32)*5/9
for x in range  (0, 101, 10):
    print("{:>3} F | {:> 6.2f} C".format(x, to_celcius(x)) )    

#name = "Jyoti is a good girl"
# print(name[4:9])

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""


#If the placeholders indicate a number, 
# they’re replaced by the variable corresponding to that order (starting at zero).

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{1} {2} {0}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""
# {:d} integer value
#print('{:d}'.format(10.5) )  #'10'

#The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be 
# equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. 
# Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for str in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if str != 0:
			new_string += str
			reverse_string = str + new_string
	# Compare the strings
	if (new_string.lower() == reverse_string.lower()):
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True




#Using the format method, fill in the gaps in the convert_distance function so that it 
# returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 
# For example, convert_distance(12) should return "12 miles equals 19.2 km".
""""
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {___} km".___
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
"""
#Fill in the gaps in the nametag function so that it uses the format method to return first_name 
# and the first initial of last_name followed by a period. 
# For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{}, {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

"""
The replace_ending function replaces the old string in a sentence with the new string, but only if the 
sentence ends with the old string. If there is more than one occurrence of the old string in the 
 sentence, only the one at the end is replaced, not all of them. 
 For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. 
 The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should
 return abcabc (no changes made).
 """
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if :
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = ___
		new_sentence = ___
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"



