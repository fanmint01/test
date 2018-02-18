# モジュール

#import user
from user import AdminUser, User

#bob = user.AdminUser("bob", 23)
bob = AdminUser("bob", 23)

tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()
