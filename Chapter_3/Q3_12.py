from operator import """①"""


class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


students = [
    Student("Alice", 165, 49.52),
    Student("Bob", 172, 63.12),
    Student("Charlie", 185, 77.42),
    Student("Dave", 169, 70.03),
    Student("Eve", 165, 55.78),
]

students.sort(key="""①"""("""②"""), reverse="""③""")
students_sorted = sorted(students, key="""①"""("""④"""), reverse="""⑤""")
