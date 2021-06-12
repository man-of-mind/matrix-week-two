class Animal:
    def walk(self):
        print("I can walk")


    def eat(self):
        print('I can eat')

    
class Dog(Animal):
    def bark(self):
        print('I can bark')


class Cat(Animal):
    def meow(self):
        print("I can meow")

dog = Dog()
cat = Cat()
dog.bark()
dog.walk()
cat.eat()
cat.meow()