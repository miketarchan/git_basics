import random

class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    
    def __init__(self, sex, age) -> None:
        self.sex = sex
        self.age = age

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(sex={self.sex!r}, age={self.age!r})'
    

class Person(Human):
    pet_list = []

    def __init__(self, name, tax_id, sex, age):
        self.name = name
        self.tax_id = tax_id
        super().__init__(sex, age)

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, tax_id={self.tax_id!r}, sex={self.sex!r}, age={self.age!r})'
    
    def own_new_pet(self, pet):
        if isinstance(pet, Pet):
            self.pet_list.append(pet)
        else:
            raise ValueError('Invalid pet type. Should be instance of "Pet" class')
        
    def display_pets(self):
        for i in range(len(self.pet_list)):
            pet = self.pet_list[i]
            print(f"{pet.name} has chip with ID: {pet.chip_identity.id}")



class ChipIdentity:

    def __init__(self) -> None:
        self.__id = random.randint(0,1000)

    @property
    def id(self):
        return self.__id
    

class Pet(Animal):
    """Abstracts an animal with an owner and name.
    """
    def __init__(self, name, chip_identity):
        """Set owner at instantiation."""
        self.name = name
        self.chip_identity = chip_identity
    
    @property
    def chip_identity(self):
        """Dummy getter for hidden method."""
        return self.__chip_identity
    
    @chip_identity.setter
    def chip_identity(self, value):
    
        # do some checks here
        if isinstance(value, ChipIdentity):
            self.__chip_identity = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of ChipIdentity.'
            raise ValueError(err)
    
    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(chip_odentity={self.__chip_identity!r})'


if __name__ == '__main__':
    pass

petOne = Pet('Мурзік', ChipIdentity())
petOne = Pet('Мурзік', ChipIdentity())
person = Person("mike", 223345, 'male', 32)
person.own_new_pet(Pet('Мурзік', ChipIdentity()))
person.own_new_pet(Pet('Дог', ChipIdentity()))
person.display_pets()