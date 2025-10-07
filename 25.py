countries = ("spain", "italy", "india", "england", "germany")
temp = list(countries)
temp.append("russia")     #add item
temp.pop(3)               #remove item
temp[2] = "finland"        #change item
countries = tuple(temp)
print(countries)

countries = ("pakistan", "Afganistan", "Bangladesh", "srilanka")
countries2 = ("Vietnam", "India", "China")
southeastasia = countries + countries2
print(southeastasia)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('count of 3 in Tuple1 is: ',res)

Tuple1 = (0, 1, 26, 31, 2, 3, 1, 3, 2)
# res = Tuple1.index(2)
res = Tuple1.index(2, 4, 8)
print('count of 2 in Tuple1 is: ',res)