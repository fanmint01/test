# package

#import mypackage.user
#import mypackage.user as mymodule
from mypackage.user import AdminUser

#bob = mypackage.user.AdminUser("bob", 23)
#bob = mymodule.AdminUser("bob", 23)
bob = AdminUser("bob", 23)

print(bob.name)
bob.say_hi()
bob.say_hello()
