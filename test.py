print("█████████████████████████████████████████████████")

import sys
print(sys.path)


print("─────────────────────────────────────────────────")


import argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parameter")
    return parser.parse_args()
print(parse_arguments().parameter)


print("─────────────────────────────────────────────────")


class Parent:

    def __init__(self):
        self.aaa = 1

    def to_impl(self):
        raise NotImplementedError


class Child(Parent):
    
    static_attr = 2

    def __init__(self):
        super().__init__()
        self._bbb = 3

    def impled(self, x):
        print(x * 4)

    @property
    def bbb(self):
        return self._bbb

    @bbb.setter
    def bbb(self, value):
        self._bbb = value

    @staticmethod
    def doStaticmethod(x):
        print(x * 6)

    @classmethod
    def doClassmethod(cls, x):
        print(x * 7)

    def __len__(self):
        return 0

    def __eq__(self, o):
        return isinstance(o, Child)

    def __hash__(self):
        return 1

print(Child.static_attr)
Child.doStaticmethod(2)
Child.doClassmethod(2)

child = Child()
child.impled(2)
print(child.bbb)
child.bbb = 8
print(child.bbb)


print("─────────────────────────────────────────────────")


#import pdb; pdb.set_trace()


print("─────────────────────────────────────────────────")

def meta_function(*args, **kwargs):
    print(args)
    print(kwargs)

meta_function()

meta_function(
    "value0",
    "value1"
)

meta_function(
    key0 = "value0",
    key1 = "value1"
)

lis = ["value0", "value1"]

tup = ("value0", "value1")

dic = {
    "key0": "value0",
    "key1": "value1"
}

meta_function(lis)
meta_function(*lis)

meta_function(tup)
meta_function(*tup)

meta_function(dic)
meta_function(**dic)

print("─────────────────────────────────────────────────")

def myfunc():
       
    def fun1(a):
        fun2(a)

    def fun2(a):

        print(a)

    fun1(3)


    x = 4
    def myinnerfunc():
        print(x)
    x = 5
    myinnerfunc()

myfunc()

print("─────────────────────────────────────────────────")

print("█████████████████████████████████████████████████")
