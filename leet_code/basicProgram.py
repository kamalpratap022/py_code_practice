# Python program to add two numbers
num1 = input("Enter 1st Number:- ")
num2 = input("Enter 2nd Number:- ")

# Adding two number
sum = int(num1) + int(num2)
str1 = num1 + num2

# Print values
print("When value is entered using USER--INPUT it is consider as STRING")
print("Sum of {0} and {1} is {2} if converted to integer".format(num1, num2, sum, str1))
print("Sum of {0} and {1} is {2} is string if not converted to string".format(num1, num2, str1))
print("                    *******End of two number Sum***********")
print("                           ***********Start of Factorial with recursive function***********")
n = 5  # input("Enter a number t find factorial value:- ")


# int(n)


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# n = input("Enter a number t find factorial value:- ")
# int(n)
print("Factorial value", n, "is ", factorial(n))
print("                    *******Factorial with recursive function***********")
print("                                                ***********Start of Factorial with loop***********")