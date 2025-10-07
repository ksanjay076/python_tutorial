l = [2, 4, 6, 8, "Sanjay", True]
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])

print(l[-3]) #Negative index
print(l[len(l)-3]) #positive index
print(l[6-3]) #positive index
print(l[3]) #positive index

if 7 in l:
    print("Yes")
else:
    print("No")
if "jay" in "Sanjay":
    print("Yes")
print(l)
print(l[:])
print(l[1:])
print(l[1:-1])
print(l[1:len(l)-1])
print(l[1:6-1])
print(l[1:5])
print(l[1:4:2])

animals = ["cat", "dog", "bat", "mouse", "horse", "donkey", "goat", "cow"]
print(animals[1:8:2])

lst = [i for i in range(8)]
print(lst)
lst = [i*i for i in range(8)]
print(lst)
lst = [i*i for i in range(8) if i%3==0]
print(lst)

names = ["milo", "sarah", "bruno", "anastasia", "rosa"]
nameswith_o = [item for item in names if "o" in item]
print(nameswith_o)

names = ["milo", "sarah", "bruno", "anastasia", "rosa"]
nameswith_o = [item for item in names if (len(item)>4)]
print(nameswith_o)