# try: 
#     raise Exception(2)
# except Exception as e: 
#     print(e.args)

# class MyEx(Exception):
#   def __init__(self, msg):
#     Exception.__init__(self, msg+msg)
#     self.args = (msg,)
 
# try:
#   raise MyEx('wrong!')
# except Exception as e:
#   print(e)

# x=5
# try:
#   x > 3
# except:
#   print("a")
# else:
#   print("b")
# finally:
#   print("c") 

# class A:
#  x = 'x'
#  def alarm(self):
#   print('a' + self.x)
 
# class B(A):
#  def alarm(self):
#   super().alarm()
 
# class C(B):
#  x = 'y'
 
# C().alarm()

# class Dog:
#  def __init__(self, breed='none'):
#   self.breed = breed
 
#  def set(self, breed='labrador'):
#   self.breed = breed
#   return self.breed
 
# puppy = Dog()
# friend = puppy
# friend.set()
# print(puppy.breed)

# longone = """Hi
# There"""
 
# print(len(longone))

# class X:
#  pass
 
# print(issubclass(X, X))

# class Art():
#  masterpiece = 'John'
#  def __init__(self):
#   self.name = 'One'
 
# print(Art().__dict__)
# class Server:
#  def __init__(self, colour):
#   self.colour = colour
#   self.name = 'Atari'
 
# myserv = Server('black')
# myserv.attr = 'extra'
# print(myserv.__dict__)

# print("\\\\")


class A:
 b = 'b'
 
def __init__(self):
 self.c = 'c'
 d = self.c
 
a = A()
# print(a.d)
# print(a.b)
print(A.__dict__)
