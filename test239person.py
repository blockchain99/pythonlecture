# _name : private which is convention (not use outside of class)
# __name  : make certain class specific 
# __name__ #define your own class

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        # __msg make specific to class Person not other class.
        self.__msg = "I like turtles"
        self.__lol = "leshajhajaj"
    # def doorman(self, guess):
    #     if guess == self._secret:
    #         ...

p = Person()
print(p.name)
print(p._secret )

# print(p.__msg ) #we won't to use like this. 
## AttributeError : 'Person' obj has no attribute '__msg'
print(dir(p))
print(p._Person__lol)
print(p._Person__msg)
