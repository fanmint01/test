# クラス
# アクセス制限

class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        self.__name = name
    #インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.__name))

        

tom = User("tom")
print(tom._User__name)
#bob = User("bob")

tom.say_hi()
#bob.say_hi()



