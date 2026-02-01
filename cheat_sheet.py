
print("Hello World")
print("my name is Swathi" + " age is 35+ ")
n = [2 ,4 ,5 ,1,9]
for i in n:
    print(int(i))

# add 2 numbers

a=2
b=3

print("sum of numbers is", a+b)

# Day5 task

print(" Subtraction is " , b-a)
print(" multiplication is" , a*b)
print(" Division is", a/b)

# Day 6

u = input(" what is user name: ")
print(u)

#Day7

pa = 5
pb = 6
print(" sum is ", pa+pb)

# Day 8
value = input("enter int value")
print(int(value))

# Day 9
sen1 = " my sentence"
print(sen1)

# Day 10
age = 40
print(f"my age is {age}")

# Day 11
"""
Day 1 task is to print values to console i.e results
Day 2 task is take variables like string and integers and print them on to console
Day 3 task is store variables and print them
Day 4,5 task is Arithematic operations on integers
Day 6 task is from console (run time) ask for input (question) and print them on to console
Day 7 task is at run time take input and so arithematic calculations
Day 8 task is input function treat variables as string in runtime, so we can converst it by parsing int()
Day 9 task is variables can hold string and integers. testing them
Day 10 task is using f-string which means print results with customized messages expressions inside curly braces {} evaluated at runtime

"""

# Day 12 ( write a simple calculator)

a = int(input("enter your number : "))
b = int(input("enter your second number : "))

print(a+b)

# Day 13 ( Modify calculator to subtract)

print (a-b)

# Day 14 ( Modify calculator to multiply)

print(a*b)

# Day 15 ( Modify calculator to Divide)

print(a/b)

# Day 16 (Print length of a string)

str = input( "enter string to length : ")

count = 0
for chr in str:
    count = count+1

print(f"length of given string is {count}")

# Day 17 ( Check data type of variables)

data = input("enter your data to check data type : ")
check_int = 4
check_str = "deada"
print(f"data type of given output is : {type(data)}")
print(f"data type of given output is : {type(check_int)}")
print(f"data type of given output is : {type(check_str)}")

# Day 18 ( : Write program that prints profile info)

name = input(" enter your name : ")
age = input(" enter your age : ")   

print(f"your name is {name} and your age is {age}")

# Day 19 ()

gender = input("enter M of F :")    
status = input(" enter your marital status : ") 
print(f"your gender is {gender} and your marital status is {status}")

# Day 20 ( handle wrong output manually)
if int(age) < 0:
    print(" age cannot be negative")
else:
    print(f" your age is {age}")

# Day 21 (Rewrite all programs from memory)

print("Hello world")
print("name is x")
print("age is y")
a = 10
b = 20
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
name = input("what is your name")
print("welcome", name)
num1 = input("enter your first number")
num2 = input("enter your second number")
print(num1+num2)
print(int(num1)+int(num2))
var = 8
str = "hello"
print(str,var)
print(f"hello {str}{var}")


# Day 25 (Learn basic if)

a=2

if a%2 == 0:
    print(f"{a} is even")

# Day 26 ( check number positive)
# Day 27 ( check number negative)
# Day 28  ( check number is zer0)
check = int(input("enter your number"))
if check>0:
    print(f"{check} is positve")
elif check<0:
    print(f"{check} is negative")
else:
    print(f"{check} is zero")


