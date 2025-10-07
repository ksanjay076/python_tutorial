s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo2", "Seoul", "Kabul", "Madrid2"}
cities3 = cities.isdisjoint(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid", "Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsink")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# cities = {"Tokyo2", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

cities = {"Tokyo2", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

info = {"carlo", 19, False, 5.9, 19}
if "carlo" in info:
    print("carlo is present")
else:
    print("carlo is absent")