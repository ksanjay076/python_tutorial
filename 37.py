# try:
#  l = [1, 5, 6, 7]
#  i = int(input("Enter the Index"))
#  print(l[i])
# except:
#  print("Some error occured")

# finally:
#  print("I am always executed")

def func1():
 try:
  L = [1, 5, 6, 7]
  i = int(input("Enter the Index: "))
  print(L[i])
  return 1
 except:
  print("Some error occured")
  return 0

 finally:
        print("I am always executed")
#  print("I am always executed")
x = func1()
print(x)