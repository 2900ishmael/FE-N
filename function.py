# Inbuilt functions
number = max(29,7,16,37,42,2900)
print(number)

y = min(2900,1600,43,23,67,77,7)
print(y)

z = pow(2,3)
print(z)

# User-defined functions
def name():
    print("ishmael")
name() # Calling a function

def details():
    name = "ishmael"
    age = "18"
    course = "MIT"
    print(name,age,course)
details()

# Parameters/variable and arguments/value
def patient(name,gender,age,marital_status):
    print(name,gender,age,marital_status)

patient("Ishmael","Male","18","Single")
patient("Brandi","Female","21","Divorced")

def multiply(x,y):
    print(x*y)

multiply(10,20)
multiply(7,21)
multiply(2900,1600)
multiply(16,29)
multiply(12,20)
multiply(15,27)


# Assignment
def employees(full_name,age,position,salary):
    print(full_name,age,position,salary)

employees("Jordan Carter","27","CEO","$500,000.00")
employees("Christie Gariy","24","Executive Director","$450,000.00")
employees("Hillary Orina","26","Marketing Director","$350,000.00")
employees("Dudley George","23","IT ","$300,000.00")
employees("Carmen Ngina","24","Manager ","$250,000.00")
