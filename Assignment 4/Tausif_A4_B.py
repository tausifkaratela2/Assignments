class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self):
        if 0 <= self.__marks <= 100:
            return self.__marks
        else:
            print("Marks should be between 0 and 100")

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 80:
            return "A"
        elif 79 >= self.__marks >= 60:
            return "B"
        elif 59 >= self.__marks >= 40:
            return "C"
        else:
            return "Fail"


    def __str__(self):
        return f"Student: {self.name} | Marks: {self.get_marks()} Grade: {self.grade()}"

My_Name = "Tausif"


st1 = Student(My_Name, 150)
st2 = Student("Girish", 86)
st3 = Student("Abhi", 78)

print(st1)
print(st2)
print(st3)

        