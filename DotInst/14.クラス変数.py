# クラス

#user_name = "taguchi"
#user_score = 10

class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
        

print(User.count)
tom = User("tom") # インスタンス
bob = User("bob")
print(User.count)

print(tom.count)
