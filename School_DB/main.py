from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Grade
from pathlib import Path
import inspect
import os
import rich

# 1. Get the full path of the current script
script_path = Path(__file__).resolve()
# 2. Get the parent directory
parent_dir = script_path.parent
# 3. Convert to a string with unified forward slashes
# set working directories
BASE_DIR = parent_dir.as_posix()
rich.print(BASE_DIR)
DATA_DIR = Path(os.path.join(BASE_DIR, 'data'))
# Create the /data folder if it doesn't already exist
DATA_DIR.mkdir(exist_ok=True)
rich.print(DATA_DIR)

db_path = Path(os.path.join(DATA_DIR, 'school.db')).as_posix()
rich.print(db_path)
engine_url = f"sqlite:///{db_path}"
rich.print(engine_url)

# Create SQLite engine (or use PostgreSQL in next section)
engine = create_engine(engine_url, echo=True)

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
