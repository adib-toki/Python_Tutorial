#Update Tuple
a = ("Apple","Orange","Kiwi")
print(a)
print(type(a))

b = list(a)
print(b)
print(type(b))
b.append("banana")
print(b)

a = tuple(b)
print(a)