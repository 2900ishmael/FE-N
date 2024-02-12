# Area of a rectangle - length * width

length = int(input("Enter length :"))
width = int(input("Enter width :"))

print("The area is",length * width)
area = length * width
print("The area is",area)

# Perimeter of a rectangle - (l+w)2

len = int(input("Enter length :"))
wid = int(input("Enter width :"))

perimeter = 2*(len + wid)

print("The perimeter is",perimeter)

# Create a calculator programme that allows one to enter first number,second number and operator
y = float(input("Enter first number:"))
v = float(input("Enter second number:"))
operator = input("Enter operator:")
if operator == "+":
    print("Result is",y + v)
elif operator == "-":
    print("Result is",y - v)
elif operator == "*":
    print("Result is",y * v)
elif operator == "/":
    print("Result is",y / v)
else:
    print("Invalid operator")