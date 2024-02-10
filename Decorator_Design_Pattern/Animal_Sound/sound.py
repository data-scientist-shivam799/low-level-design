# Step 1: Define the Animal Interface
"""
We start by defining an interface with the method make_sound. This will be the contract that all concrete animals will follow, as well as our null object.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def make_sound(self):
        """Abstract method to make a sound."""
        pass

# Step 2: Create Concrete Animal Classes
"""
Next, we create concrete classes that implement the Animal interface, like Dog and Cat.
"""
class Dog(Animal):
    def make_sound(self):
        """Returns the sound of a dog."""
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        """
        Return the sound of the animal.
        """
        return "Meow!"
    
# Step 3: Creating base decorator class
"""
Decorator class will also implements Animal interface.
"""

class AnimalDecorator(Animal):
    """
    Initialize the class with the given animal.
    Args:
        animal (str): The type of animal.
    """
    def __init__(self, animal):
        self._animal = animal

    def make_sound(self):
        """Make the animal object associated with this instance make a sound."""
        return self._animal.make_sound()
    
# Step 4: Add on to specific decorator to base decorator class
"""
Create specific decorators that add behaviors to the original make_sound method of the Animal objects
""" 

"""A decorator that adds additional sound to the animal's sound"""
class LoudDecorator(AnimalDecorator):
    def make_sound(self):
        """
        Method to make the animal sound loud.
        Returns:
            str: The animal sound repeated twice.
        """
        return f"{self._animal.make_sound()}! {self._animal.make_sound()}!"
    
"""A decorator that adds a whispering effect to the sound"""
class WhisperDecorator(AnimalDecorator):
    def make_sound(self):
        """
        Generate a sound from the animal object associated with this instance.
        Returns:
            str: A string representing the whisper sound made by the animal.
        """
        return f"...{self._animal.make_sound().lower()}..."
    
# Step 5: Use decorator object in client code
"""
In the client code, we can now handle animals without worrying whether the sound is set up or not.
"""

# create a Dog instance
dog = Dog()
print(dog.make_sound())  # Output: Woof!

# Decorato the dog with a loud decorator
loud_dog = LoudDecorator(dog)
print(loud_dog.make_sound()) # Output: Woof! Woof!

# Decorato the dog with a whisper decorator
whisper_dog = WhisperDecorator(dog)
print(whisper_dog.make_sound()) # Output: ...woof...