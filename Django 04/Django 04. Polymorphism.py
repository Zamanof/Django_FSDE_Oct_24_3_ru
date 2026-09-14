# super class
class Human:
    type = "Human"
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age if age > 0 else 0

    def get_info(self):
        return f"Name: {self.name}. Surname: {self._surname}. Age: {self.__age}"

    @staticmethod
    def get_type_static_method():
        return  Human.type

    @classmethod
    def get_type_class_method(cls):
        return cls.type

# subclass
class Student(Human):
    type = "Student"
    def __init__(self, name, surname, age, group):
        super().__init__(name, surname, age)
        self.group = group

    def get_info(self):
        return f"{super().get_info()}. Group: {self.group}"

class Foo:
    def get_info(self):
        return f"Salam"

class Bar:
    def get_info(self):
        return f"Hi"


student = Student("Nadir", "Zamanov", 45, "FSDE_Oct_24_3_ru")
human = Human("Ali", "Aliyev", 45)
# foo = Foo()
# bar = Bar()
# lst = [student, human, foo, bar]
#
# for i in lst:
#     print(i.get_info())
'''
 type = "Student"
 @staticmethod
    def get_type_static_method():
        return  Human.type
    
    @classmethod
    def get_type_class_method(cls):
        return cls.type
'''
# print(human.get_type_static_method())
# print(human.get_type_class_method())

print(student.get_type_static_method())
print(student.get_type_class_method())