from datetime import datetime
import StudentClass as s

student = s.student('123456', 'John Doe', datetime(2003, 4, 14), 'Junior')

student.calc_age()
student.registration()

print(f"Age: {student.get_age()}")
print(f"Registration Dates: {student.get_registration()}")