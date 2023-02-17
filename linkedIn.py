# item is something random and a is outside
a = [1,2,3,4,5]
for item in a:
    print(item)

# appends 6 everytime called
def appendSix(list):
    list.append(6)

appendSix(a)
print(a)

# prints none
print(print('5'))

# better use upper case first letter
# they exist to help you be organized
class Dog:
    # initialization, called whenever an instance of the class dog is created
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' bark')

myDog = Dog('roger')

myDog.speak()
