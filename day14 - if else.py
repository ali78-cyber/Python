# if else conditions
a = int(input("Enter your marks"))
print("your marks is", a)

# condditinal operators
# > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), == (equal to), != (not equal to)

print(a>90) # this will check if a is greater than 90 return boolean value true or false
print(a<90) # this will check if a is less than 90 return boolean value true or false
print(a>=90)# this will check if a is greater than or equal to 90 return boolean value true or false
print(a<=90)#this will check if a is less than or equal to 90 return boolean value true or false
print(a==90)#this will check if a is equal to 90 return boolean value true or false
print(a!=90) #this will check if a is not equal to 90 return boolean value true or false

 # example of if else condition

if (a>=90):
    print("you got A grade") # the space before the print statement is called indentation and it is used to define the block of code that will be executed if the condition is true
else:
    print("sorry you are not in merit list")
    print("try again next time")

# another example of if else condition

totalfee = 1000
currentfee = int(input("Enter your current fee :"))

if (currentfee >= totalfee):
    print("you have successfully paid your fee")
else:
    print("you have not paid your fee")
    print("please pay fee as soon as possible")

# another example of if else condition

# this will give discount to those customer who get their tickets number from 1 to 100
totalentryfee = 1000
discount = 0.1
ticketnumer = int(input("Please enter your ticket number :"))
if (ticketnumer >= 1 and ticketnumer <=100):
    print("you have eligible for discount")
    print("your discount is ", totalentryfee*discount)
    print("your total entry fee is ", totalentryfee - (totalentryfee*discount))
else:
    print ("sorry your are not eligible for discount")


# same example with elif statement
totalentryfee = 1000
discount = 0.1
ticketnumer = int(input("Please enter your ticket number :"))
if (ticketnumer >= 1 and ticketnumer <=100):
    print("you have eligible for discount")
    print("your discount is ", totalentryfee*discount)
    print("your total entry fee is ", totalentryfee - (totalentryfee*discount))
elif (ticketnumer > 100 and ticketnumer <=200):
    print("you have eligible for discount")
    print("your discount is ", totalentryfee*discount/2)
    print("your total entry fee is ", totalentryfee - (totalentryfee*discount/2))
else:
    print ("sorry your are not eligible for discount")


# another example of if else elif condition

#  this will check whether the number is positive, negative or zero

num = int(input("please enter a number :"))
if (num > 0):
    print("the given number", num , "is a positive number")
elif (num == 0):
    print("the given number", num , "is zero")
elif (num < 0):
    print ("the given number", num , "is a negative number")
else:
    print("invalid input")

# this is the nested if else condition

num = int(input("please enter a number :"))
if (num<0):
    print("the given number", num , "is a negative number")
elif (num>0):
    if (num % 2 == 0 ):
        print("the given number", num , "is a positive even number")
    elif (num % 2 !=0):
        print ("the given number", num , "is a positive odd number")
else:
        print ("number is zero")
