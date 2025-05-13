from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Grade

# Create SQLite engine (or use PostgreSQL in next section)
engine = create_engine('sqlite:///school.db', echo=True)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add data
student = Student(name="Alice", email="alice@example.com")
course = Course(title="Biology", description="Intro to Biology")
grade = Grade(student=student, course=course, grade="A")

session.add_all([student, course, grade])
session.commit()

# Query data
students = session.query(Student).all()
for s in students:
    print(f"{s.name} - {s.email}")
