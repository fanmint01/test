# リスト型とタプル
# 集合型
# 辞書型

# セット <- 値の重複しない

#a = set([5, 4, 8, 5])
a = {5, 3, 8, 5}
print(a)
print(5 in a) # True
a.add(2)
a.remove(3)
print(a)
print(len(a))

a = {1, 3, 5, 8}
b = {3, 5, 8, 9}
print(a | b)
print(a & b)
print(a - b)
