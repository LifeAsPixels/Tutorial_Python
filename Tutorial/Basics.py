from Tutorial.Console_Utility import Console_Utility as cu
import json
import csv
from functools import reduce

class Tutorial:
    """These are lego-brick-like notes meant to be read inline and compared in console for learning purposes."""
    
    Util = cu()

    def Syntax_Variables_Data_Types(self):
        self.Util.Header()
        
        age_input = "21" # snake case is standard in python
        student_name = "Bob Jones"
        student_age = int(age_input) # type casting
        student_gpa: float = 3.5 # type annotations are like hints -- they do not enforcing typing
        is_enrolled = True
        course_1, course_2 = "English", "Math" # multiple variable assignment
        course_1, course_2 = course_2, course_1 # they are now swapped values
        MAX_STUDENTS = 31 # all caps treats a var as a constant by convention -- not enforced

        print(f"Max students: {MAX_STUDENTS}")
        print(id(student_age)) # check memory location for advanced curiosity
        print("is_enrolled type:", type(is_enrolled)) # check the type

        print(f"Student Name:{student_name}")      # Output the student's name using an f-string
        print("Student Name:", student_name)      
        print("Student Age:", student_age)        
        print("Student GPA:", student_gpa)        
        print("Currently Enrolled:", is_enrolled) 

    def Type_Mutability(self):
        """int, float, str, bool, tuple = immutable
        list, dict, set = mutable
        methods on mutable types return values into the variable
        methods on immutable types return values, but do not save them into the variable
        mutability affects the method calls on that variable using dot notation."""

        self.Util.Header()
        student_name = "Bob Jones"
        list_a, list_b = [1,2], [1,2]

        # Example of mutability
        courses = ["English", "Math" ]
        courses1 = courses # these now point to the same object
        courses1.append("Biology") # this fuction modifies the original object adding to it
        print("courses: ")
        for course in courses:
            print(course)

        # Example of Immutability
        print(student_name.upper()) # print the value of the functions return
        print(student_name) # print the value after the function returns

        # Identity vs Equality
        print(f"List A: {list_a} List B: {list_b}")
        print( "list_a == list_b: ", list_a == list_b) # compare values of list as equal = TRUE
        print( "list_a is list_b: ", list_a is list_b) # compare object references as equal = FALSE

    def Operators(self):
        self.Util.Header()
        
        # arithmatic operators
        list_a = [1 + 1, 
                  1 - 1, 
                  2 * 3, 
                  12 / 5, # float division
                  12 // 5, # integer division
                  12 // 5, # Modulus (remainder)
                  2 ** 3, # exponentiation
                  ]
        list_b = ['addition', 'subtraction', 'multiplication', 'float division', 'integer division', 'Modulus', 'Exponents']
        index = 0
        while index < len(list_a):
            print(f"{list_b[index]}: {list_a[index]}")
            index += 1

        print('\ncomparison operators:')
        a = 5
        b = 7
        list_c = [a == b,
                  a != b,
                  a > b,
                  a < b,
                  a >= b,
                  a <= b]
        for index in list_c:
            print(index)
        print('\nAnd, Or, Not:')
        c = True
        d = False
        list_d = [c and d,
                  c or d,
                  not c]
        for index in list_d:
            print(index)

    def Control_Flow(self):
        self.Util.Header()
        # Student final score
        final_score = 78

        # Decision logic for student result
        if final_score >= 90:
            print("Excellent! Honor Roll.")
        elif final_score >= 60:
            print("Pass. Good job!")
        else:
            print("Fail. Retake required.")

    def Loops(self):
        self.Util.Header()
        
        index = 0
        while index < 10:
            print("Number:", index)
            index += 1

        # List of student names
        students = ["Alice", "Brian", "Carmen", "David"]

        print('''Print each student's name''')
        for student in students:
            print("Student:", student)

        var = 5
        print('for index in range({var}):...')
        for index in range(var):
            print("Number:", index)

        print('Zip two or more lists together and unpackage them.')
        names = ["Alice", "Brian", "Carmen", "David"]
        attendance = [92, 68, 88, 74]

        for name, score in zip(names, attendance):
            if score < 75:
                print(name, "has low attendance:", score,'%')

        # Break and Continue
        students = ["Alice", "Brian", "Carmen", "David"]
        search = "Carmen"

        for student in students:
            if student == search:
                print("Student found:", student)
                break # do nothing but exit the innermost loop
        
        students = ["Alice", "", "Carmen", None, "David"]

        for student in students:
            if not student:
                continue  # do nothing, but continue on to the next iteration
            print("Checking student:", student)

        search = "Eva"

        for student in students:
            if student == search:
                print("Student found:", student)
                break
        else:
            print("Student not found.")
    
    scoped_variable = 12
    
    def Functions(self, input = "Nothing. You left the input blank"):  # a default value is set to input
        self.Util.Header()

        global scoped_variable
        scoped_variable = 10 # a local variable is only accessible within the function where it is defined
        print(f'writing functions and methods is easy! the syntax is the same. You wrote, "{input}". The scoped_variable = {scoped_variable}')
    
    def Builtin_Functions(self):
        self.Util.Header()
        print(f'Common built-ins:  print(), len(), type(), sum(), max(), min()\nUtility functions: abs(), round(), sorted(), range(), input()')
    
    def Exceptions(self):
        self.Util.Header()

        try:
            score = int(input("Enter some text to make this throw a ValueError: "))  # Could fail if input is not a number
            print("Score entered:", score)
        except ValueError: # only executes on valueError
            print("Please enter a valid number.")
        
        print('Handle multiple errors differently with "try" and "except"')
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter another number (0 to force fail): "))
            result = a / b
            print("Result:", result)
        except ValueError:
            print("Only numbers are allowed.")
        except ZeroDivisionError:
            print("You can’t divide by zero.")
        
        print("'else' reuns if no exception occurs and 'finally' always runs")        
        try:
            f = open("grades.txt")
            content = f.read()
        except FileNotFoundError:
            print("File not found.")
        else:
            print("File contents:", content)
        finally:
            print("Operation complete.")


        score = 105  # This raises a ValueError
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100") # force certain type of error to produce under certain conditions.
        print("Grade recorded:", score)
        
    def Input_Output(self):
        self.Util.Header()

        # Basic string printing
        print("Welcome to the School Portal!")

        # Using variables
        name = "Alice"
        print("Student name:", name)

        # Multiple arguments, auto-spaced
        print("Grade:", 90, "Class:", "Math")

        # Read a name
        student_name = input("Enter the student’s name: ")

        # Read and convert score to an integer
        score = int(input("Enter the test score: "))

        # Print result
        print("Student:", student_name, "| Score:", score)

        name = "Brianna"
        grade = 88

        # Using an f-string to format the output
        print(f"{name} scored {grade} on the exam.")

    def String_Manipulation(self):
        self.Util.Header()
        
        name = "  john DOE  "

        # Remove leading/trailing spaces
        cleaned = name.strip()

        # Convert to title case
        title_cased = cleaned.title()

        # Make all lowercase or uppercase
        lowercase = title_cased.lower()
        uppercase = title_cased.upper()

        # Replace substrings
        replaced = title_cased.replace("Doe", "Smith")

        print("Original:", name)
        print("Cleaned:", title_cased)
        print("Lower:", lowercase)
        print("Upper:", uppercase)
        print("Replaced:", replaced)

        email = "student@example.edu"

        # Check if string contains "@"
        print("@" in email)  # True

        # Find the position of "@"
        at_index = email.find("@")
        print("Found '@' at index:", at_index)

        courses = "Math,Science,History"

        # Split into list
        course_list = courses.split(",")

        # Join list back to string with slashes
        joined = " / ".join(course_list)

        print("List:", course_list)
        print("Joined:", joined)

    
    def Slice(self):
        self.Util.Header()
        
        course = "CS101 - Introduction to Python"

        # First character
        print(course[0])  # "C"

        # Last 6 characters
        print(course[-6:])  # "Python"

        # Substring from index 7 to 19
        print(course[7:20])  # "Introduction"

    def Text_IO(self):
        self.Util.Header()

        # Writing to a file
        with open("students.txt", "w") as file:
            file.write("Alice - A\n")
            file.write("Bob - B\n")

        # Reading from a file
        with open("students.txt", "r") as file:
            contents = file.read()

        print("File contents:")
        print(contents)

    def JSON_IO(self):
        self.Util.Header()
        
        # Student dictionary
        students = {
            "Alice": {"grade": "A", "id": 1},
            "Bob": {"grade": "B", "id": 2}
        }

        # Write JSON to file
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        # Read JSON from file
        with open("students.json", "r") as file:
            data = json.load(file)

        print("JSON contents:")
        print(data)

    def Lists(self):
        self.Util.Header()

        # A list of student names
        students = ["Alice", "Bob", "Charlie", "Diana"]

        # Accessing items:
        print(students[0])  # Alice
        print(students[-1])  # Diana (negative index starts from the end)

        # Update the list
        students[1] = "Bobby"
        # Add new student at the end
        students.append("Eve")
        # Insert a student at index 2
        students.insert(2, "Carl")
        print(students)  # ["Alice", "Bobby", "Charlie", "Diana"]

        # Remove Items
        students.remove("Charlie")
        # Remove last item and return it
        last_student = students.pop()
        # Remove by index
        del students[0]
        print(students)


        # use slices
        first_two = students[0:2]
        print(first_two)

        # Loop through
        for student in students:
            print(student)

        # Copying a list
        students_copy = students[:]
        # or
        students_copy = students.copy()

        var = '''
Common list methods:
.append(x)	Add an item to the end
.insert(i, x)	Insert at position i
.remove(x)	Remove first occurrence of x
.pop()	Remove and return last item
.sort()	Sort the list in-place
.reverse()	Reverse the list in-place
.index(x)	Find index of first occurrence of x
.count(x)	Count occurrences of x'''
        print(var)

    def Tuples(self):
        self.Util.Header()

        # A tuple of course information
        course_info = ("Math", "MATH101", 3)  # (Course Name, Course Code, Credit Hours)

        # Access the course name
        print(course_info[0])  # Math
        # Access the credit hours
        print(course_info[2])  # 3

        # Correct single-item tuple
        one_course = ("Math",)
        # Incorrect — just a string in parentheses
        not_a_tuple = ("Math")

        # Unpacking
        name, code, credits = course_info
        print(name)    # Math
        print(code)    # MATH101
        print(credits) # 3

        # List of student names and grades
        student_grades = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
        # Loop through each tuple
        for student, grade in student_grades:
            print(f"{student} scored {grade}")

    def Dictionaries(self):
        self.Util.Header()

        # A dictionary mapping student IDs to student names
        students = {
            1001: "Alice",
            1002: "Bob",
            1003: "Charlie"
        }
        
        # Add a Value
        students[1004] = "Diana"
        # Update an existing student
        students[1001] = "Alicia"
        print(students)

        # Remove a key-value-pair
        del students[1002]
        print(students)

        # Retrieve key-value-pairs
        for student_id, name in students.items():
            print(f"ID: {student_id}, Name: {name}")

        var = '''
Common Dictionary Methods:
get(key, default)	Retrieve value safely (no crash if missing)	students.get(1005, "Unknown")
keys()	Get all keys	students.keys()
values()	Get all values	students.values()
items()	Get all (key, value) pairs	students.items()
pop(key)	Remove item and return value	students.pop(1003)
clear() Empty the dictionary	students.clear()'''

    def Sets(self):
        self.Util.Header()
        
        # Creating a set of student IDs
        student_ids = {1001, 1002, 1003, 1004}
        # Or using set() function
        empty_set = set()

        # Add a new student
        student_ids.add(1005)

        # Remove a student
        student_ids.remove(1003)  # Raises error if not found
        student_ids.discard(1006) # Safe remove: no error if not found
        print(student_ids)
        print()
        club_a = {1001, 1002, 1003}
        club_b = {1003, 1004, 1005}
        
        # Union: all students in either club
        print('Union:\n' , club_a | club_b)  # {1001, 1002, 1003, 1004, 1005}
        # Intersection: students in both clubs
        print('Intersection:\n', club_a & club_b)  # {1003}
        # Difference: students in club_a but not club_b
        print('Difference:\n', club_a - club_b)  # {1001, 1002}
        
    def List_Comprehension(self):
        self.Util.Header()

        scores = [70, 80, 60, 90, 55]
        # Keep only passing scores
        passing_scores = [score for score in scores if score >= 75]
        print(passing_scores)  # [80, 90]

        student_groups = [[1001, 1002], [1003, 1004]]
        # Flatten into one list
        flat_list = [student for group in student_groups for student in group]
        print(flat_list)  # [1001, 1002, 1003, 1004]

        def grade(score):
            return 'Pass' if score >= 60 else 'Fail'

        scores = [72, 45, 88, 59]
        results = [grade(score) for score in scores]

        print(results)  # ['Pass', 'Fail', 'Pass', 'Fail']
        
    def IO_Text(self):
        self.Util.Header()

        # Writing student names to a text file
        with open("students.txt", "w") as file:
            file.write("Alice\n")
            file.write("Bob\n")
            file.write("Charlie\n")

        # Reading from the text file
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())  # .strip() removes the newline

    def IO_CSV(self):
        self.Util.Header()

        # Writing to CSV
        with open("grades.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Grade"])
            writer.writerow(["Alice", "A"])
            writer.writerow(["Bob", "B"])

        # Reading from CSV
        with open("grades.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


    def IO_JSON(self):
        self.Util.Header()
        
        import json

        # Data as Python dictionary
        students = {
            "students": [
                {"name": "Alice", "grade": "A"},
                {"name": "Bob", "grade": "B"}
            ]
        }

        # Write JSON file
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        # Read JSON file
        with open("students.json", "r") as file:
            data = json.load(file)
            for s in data["students"]:
                print(s["name"], s["grade"])


        print("JSON contents:")
        print(data)

    def Lambdas(self):
        self.Util.Header()

        grades = [67, 82, 90, 58, 74]

        # Curve grades by adding 5 points using map and lambda
        curved = list(map(lambda g: g + 5, grades))
        print("Curved Grades:", curved)

        # Filter only passing grades (>= 70)
        passing = list(filter(lambda g: g >= 70, curved))
        print("Passing Grades:", passing)

        # Reduce to calculate total score of passing students
        total = reduce(lambda a, b: a + b, passing)
        average = total / len(passing)
        print("Average passing grades:", average)