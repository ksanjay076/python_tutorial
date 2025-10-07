letter = "Hey my name is {} and i am from {}"
country = "Nepal"
name = "Sanjay"
print(letter.format(name, country))

letter = "Hey my name is {} and i am from {}"
country = "Nepal"
name = "Sanjay"
print(letter.format(country, name))

letter = "Hey my name is {1} and i am from {0}"
country = "Nepal"
name = "Sanjay"
print(letter.format(country, name))

print(f"Hey my name is {name} and i am from {country}")
print(f"Hey my name is {{name}} and i am from {{country}}")
txt = "For only{price:.2f} dollars!"
print(txt.format(price = 49.0999))

price = 49.0999
txt = f"For only{price:.2f} dollars!"
print(txt)
# print(txt.format(price = 49.0999))

print(f"{2 * 30}")
print(type(f"{2 * 30}"))

