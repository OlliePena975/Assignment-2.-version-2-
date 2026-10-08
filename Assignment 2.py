class Animal():
    def __init__(self, name):
        if name == "":
            raise ValueError('Name cannot be empty')
        self._name = name

    @property
    def name(self):
        return self._name

    def make_sound(self):
        print(f'{self._name} makes a generic animal sound.')

class Dog(Animal):
    def make_sound(self):
        print(f'{self._name} says Woof!')

class Cat(Animal):
    def make_sound(self):
        print(f'{self._name} says Meow!')

class Duck(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self._can_fly = can_fly

    def make_sound(self):
        print(f'{self._name} says Quack!')
        if self._can_fly == True:
            print(f'{self._name} flaps away.')

def make_animal_sound(animal):
    animal.make_sound()

if __name__ == "__main__":
    a = [Dog("Rex"), Cat("Tom"), Duck("Donald", True), Animal("Mystery")]
    for animal in a:
        make_animal_sound(animal)


class Vector():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property   
    def y(self):
        return self.__y

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __str__(self):
        return str(f'Vector({self.__x}, {self.__y})')

a = Vector(2, 5)
b = Vector(3, 1)
c = a + b
print(c)
print(a)