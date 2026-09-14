# Encapsulation

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age if age > 0 else 0

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, age):
    #     self.__age = age if age > 0 else 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age must be >= 0")
        self.__age = value


human = Human("Nadir", "Zamanov", 24)
# print(human.get_age())
# human.set_age(45)
# print(human.get_age())
print(human.age)
human.age = -25
print(human.age)
