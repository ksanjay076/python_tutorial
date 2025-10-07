# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# for i in range(1, 11):
#     print(f"{int(a)} x {i} = {int(a)*i}")

# print("some imp lines of codes")
# print("End of program")

# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1, 11):
#      print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e:
#     print("Invalid Input")
# print("some imp lines of codes")
# print("End of program")

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("number entered is not an integer")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("number entered is not an integer")

except IndexError:
    print ("IndexError")