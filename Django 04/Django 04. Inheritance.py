# super class
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age if age > 0 else 0

    def get_info(self):
        return f"Name: {self.name}. Surname: {self._surname}. Age: {self.__age}"

# subclass
class Student(Human):
    def __init__(self, name, surname, age, group):
        super().__init__(name, surname, age)
        self.group = group

    def get_info(self):
        return f"{super().get_info()}. Group: {self.group}"


student = Student("Nadir", "Zamanov", 45, "FSDE_Oct_24_3_ru")
# print(student.get_info())

# print(isinstance(student, Student))
# print(isinstance(student, Human))
# print(isinstance(student, object))