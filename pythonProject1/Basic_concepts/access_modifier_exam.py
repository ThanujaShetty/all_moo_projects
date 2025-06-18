class base:
    a = 10
    _b = 20
    __c = 30
    print(a,_b,__c)
    def sample(self):
        self.__c = self.a + self._b
        print(self.__c)

"""obj = base()
obj.sample()
print(obj.a)  #can be accessed b/c its public
print(obj._b)  #can be accessed b/c protected
print(obj.__c)"""
# private member can not be acccesed

#without inhertance
class child1:
    def child_method(self):
        print(base.a)
        print(base._b)
        print(base.__c)
ch = child1()
ch.child_method()