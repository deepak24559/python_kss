#check if number is perfectly divides the others
m = eval(input("Enter The First Number: "))
n= eval(input("Enter The Second Number: "))

if m%n == 0:
    print("n is divided by m")
elif n%m==0: 
    print("n is divided by m")
else: print("neither m Is divided by n nor m is divided by m")




# to print the factorial
m = eval(input("Enter The Number For Factorial "))
factorial = 1
for i in range(1,m+1):
      factorial = factorial*i  

print("The Factorial Is", factorial)



 
# to print the sum of all numbers between m and n (both included)
m = eval(input("Enter The First Number "))
n = eval(input("Enter The Second Number "))

sum = 0
for i in range(m,n+1):
      sum = sum+i

print("The Sum Is", sum)



# to print the area and perimeter of a circle if the diameter is given
import math
diameter = eval(input("Enter The Diameter "))
Radius = diameter/2
perimeter = 2*math.pi*Radius
area = math.pi*Radius**2

print("The Perimeter Is: ",perimeter)
print("The Area Is: ",area)



# print the pattern
m = eval(input("Enter The Number: "))
for i in range(1,m+1):
    for j in range(1,i+1):
        print(j, end="")
    print()



