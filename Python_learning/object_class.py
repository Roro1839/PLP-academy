class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, and my gender is {self.gender}.")

person_instance = Person("John Doe", 30, "Male")

person_instance.introduce()

