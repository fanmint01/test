# クラス
# 関数（メソッド）

#user_name = "taguchi"
#user_score = 10

class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
    #インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))
    
    #クラスメソッド
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

        

tom = User("tom") # インスタンス
bob = User("bob")

#tom.say_hi()
#bob.say_hi()

User.show_info()


