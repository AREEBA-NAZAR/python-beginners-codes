#fuction to add two numbers
def add(num1 , num2):
    return num1 + num2

#function to subtract two numbers
def subtract(num1 , num2):
     return num1 - num2

#function to multiply two numbers

def multiply(num1 , num2):
    return num1 * num2

#function to devide 2 numbers 

def divide(num1 , num2):
    return num1 / num2

print (" please select one option \n \
      1. add \n \
      2. subtract\n \
      3. multiply \n \
      4.divide \n ")
#take input from user
select=int(input("please select one optiopn from 1,2,3,4 :  "))
num1=int(input("enter a first number :  "))
num2=int(input("enter a second number :  "))


if select == 1:
    print("the sum of two number is : ",num1, "+", num2, "=",add(num1 , num2))
    
elif select == 2:
    print("the difference of two number is : ",num1 , "-", num2,  "=" , subtract(num1 , num2))
    
elif select == 3:
    print("the multiplication of two number is : ",num1 ," * " ,num2 ," = " ,multiply(num1 , num2))
    
elif select == 4:
    print("the division of two number is : ",num1 ," / " ,num2 ,"=" ,divide(num1 , num2))
    
else:
    print("invalid choice")


     