import re

file = open("mbox-short.txt", "r")
x = file.read()
# print(x)

wzorzec = r"[d-u]{4}.r"
y = re.search(wzorzec, x)
z = y.group()
print(z)
