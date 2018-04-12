import random

class MyClass:
    def __init__(self):
        self.a = 'a'

    def first(self):
        print "one"
        self.second()

    def second(self):
        print "two"

one = MyClass()
print one
one.a = 'b'
print one.a
one.a = 'b'

two = one
print two
print two.a


list = [1,2,3,4,5,6,7,8,9,10,1]
print list[:10]
print list[4:]
random.shuffle(list)
print list
random.shuffle(list)
print list

print list.count(1)
print list.index(1)

