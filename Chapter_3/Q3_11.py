from operator import """①"""

students = [
    ("Alice", 165, 49.52),
    ("Bob", 172, 63.12),
    ("Charlie", 185, 77.42),
    ("Dave", 169, 70.03),
    ("Eve", 165, 55.78),
]

students_sorted = sorted(students, key="""①"""(1), reverse=True)
