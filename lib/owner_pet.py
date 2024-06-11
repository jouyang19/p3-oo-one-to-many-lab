class Pet:
    PET_TYPES = [
        'dog',
        'cat',
        'rodent',
        'bird',
        'reptile',
        'exotic'
    ]
    
    all = []
    
    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
        
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        if new_pet_type in self.PET_TYPES:
            self._pet_type = new_pet_type
        else:
            raise Exception('Pet type not accepted.')
    
    def __repr__(self) -> str:
        return f'<Pet name:{self.name} type: {self.pet_type} owner={self.owner}'

class Owner:
    
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        result = []
        for pet in Pet.all:
            if pet.owner is self:
                result.append(pet)
        return result
    
    def add_pet(self, pet):
        if pet in Pet.all:
            pet.owner = self
        else: 
            raise Exception('Invalid Pet Type!')
    
    def get_sorted_pets(self):
        pets = self.pets()
        pets.sort(key=lambda pet: pet.name)
        return pets
    
    def __repr__(self):
        return f'{self.name}'
        
        
# TESTING
owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
# owner.pets()
print("owner's pets:", owner.pets())
print("all pets", Pet.all)

o2 = Owner("Joe")
p3 = Pet("Barley", "dog", o2)
p4 = Pet("Charlie", "dog", o2)
p5 = Pet("Coco", "cat", o2)
p6 = Pet("Momo", "cat", o2)
print("owner's sorted pets", owner.get_sorted_pets())