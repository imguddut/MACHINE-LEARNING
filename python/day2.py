# checking a condition 
num = 1
if num > 0:
   print("Positive number")
elif num == 0:
    print("Its a zero")
else:
    print("negative number")
    
# Example 2 : Nested conditions
age = 25
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")

# Loop through list
# Use of For loop
fruits = ["apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i)

# use of While loop
count = 5
while 1 :
    print(count)
    if count == 1:
        break
    count = count -1
    
# Check the no. is prime or not
no = int(input("Enter no."))
if no >1:
    for i in range(2, int(no**0.5) +1):
        if no % i == 0:
            print(f"{no} is not a prime")
    else:
        print(f"{no} is prime")
else:
    print(f"{no} is not prime")
    

# Calculator
 
def add(a , b):
    return a + b

def sub(a , b):
    return a - b

def mul(a,b):
    return a+b

def div(a,b):
    if b == 0:
        print ("Undefined")
    else:
        return a/b
    
print("Enter choices")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")
choice = input("Enter No.")

num1 = float(input("Enter Num1: "))
num2 = float(input("Enter Num2: "))

if choice == "1":
    print("Result: ", add(num1, num2))
elif choice == "2":
    print("Result: ",)