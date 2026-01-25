#Unpack Tuple
fruits = ("apple", "banana", "cherry","kiwi")

(a,b,c,d) = fruits
print(d)

(*x,) = fruits
print(x)

(*z,y) = fruits
print(z)
print(y)

(s,*f) = fruits
print(f)
print(s)