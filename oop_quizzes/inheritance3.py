class Animal:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Using the Dog class
dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
