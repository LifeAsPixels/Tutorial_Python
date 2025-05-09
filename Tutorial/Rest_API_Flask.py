# app.py (Flask version)

from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Alice", "grade": "A"},
    {"id": 2, "name": "Bob", "grade": "B"},
]

# Route: Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Route: Get one student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
