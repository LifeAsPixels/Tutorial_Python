from Tutorial.Console_Utility import Console_Utility as cu
import json
import csv
from functools import reduce
import logging
import itertools
import time
import os
import numpy as np
import pandas as pd

logging.basicConfig(level = logging.DEBUG)

cwd = 'C:\cs\code\py\Tutorial_Python'
os.chdir(cwd)

def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[{elapsed:.4f}s] {func.__name__} -> {result}")
        return result
    return clocked

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

        logging.debug(f'is_enrolled:  {is_enrolled}')
        # breakpoint()

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
    
        iterator = ['A','B','C']
        index = 0
        for item in itertools.cycle(iterator):
            print(item)
            index += 1
            if index > 12:
                break

    scoped_variable = 12

    def cycle(self):
        iterator = ['A','B','C']
        index = 0
        for item in itertools.cycle(iterator):
            print(item)
            index += 1
            if index > 12:
                break

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

        number = 1000
        flt = 2/3
        print(f'{number:,}')
        print(f'{flt:.3f}')
    
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

    def Idioms_Enumerate_Zip_Unpack(self):
        self.Util.Header()
        
        # Sample data
        student_names = ["Alice", "Bob", "Charlie"]
        grades = [85, 92, 78]
        courses = ["Math", "Science", "History"]
        student_records = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

        # 1. zip(): iterate over multiple sequences together
        print("Student Grades:")
        for name, grade in zip(student_names, grades):
            print(f"{name} scored {grade}")

        # 2. enumerate(): track index while looping
        print("\nCourse List:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")

        # 3. Unpacking tuples in a loop
        print("\nStudent Records:")
        for name, grade in student_records:
            print(f"{name} - {grade}")

    @clock
    def print_func(self):
        self.Util.Header()

        name = 'Shawn'
        print('no newline', name, end = '',)
        print('no newline')

    @clock
    def read_text_line(self, file_path):
        self.Util.Header()

        with open(file_path, "r") as file:
            for line in file:
                print(line)

        with open(file_path, 'r') as file:
            line = file.readline()
            while line:
                # Process the line
                print(line.strip())
                line = file.readline()
        
    
    @clock
    def Ternary_Operator(self):
        ''' Python's equivalent to the ternary operator found in other languages.'''
        self.Util.Header()
        age = 20
        ticket_price = 20 if int(age) >= 18 else 5

        print(f"The ticket price is ${ticket_price}")

    @clock
    def Recursion1(self, start):
        """ Count down from a number  """
        print(start)

        # call the count_down if the next
        # number is greater than 0
        next = start - 1
        if next > 0:
            self.Recursion1(next)

    @clock
    def numpy_array_generation(self):
        """
        A tutorial on just the necessary numpy to complete the google ML Crash Course content
        google ML crash course link:
        https://developers.google.com/machine-learning/crash-course/

        google numpy link:
        https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en#scrollTo=aiqqxDBINAOY
        """

        one_dimensional_array = np.array([1.1, 2.5, 3.5, 4.7, 6.0, 7.1, 8.5, 9.5])
        print("one_dimensional_array: \n", one_dimensional_array)

        two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
        print("two_dimensional_array: \n", two_dimensional_array)

        zeros_array = np.zeros(shape=(2,5))
        ones_array = np.ones(shape=(4,2))
        print("zeros_array: \n", zeros_array)
        print("ones_array: \n", ones_array)

        sequence_of_integers = np.arange(5,12)
        print("sequence_of_integers: \n", sequence_of_integers)

        random_int_50_100 = np.random.randint(low=50, high=101, size=(6,)) # high is exclusive
        print("random_int_50_100: \n", random_int_50_100)

        random_float_0_1 = np.random.random((6,))
        print("random_float_0_1: \n", random_float_0_1)

        random_float_2_3 = random_float_0_1 + 2
        print("random_float_2_3: \n", random_float_2_3)

        random_int_150_300 = random_int_50_100 * 3
        print("random_int_150_300: \n", random_int_150_300)

    @clock
    def numpy_array_pracitce(self):
        """
        A tutorial on just the necessary numpy to complete the google ML Crash Course content
        google ML crash course link:
        https://developers.google.com/machine-learning/crash-course/

        google numpy link:
        https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en#scrollTo=aiqqxDBINAOY
        """

        feature = np.arange(5, 21)
        label = 3 * feature + 4
        print("feature: \n", feature)
        print("label: \n", label)

        noise = np.random.randint(low=-2, high=3, size=feature.shape)
        label += noise
        print("noise: \n", noise)
        print("label: \n", label)

    @clock
    def pandas_google_intro(self):
        """
        A tutorial on just the necessary pandas to complete the google ML Crash Course content
        google ML crash course link:
        https://developers.google.com/machine-learning/crash-course/

        google pandas link:
        https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en#scrollTo=JEBZyMdEOngx
        """
        # section 1
        # prep the data
        my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])
        # prep the column names
        my_column_names = ['temperature', 'activity']
        # create the data with column names
        my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)
        print("my_dataframe: \n", my_dataframe)

        # add a new column to an existing df
        my_dataframe["adjusted"] = my_dataframe["activity"] + 2
        print("\n my_dataframe: \n", my_dataframe)

        # ways of retrieving specific data from df
        print("\n Rows #0, #1, and #2:")
        print(my_dataframe.head(3), '\n')

        print("\n Row #2:")
        print(my_dataframe.iloc[[2]], '\n')

        print("\n Rows #1, #2, and #3:")
        print(my_dataframe[1:4], '\n')

        print("\n Column 'temperature':")
        print(my_dataframe['temperature'])

        # section 2
        my_data = np.random.randint(low=0, high=101, size=(3, 4))
        my_column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']

        df = pd.DataFrame(data=my_data, columns=my_column_names)
        print("\n df: \n", df)
        print("\n Row #1:")
        print(df.iloc[[1]], '\n')
        df['Janet'] = df['Tahani'] + df['Jason']
        print("\n df: \n", df)
    
        # section 3 making copies

        # Create a reference by assigning my_dataframe to a new variable.
        print("\n Experiment with a reference:")
        reference_to_df = df

        # Print the starting value of a particular cell.
        print("\n   Starting value of df: %d" % df['Jason'][1])
        print("\n   Starting value of reference_to_df: %d\n" % reference_to_df['Jason'][1])

        # Modify a cell in df.
        df.at[1, 'Jason'] = df['Jason'][1] + 5
        print("\n   Updated df: %d" % df['Jason'][1])
        print("\n   Updated reference_to_df: %d\n\n" % reference_to_df['Jason'][1])

        # Create a true copy of my_dataframe
        print("\n Experiment with a true copy:")
        copy_of_my_dataframe = my_dataframe.copy()

        # Print the starting value of a particular cell.
        print("\n   Starting value of my_dataframe: %d" % my_dataframe['activity'][1])
        print("\n   Starting value of copy_of_my_dataframe: %d\n" % copy_of_my_dataframe['activity'][1])

        # Modify a cell in df.
        my_dataframe.at[1, 'activity'] = my_dataframe['activity'][1] + 3
        print("\n   Updated my_dataframe: %d" % my_dataframe['activity'][1])
        print("\n   copy_of_my_dataframe does not get updated: %d" % copy_of_my_dataframe['activity'][1])
