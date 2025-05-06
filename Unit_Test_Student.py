import unittest

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    

class TestStudent(unittest.TestCase):

    def test_calculate_average(self):
        # Arrange
        s = Student("John", [80, 90, 100])
        
        # Act
        avg = s.calculate_average()
        
        # Assert
        self.assertEqual(avg, 90.0)

if __name__ == '__main__':
    unittest.main()