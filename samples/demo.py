class People:
    def __init__(self, dr):
        self.driver = dr


class Student(People):
    def __init__(self, dr):
        super().__init__(dr)


xiaoming = Student('bbb')

print(xiaoming.driver)