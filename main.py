#Binary Type
a = [1,2,3,4,5,6,7,8,9,255]
b = bytes(a)
print(type(b))
print(b[1])

c = [1,2,4,4,5,6,7,8,9,255]
d = bytearray(c)
print(type(b))
d[2] = 3
print(d[2])