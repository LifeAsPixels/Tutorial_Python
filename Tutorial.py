from Tutorial import *
import time


# delete a variable
big_number = 9999
del big_number

def main():
    t0 = time.time()
    
    Instance = Basics.Tutorial()
    Instance.Util.Header(title = "Python Tutorial")
    print(Instance.__doc__)
    Instance.Syntax_Variables_Data_Types()
    Instance.Type_Mutability()
    Instance.Operators()
    Instance.Loops()
    Instance.Functions(7)
    Instance.Builtin_Functions()
    
    # Instance.Exceptions()
    # Instance.Input_Output()
    Instance.String_Manipulation()
    Instance.Slice()

    Instance.Lists()
    Instance.Tuples()
    Instance.Dictionaries()
    Instance.Sets()
    Instance.List_Comprehension()
    Instance.IO_Text()
    Instance.IO_JSON()
    Instance.IO_CSV()


    Instance.Util.Header(title = "OOP - Class, Method, Property")
    # Create two student objects
    student1 = OOP.Student("Alice", "S001") # this is a dependency injection step
    student2 = OOP.Student("Bob", "S002")

    # Enroll each student in courses
    student1.enroll_in_course("Math")
    student2.enroll_in_course("Science")

    # Display their information
    student1.display_info()
    student2.display_info()


    Instance.Util.Header(title = "APIE - Abstraction, Polymorphism, Inheritence, Encapsulation")
    # Create objects from concrete classes
    alice = APIE.Student("Alice", "alice@school.com", "S001")
    mr_smith = APIE.Teacher("Mr. Smith", "smith@school.com", "Math")

    for member in [alice, mr_smith]:
        print(f'{member.get_role()}: {member.get_details()}. {member.get_contact_info()}')
    
    
    Instance.Lambdas()

    t1 = time.time()
    Instance.Util.Header("Application Stats")
    print(f'Program took {t1-t0:.4f} seconds to execute.')
if __name__ == "__main__":
    main()