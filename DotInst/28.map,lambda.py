# map(関数, イテレータ)

def triple(n):
    return n * 3

print(list(map(triple, [1, 2, 3])))


# lambda 引数: 処理, イテレータ
print(list(map(lambda n: n * 3, [1, 2, 3])))
