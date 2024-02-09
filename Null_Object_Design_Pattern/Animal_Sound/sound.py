# Step 1: Define the Animal Interface
"""
We start by defining an interface with the method make_sound. This will be the contract that all concrete animals will follow, as well as our null object.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Base class for all animals"""
    @abstractmethod
    def make_sound(self):
        """Abstract method to make a sound"""
        pass

# Step 2: Create Concrete Animal Classes
"""
Next, we create concrete classes that implement the Animal interface, like Dog and Cat.
"""

class Dog(Animal):
    """Print the sound of a dog."""
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    """Print the sound of a dog."""
    def make_sound(self):
        return "Meow!"

# Step 3: Implement the Null Object Class
"""
Now we implement the NullAnimal class which also implements the Animal interface but provides a no-op implementation of make_sound.
"""

class NullAnimal(Animal):
    """No-op implementation: Does nothing"""
    def make_sound(self):
        return "No Sound"
    
# Step 4: Use the Null Object in a Client Code
"""
Finally, we'll use these classes in a client code, which can handle Animal objects, and demonstrate how the null object avoids the need for null checking.
"""

def animal_sound(animal: Animal):
    """
    Prints the sound made by the given animal.
    
    Args:
        animal (Animal): It specifies the type hint, indicating that the animal parameter should be of type Animal. 
        This means that when calling this function, you should pass an object of a class that inherits from or implements the Animal class/interface.
    """
    print(animal.make_sound())

# creating concrete animal objects
dog = Dog()
cat = Cat()

# Using concrete objects
animal_sound(dog)
animal_sound(cat)

# Using the null object instead of None
# This avoids an if-statement to check if animal is None
null_animal = NullAnimal()
animal_sound(null_animal)