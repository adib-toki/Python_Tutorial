#Add Set Item
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)


x = {"apple", "banana", "cherry"}
y = {"pineapple", "mango", "papaya"}

x.update(y)
print(x)


set1 = {1,2,3,4,5}
list1 = [6,7,8,9,0]

set1.update(list1)
print(set1)