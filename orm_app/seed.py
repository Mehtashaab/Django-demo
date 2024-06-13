from faker import Faker
import random
from .models import Department, Student, StudentID

fake = Faker()

def seed_db(n=10) -> None:
    try:
        for i in range(n):
            departments_obj = Department.objects.all()
            if not departments_obj:
                print("No departments available.")
                return
            
            random_index = random.randint(0, len(departments_obj) - 1)
            department = departments_obj[random_index]
            
            student_id = f"STU-{random.randint(100, 999)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()
            
            student_id_obj = StudentID.objects.create(student_id=student_id)
            
            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )
    except Exception as e:
        print(f"An error occurred: {e}")


