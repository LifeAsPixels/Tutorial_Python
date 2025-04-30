from abc import ABC, abstractmethod

class SchoolMember(ABC):

    def __init__(self, name, email):
        self.name = name            # Common attribute
        self.email = email          # Common attribute

    @abstractmethod
    def get_role(self):
        pass # must be implemented by a subclass

    @abstractmethod
    def get_details(self):
        pass

    # NOT  an abstract method
    def get_contact_info(self):
        return f"{self.name} can be reached at {self.email}"


class Student(SchoolMember):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)     # Inherit name and email from User
        self.student_id = student_id

    # different behaviors for the same methods across multiple classes is an example of ploymorphism
    def get_role(self):
        return "Student" 
    
    def get_details(self):
        return f'{self.name} (ID: {self.student_id})'
        

class Teacher(SchoolMember):
    def __init__(self, name, email, subject):
        super().__init__(name, email)     # Inherit name and email from User
        self.subject = subject

    # different behaviors for the same methods across multiple classes is an example of ploymorphism
    def get_role(self):
        return "Teacher"

    def get_details(self):
        return f"{self.name}, teaches {self.subject}"