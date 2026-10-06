class Studen:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
        
    def show(self):
        print(f"Student Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")  

my_Name = Studen("Tausif", 12, 43)
classmate = Studen("Girish", 4, 35)

my_Name.show()
classmate.show()