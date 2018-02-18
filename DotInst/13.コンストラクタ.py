# クラス

#user_name = "taguchi"
#user_score = 10

class User:
    def __init__(self, name):
        self.name = name
        

tom = User("tom") # インスタンス
bob = User("bob")

print(tom.name)
print(bob.name)
