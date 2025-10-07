def average(a, b):
    print("The average is ", (a+b)/2)
average(4, 6)

def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average()

def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average(1, 5)

def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average(4)

def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average(b=9)

def average(a, b, c=1):
    print("The average is ", (a+b+c)/2)
average(5, 6)

def name(fname, mname = "kumar", lname = "yadav"):
    print("Hello,", fname, mname, lname)
name("sanjay")

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Sanjay","Kumar","yadav")

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average is: ", sum/len(numbers))
average(5, 6, 7, 3)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
        return sum/len(numbers)
c = average(5, 6, 7, 3)
print(c)

def name(**name):
    print(type(name))
    print("Hello,", name["fname"],name["mname"],name["lname"])
name(mname = "kumar",lname = "Yadav", fname = "Sanjay")