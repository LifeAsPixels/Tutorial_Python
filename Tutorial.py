from Tutorial import *
import time
from Tutorial.Basics import clock

# delete a variable
big_number = 9999
del big_number

@clock
def main():    
    Instance = Basics.Tutorial()
    Instance.Util.Header(title = "Python Tutorial")
    print(Instance.__doc__)

    basics = [
        Instance.Syntax_Variables_Data_Types,
        Instance.Type_Mutability,
        Instance.Operators,
        Instance.Loops,
        lambda: Instance.Functions(7),
        Instance.Builtin_Functions,
        # Instance.Exceptions(),
        Instance.Lambdas,
        Instance.Ternary_Operator,
        lambda: Instance.Recursion1(3),
    ]
    input_output = [
        # Instance.Input_Output(),
        Instance.String_Manipulation,
        Instance.Slice,
        Instance.Lists,
        Instance.Tuples,
        Instance.Dictionaries,
        Instance.Sets,
        Instance.List_Comprehension,
        Instance.IO_Text,
        Instance.IO_JSON,
        Instance.IO_CSV,
        Instance.print_func,
        lambda: Instance.read_text_line(file_path = 'example.txt'),
    ]
    def oop():
        Instance.Util.Header(title = "OOP - Class, Method, Property")
        # Create two student objects
        Instances = []
        student1 = OOP.Student("Alice", "S001") # this is a dependency injection step
        student2 = OOP.Student("Bob", "S002")
        # Enroll each student in courses
        student1.enroll_in_course("Math")
        student2.enroll_in_course("Science")
        # Display their information
        Instances.append(student1)
        Instances.append(student2)
        for inst in Instances:
            print(inst)
    def apie():
        Instance.Util.Header(title = "APIE - Abstraction, Polymorphism, Inheritence, Encapsulation")
        # Create objects from concrete classes
        alice = APIE.Student("Alice", "alice@school.com", "S001")
        mr_smith = APIE.Teacher("Mr. Smith", "smith@school.com", "Math")
        for member in [alice, mr_smith]:
            print(f'{member.get_role()}: {member.get_details()}. {member.get_contact_info()}')
    
    numpy = [
        Instance.numpy_array_generation,

    ]
    # use commenting inside this list to toggle execution of sections of main()
    groups_to_run = [
        # basics,
        # input_output,
        # oop,
        # apie,
        numpy,
    ]

    for group in groups_to_run:
        if callable(group):
            group()
        else:
            for action in group:
                action()

    Instance.Util.Header("Application Stats")

if __name__ == "__main__":
    main()