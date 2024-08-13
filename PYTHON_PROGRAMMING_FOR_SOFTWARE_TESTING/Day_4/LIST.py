# list is in order and we can change

lst = [1, "Banana", 3]
lst2 = [11, 12, 13]
for i in lst:
    print(i)
print(len(lst))

print(len(lst2))
print(lst[0:3])

lst.append("Orange")
for i in lst:
    print(i)
print(len(lst))

lst.insert(2, "Pineapple")
for i in lst:
    print(i)
print(len(lst))
lst[3] = 10
lst.reverse()
for i in lst:
    print(i)

lst3 = lst + lst2

for j in lst3:
    print(j)

sst = {10, 10}
print(len(sst))
lst.remove()
