## ### While loop
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(2)

##### 
print("Infinite loop")

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n=n+1
	

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)  

####Question 2 Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. 
# A prime factor is a number that is prime and divides another without a remainder.
print("Prime Factor")
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor = factor +1 
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

#Question 3 The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.
#Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  if (n==0):
    return False
  else:
    while n % 2 == 0:
      n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
      return True
    return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

###
4.
# Question 4 Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
#A divisor is a number that divides into another without a remainder.
print("sum of divisors")
def sum_divisors(n):
  sum = 0
  #divisor=1
  for i in range(1, n):
    if n % i == 0:
        sum += i
  return sum
  


print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

###5.
# Question 5 The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
#  An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
#Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier  
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

#Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). 
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

#In math, the factorial of a number is defined as the product of an integer and all the integers below it. 
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. 
# Fill in the blanks to make the factorial function return the right number.


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

###
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " VS " + away_team)


# Greet Friends
# friends(['Soumya', 'Ram', 'Rajni', 'Sweety'])
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


greet_friends(['Soumya', 'Ram', 'Rajni', 'Sweety'])
greet_friends("Manan")

#The validate_users function is used by the system to check if a list of users is valid or invalid. 
# A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] 
# are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

def is_valid(user):
   if len(user) >3:
       return True
def validate_users(users):
  for user in users:
    if is_valid(user):                # used in Django
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat", "tom", "Rani"])

#Question 2
# Fill in the blanks to make the factorial function return the factorial of n.
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer and all integers before it.
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,n+1):
       result = result * x
    return result

for n in range(0,10):
    if n==0:
        print(n, str(0))
    else:
        print(n, factorial(n))

#Question 4
#Write a script that prints the multiples of 7 between 0 and 100.
#Print one multiple per line and avoid printing any numbers that aren't multiples of 7.
# Remember that 0 is also a multiple of 7.

for x in range(100):
    if ((x % 7) == 0):
        print(x)

#The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts. 
# Currently the code will keep executing the function even if it succeeds. 
# Fill in the blank so the code stops trying after the operation succeeded.

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

#retry(create_user, 3)
#retry(stop_service, 5)

#The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.
#  Fill in the gaps to make this work:
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return False

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


print("big" > "small")
print((10 >= 5*2) and (10 <= 5*2))


#Recursion
#def recursive_function(parameters):
 #   if base_case_condition(parameters):
  #      return base_case_value
   # recursive_function(modified_parameters)

#The count_users function recursively counts the amount of users that belong to a group in the company system, 
# by going through each of the members of a group and if one of them is a group, 
# recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?

# def count_users(group):
 # count = 0
 
 # for member in get_members(group):
    #count += 1
  #  if is_group(member):
  #    count += count_users(member)
  #  else:
  #    count+=1
 # return count

#print(count_users("sales")) # Should be 3
#print(count_users("engineering")) # Should be 8
#print(count_users("everyone")) # Should be 18

#Question 3
#Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
# Note: base is assumed to be a positive number. 
#Tip: for functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number==1
  result = number//base
 
  # Recursive case: keep dividing number by base.
  return is_power_of(result, base )

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
