class Human:
    def __init__(self, name, surname, age):
        self.name = name                              # public
        self._surname = surname                       # protected
        self.__age = age if age > 0 else 0            # private

    # def __repr__(self):
    #     return f'Human({self.name}, {self._surname}, {self.__age})'

    def __str__(self):
        return f'Human({self.name}, {self._surname}, {self.__age})'

    def __add__(self, other):
        return self.name + other.name

    def __eq__(self, other):
        return self.__age == other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __int__(self):
        return self.__age






human = Human(name='Salam', surname='Salamov', age=18)
human1 = Human(name='Nadir', surname='Zamanov', age=18)

# print(human)
# print(human == human1)
# print(human > human1)
# print(human + human1)

# print(int(human))