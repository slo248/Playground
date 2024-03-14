# from HouseBuilder import *
# from Director import *

# b = HouseBuilder()

# d = LuxuryDirector(b)
# d.make()

# print(b.getResult())

class A:
    def __init__(self):
        self.__a=[1,2,3]

    @property
    def b(self):
        return self.__a.copy()

    @b.setter    
    def b(self,new_a):
        flag=True
        for x in new_a:
            if x&1:
                flag=False
                break
        if flag:
            self.__a=new_a

obj = A()
print(obj.b)
print('After')
obj.b[2]=4
print(obj.b)


