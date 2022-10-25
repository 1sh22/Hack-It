#simple calculator
def add(P, Q):    
   #  add two numbers   
   return P + Q   
def subtract(P, Q):   
   # subtract two numbers   
   return P - Q   
def multiply(P, Q):   
   # multiply two numbers   
   return P * Q   
def divide(P, Q):   
   #  divide two numbers    
   return P / Q    
#user input   
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
op = input(" enter operation (a/b/c/d): ")    
    
num1 = int (input ("enter the first number: "))    
num2 = int (input (" enter the second number: "))    
    
if op== 'a':    
   print (num1, " + ", num2, " = ", add(num1, num2))    
    
elif op == 'b':    
   print (num1, " - ", num2, " = ", subtract(num1, num2))    
    
elif op == 'c':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif op == 'd':    
   print (num1, " / ", num2, " = ", divide(num1, num2))    
else:    
   print ("invalid input")    








