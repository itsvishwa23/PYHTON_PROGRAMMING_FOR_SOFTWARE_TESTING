set = {1, 2, 3, 4}
set2 = {11, 22, 33, 44}
print(set)
for i in set:
    print(i)

set.update([20])
print(set)

set3 = set.union(set2)
print(set3)
print(len(set3))
