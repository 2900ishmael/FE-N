# Data Type

number = 67 # int
num = 78.89 # float
greeting = "Hello World" #str
IsPythonInteresting = True #bool

# A variable storing multiple values
languages = ["Python","Java","PHP"] # list
fruits = ("banana", "apple", "orange", "watermelon") #tuple
countries = {"Kenya","United States","United Kingdom","Italy"} #
# Dictionary
details = {
    "firstname":"Brian" ,
    "age" : 17,
    "course": "MIT",
    "nationality": "USA"

}
print(number)
print(IsPythonInteresting)
print(countries)
print(details)
print(details["course"])


# Determining the data type
print(type(details))
print(type(countries))
print(type(languages))

# Typecasting - Converting one datatype to another
print(float(number))
print(int(num))

