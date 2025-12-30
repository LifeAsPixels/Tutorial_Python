# Define a class called Student
class Student:
    # Constructor method that runs when a new Student is created
    def __init__(self, name, student_id):
        self.name = name              # instance variable for name
        self.student_id = student_id  # instance variable for student ID
        self.courses = []             # list to store enrolled courses

    # Method to enroll the student in a new course
    def enroll_in_course(self, course_name):
        self.courses.append(course_name)  # add course to the list
        print(f"{self.name} enrolled in {course_name}.")

    # Method to display student info
    def __str__(self):
        courses = ", ".join(self.courses)
        return f"Student: {self.name}, ID: {self.student_id}\nCourses: {courses}"
