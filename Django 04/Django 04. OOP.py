class Human:
    # name = "Nadir"
    # surname = "Zamanov"
    __count = 0
    def __init__(self, name, surname, age):
        self.name = name            # public
        self._surname = surname     # protected
        self.__age = age            # private
        Human.__count += 1

    def show_info(self):
        print(f"Name = {self.name}, Surname = {self._surname}, Age = {self.__age}")

    # def initialize(self, name, surname):
    #     self.name = name
    #     self.surname = surname


    @staticmethod
    def get_count():
        return Human.__count


    @classmethod
    def get_count_class_method(cls):
        return cls.__count


# print(Human.get_count_class_method())
# print(Human.get_count())

human = Human("Nadir", "Zamanov", 45)

human1 = Human("Salam", "Salamzade", 38)
# human.initialize("Salam", "Salamzade")
# human.show_info()
# human1.show_info()

# print(human.name)
# print(human._surname)
# print(human._Human__age)
# print(human.count)
# print(human1.count)

print(Human.get_count())

