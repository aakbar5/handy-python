""" python set for custom object """

class CustomObject:
  def __init__ (self, name):
    self.name           = name

  def __str__ (self):
    return "CustomObject # %s" % (self.name)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and
            self.name == getattr(other, 'name', None))

  def __hash__(self):
    return hash(self.name)

# Set # 1
s1 = set()
s1.add(CustomObject ("obj1"))
s1.add(CustomObject ("obj2"))

print("\nset1")
for s in s1:
  print(s)

# Set # 2
s2 = set()
s2.add(CustomObject ("obj3"))
s2.add(CustomObject ("obj1"))
s2.add(CustomObject ("obj4"))

print("\nset2")
for s in s2:
  print(s)

print("\nAfter union")
su = s1.union(s2)
for s in su:
  print(s)

print("\nAfter symmetric_difference")
sd = s1.symmetric_difference(s2)
for s in sd:
  print(s)
