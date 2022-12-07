#!/usr/bin/python

class Dog():
  
  def __init__(self,name, age):
      self.name = name
      self.age = age


  def bark(self):
      print(f"A {self.age} years puppy named {self.name.title()} is barking.\n")




# if __name__=="__main__":
#     d = Dog('Tenny',2)
#     d.bark()