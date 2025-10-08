x = 4
print(x)

def hello():
    x = 5
    print(f"The local x is {x}")
    print("Hello Sanjay")
print(f"The global x is {x}")
hello()
print(f"The global x is {x}")

x = 10   # global variable

def my_function():
    global x
    x = 4
    y = 5  # local variable
    print(y)

my_function()
print(x)