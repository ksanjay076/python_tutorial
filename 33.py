info = {'name':'Sanjay', 'age':'26', 'eligible':'True'}
print(info)
print(info['name'])
print(info.get('name'))

info = {'name':'Sanjay', 'age':'26', 'eligible':'True'}
print(info)
# print(info['name2'])
print(info.get('name2'))

info = {'name':'Sanjay', 'age':'26', 'eligible':'True'}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])

for key in info.keys():
    print(f"The value corresponding to the key {key}{info[key]}")

print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

