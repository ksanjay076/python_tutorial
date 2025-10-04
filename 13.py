# strings are immutable
a = "sanjay"
print(len(a))
print(a.upper())
print(a.lower())
x = "AbNcgHJUtf"
print(x.upper())
print(x.lower())
y = "Sanjay ,,,,,,,"
print(y.rstrip(","))
print(y.upper())
print(a.replace("sanjay","sandeep"))
print(y.split(" "))
print(a.capitalize())
b = "InTroDuCtION oF pYThon!!!!!!"
print(b.capitalize())
print(len(b))
print(len(b.center(50)))
print(b.count("InTroDuCtION oF pYThon"))
print(b.endswith("!!!!"))
c = "welcome To the home"
print(c.endswith("to",4,10))
print(c.find("to"))
print(c.find("is"))
#print(c.index("is"))

d = "WelcomeTpTheConsole"
print(d.isalnum())
d= "Welcome"
print(d.isalpha())
print(d.islower())
print(d.isprintable())
print(d.isspace())
e = "World Health Organization"
print(e.istitle())
f = "To kill a Mocking bird"
print(f.istitle())
g = "Python is a interpreted language"
print(g.startswith("Python"))
print(g.startswith("language"))
print(g.swapcase())
h = "his name is dan. Dan is an honest man"
print(h.title())