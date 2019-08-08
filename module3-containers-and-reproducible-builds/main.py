class Dog:

    #class attr - these don't change
    species = 'mammal'

    #Instance attributes - follow the class, but can have diff values
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return "{} is {} years old". format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}". format(self.name, sound)

#child class (inheritance)
class Beagal(Dog):
    def run(self, speed):
        return "{} runs {}". format(self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}". format(self.name, speed)

#instantiate (new, unique instances)
ben = Dog('Ben', 43)
blake = Dog('Blake', 25)

print(ben.description())
print(ben.speak("woof, woof"))

mary = Beagal('Mary', 12)
print(mary.description())

print(mary.run('quickly'))

#methods - do something for the clas, about the class
#Instance - happen when class is copied, self
#Class - cls parameter, not self, points to the class when instantiated, not the instance - defined in the class and doesn't change
#Static

#Inheritance - rec chars from a parent class

#original class - parent class == class Dog