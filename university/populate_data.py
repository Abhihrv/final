from university.models import *
from courses.models import *
import requests  
import random

#Populating UserType Model
new_type = UserType(code='AD',name='admin')
new_type.save()
new_type = UserType(code='ST',name='student')
new_type.save()
new_type = UserType(code='SF',name='staff')
new_type.save()
new_type = UserType(code='TE',name='teaching')
new_type.save()

#Creating first superuser
superuser = User.objects.create_superuser('admin', 'admin@gmail.com', 'password', user_type=UserType.objects.get(code='AD'))
superuser.save()

#Populating Gender Model
new_gender = Gender(code='M',name='male')
new_gender.save()
new_gender = Gender(code='F',name='female')
new_gender.save()
new_gender = Gender(code='O',name='other')
new_gender.save()

#Populating AddressType Model
new_type = AddressType(code='C',name='current')
new_type.save()
new_type = AddressType(code='H',name='home')
new_type.save()

#Below are for two more housing types for a student dorm and apartment for a teacher
new_type = AddressType(code='D',name='dorm')
new_type.save()
new_type = AddressType(code='A',name='apartment')
new_type.save()

#Creating fixed dorm locations
address_dorm = Address(street='90 Connor St.', apt='802', city='Salt Lake City', pincode= '84113', country='US', address_type = AddressType.objects.get(code='D'), state='Utah')
address_dorm.save()
address_dorm = Address(street='120 Connor St.', apt='806', city='Salt Lake City', pincode= '84113', country='US', address_type = AddressType.objects.get(code='D'), state='Utah')
address_dorm.save()
address_dorm = Address(street='265 South 1850 East', apt='806', city='Salt Lake City', pincode= '84112', country='US', address_type = AddressType.objects.get(code='D'), state='Utah')
address_dorm.save()
address_dorm = Address(street='265 Fort Douglas Blvd.', apt='810', city='Salt Lake City', pincode= '84113', country='US', address_type = AddressType.objects.get(code='D'), state='Utah')
address_dorm.save()

#Creating designations for students
new_designation = Desgination(code='gras',name='graduate assistant')
new_designation.save()
new_designation = Desgination(code='reas',name='research assistant')
new_designation.save()
new_designation = Desgination(code='stud',name='student')
new_designation.save()

#Adding 100 students
student_addresses = Address.objects.filter(address_type=AddressType.objects.get(code='D'))
for i in range(0,100):
    user_request = requests.get('https://randomuser.me/api/') 
    data = user_request.json()['results'][0]
    new_user = User.objects.create_user(username=data['login']['username'], first_name=data['name']['first'], last_name=data['name']['last'], email=data['email'], password=data['login']['password'], user_type=UserType.objects.get(code='ST'))
    new_user.save()
    address_current = random.choice(student_addresses)
    address_home = Address(street=str(data['location']['street']['number'])+' '+data['location']['street']['name'], apt=str(random.randint(0, 1000)), city=data['location']['city'], pincode= data['location']['postcode'], country=data['location']['country'], address_type = AddressType.objects.get(code='H'), state=data['location']['state'])
    address_home.save()
    new_student = Student(user=new_user, age=random.randint(18,35), gender=Gender.objects.get(name=data['gender']), address_home=address_home, address_current=address_current, designation=Desgination.objects.get(code='stud'))
    new_student.save()

#Creating fixed teaching apartment locations
address_teaching = Address(street='2155 Red Butte Canyon Rd', apt='830', city='Salt Lake City', pincode= '84112', country='US', address_type = AddressType.objects.get(code='A'), state='Utah')
address_teaching.save()
address_teaching = Address(street='250 S Mario Capecchi Dr', apt='820', city='Salt Lake City', pincode= '84112', country='US', address_type = AddressType.objects.get(code='A'), state='Utah')
address_teaching.save()

#Creating designations for teachers
new_designation = Desgination(code='inst',name='instructor')
new_designation.save()
new_designation = Desgination(code='apro',name='assistant professor')
new_designation.save()
new_designation = Desgination(code='asop',name='associate professor')
new_designation.save()
new_designation = Desgination(code='prof',name='professor')
new_designation.save()
new_designation = Desgination(code='dean',name='dean')
new_designation.save()

#Adding 30 teaching staff
teaching_addresses = Address.objects.filter(address_type=AddressType.objects.get(code='A'))
teaching_designations = Desgination.objects.filter(code__in=['inst', 'apro', 'asop', 'prof', 'dean'])
for i in range(0,30):
    user_request = requests.get('https://randomuser.me/api/') 
    data = user_request.json()['results'][0]
    new_user = User.objects.create_user(username=data['login']['username'], first_name=data['name']['first'], last_name=data['name']['last'], email=data['email'], password=data['login']['password'], user_type=UserType.objects.get(code='TE'))
    new_user.save()
    address = random.choice(teaching_addresses)
    designation = random.choice(teaching_designations)
    new_teaching = Teaching(user=new_user, age=random.randint(25,60), gender=Gender.objects.get(name=data['gender']), address=address, designation=designation)
    new_teaching.save()

#Creating designations for other staff
new_designation = Desgination(code='laas',name='lab assistant')
new_designation.save()
new_designation = Desgination(code='invi',name='invigilator')
new_designation.save()

#Adding 15 teaching staff
staff_addresses = Address.objects.filter(address_type=AddressType.objects.get(code='A'))
staff_designations = Desgination.objects.filter(code__in=['laas', 'invi'])
for i in range(0,15):
    user_request = requests.get('https://randomuser.me/api/') 
    data = user_request.json()['results'][0]
    new_user = User.objects.create_user(username=data['login']['username'], first_name=data['name']['first'], last_name=data['name']['last'], email=data['email'], password=data['login']['password'], user_type=UserType.objects.get(code='SF'))
    new_user.save()
    address = random.choice(staff_addresses)
    designation = random.choice(staff_designations)
    new_staff = Staff(user=new_user, age=random.randint(25,60), gender=Gender.objects.get(name=data['gender']), address=address, designation=designation)
    new_staff.save()

#Adding 2 Departments
Department(code='CS', name='Computer Science').save()
Department(code='FIN', name='Finance').save()

#Adding 2 Degrees
Degree(dept=Department.objects.get(code='FIN'), code='MSF', name='Master of Science in Finance', credit_required=33).save()
Degree(dept=Department.objects.get(code='CS'), code='MSCS', name='Master of Science in Computer Science', credit_required=30).save()

#Adding Schedules
Schedule(name='MW', monday=1, wednesday=1).save()
Schedule(name='TTh', tuesday=1, thursday=1).save()
Schedule(name='WF', wednesday=1, friday=1).save()

#Adding Semesters
Semester(name='Fall', from_month=9, to_month=12, start=datetime(2022,9,1)).save()
Semester(name='Spring', from_month=1, to_month=4, start=datetime(2022,1,1)).save()
Semester(name='Summer', from_month=5, to_month=8, start=datetime(2022,5,1)).save()

#Adding Courses
#Adding Finance Courses
dept = Department.objects.get(code='FIN')                                                 
degree = Degree.objects.get(code='MSF')   
Course(dept=dept, degree=degree, code='FIN001', name='Advanced Corporate Finance', credits=3, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='FIN002', name='Investments and Portfolio Management', credits=3, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='FIN003', name='Financial Modeling', credits=3, schedule=Schedule.objects.get(name='WF'),semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='FIN004', name='Financial Application of Statistical Models', credits=1.5, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='FIN005', name='Introduction to Financial Programming', credits=3, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='FIN006', name='Financial Programming', credits=3, schedule=Schedule.objects.get(name='WF'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='FIN007', name='VBA for Excel', credits=1.5, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='FIN008', name='Finance Professional Lecture Series', credits=1.5, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='FIN009', name='Personal Finance Planning', credits=3, schedule=Schedule.objects.get(name='WF'),semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='FIN010', name='Financial Management and Decision Making in a Corporation', credits=3, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='FIN011', name='Cases in Corporate Financial Planning & Analysis', credits=3, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='FIN012', name='Intro Risk Management for Multi-Assets Investors', credits=3, schedule=Schedule.objects.get(name='WF'),semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='FIN013', name='Venture Capital', credits=1.5, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()

#Adding Finance Courses
dept = Department.objects.get(code='CS')                                                 
degree = Degree.objects.get(code='MSCS')   
Course(dept=dept, degree=degree, code='CS001', name='Data Mining', credits=3, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='CS002', name='Graduate Algorithms', credits=3, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='CS003', name='Clustering', credits=3, schedule=Schedule.objects.get(name='WF'),semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='CS004', name='Data Structures and Algorithms', credits=1.5, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='CS005', name='Computational Topology', credits=3, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='CS006', name='Artificial Intelligence', credits=3, schedule=Schedule.objects.get(name='WF'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='CS007', name='Computer Vision', credits=1.5, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='CS008', name='Natural Language Processing', credits=1.5, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='CS009', name='Motion Planning', credits=3, schedule=Schedule.objects.get(name='WF'),semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='CS010', name='Distributed Systems', credits=3, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='CS011', name='Information Extraction from Text', credits=3, schedule=Schedule.objects.get(name='TTh'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()
Course(dept=dept, degree=degree, code='CS012', name='Advanced Operating System Implementation', credits=3, schedule=Schedule.objects.get(name='WF'),semester_offered=Semester.objects.get(name='Spring', start=datetime(2022,1,1))).save()
Course(dept=dept, degree=degree, code='CS013', name='Advanced Compilers', credits=1.5, schedule=Schedule.objects.get(name='MW'), semester_offered=Semester.objects.get(name='Fall', start=datetime(2022,9,1))).save()

#Assigning courses to the teaching staff
teachers = list(Teaching.objects.all())
num_teachers = len(teachers)
fin_teachers = random.sample(teachers, int(num_teachers/2))
cs_teachers = list(filter(lambda teacher: teacher not in fin_teachers, teachers))
fin_courses = Department.objects.get(code='FIN').courses_in_dept.all()
cs_courses = Department.objects.get(code='CS').courses_in_dept.all()
[TeachingCourse(teaching=fin_teachers[i], course=fin_courses[i]).save() for i in range(0, len(fin_courses))]
[TeachingCourse(teaching=cs_teachers[i], course=cs_courses[i]).save() for i in range(0, len(fin_courses))]

#Creating various statuses
Status(code = 0, name = 'Default').save()
Status(code = 1, name = 'Applied').save()
Status(code = 2, name = 'Enrolled').save()
Status(code = 3, name = 'Completed').save()
Status(code = 4, name = 'Dropped').save()
Status(code = 5, name = 'Failed').save()

#Creating Grading criteria A+ = 4.0, A = 4.0, A- = 3.7. B+ = 3.3, B = 3.0, B- = 2.7. C+ =2.3, C = 2.0, C- = 1.7. D+ = 1.3, D = 1.0, F = 0
Grade(code = 'A+', value = 4.0).save()
Grade(code = 'A', value = 4.0).save()
Grade(code = 'A-', value = 3.7).save()
Grade(code = 'B+', value = 3.3).save()
Grade(code = 'B', value = 3.0).save()
Grade(code = 'B-', value = 2.7).save()
Grade(code = 'C+', value = 2.3).save()
Grade(code = 'C', value = 2.0).save()
Grade(code = 'C-', value = 1.7).save()
Grade(code = 'D+', value = 1.3).save()
Grade(code = 'D', value = 1.0).save()
Grade(code = 'F', value = 0).save()
Grade(code = 'Def', value = 0).save()

#Creating Current Values
Current.objects.create(currentDateTime=datetime(2022,9,1), currentSemester=Semester.objects.get(start = datetime(2022,9,1))).save()

#Find two users which are a student in the database to use them as sample students
user = User.objects.get(username = 'crazypanda429')
user.set_password('password')
user.save()

user = User.objects.get(username = 'silvermeercat348')
user.set_password('password')
user.save()

#Enrolling a student in a degree
StudentDegree(
    student = User.objects.get(username='crazypanda429').student_data.get(),
    degree = Degree.objects.get(code='MSCS'),
    credits_achieved = 0,
    status = Status.objects.get(code = 2),
    cgpa = 0.0,
    enrollment_date = datetime(2022,1,1)
).save()

StudentDegree(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    degree = Degree.objects.get(code='MSF'),
    credits_achieved = 0,
    status = Status.objects.get(code = 2),
    cgpa = 0.0,
    enrollment_date = datetime(2022,9,1)
).save()

#Enrolling a student in the spring semester
StudentSemester(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    semester = Semester.objects.get(name='Spring'),
    status = Status.objects.get(code = 2),
    sgpa = 0,
    enrollment_date = datetime(2022,1,1)
).save()

#Enrolling a student in the fall semester
StudentSemester(
    student = User.objects.get(username='crazypanda429').student_data.get(),
    semester = Semester.objects.get(name='Fall'),
    status = Status.objects.get(code = 2),
    sgpa = 0,
    enrollment_date = datetime(2022,9,1)
).save()
StudentSemester(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    semester = Semester.objects.get(name='Fall'),
    status = Status.objects.get(code = 2),
    sgpa = 0,
    enrollment_date = datetime(2022,9,1)
).save()

#Enrolling 2 Students in courses
StudentCourse(
    student = User.objects.get(username='crazypanda429').student_data.get(),
    course = Course.objects.get(code = 'CS001'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='crazypanda429').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='crazypanda429').student_data.get(),
    course = Course.objects.get(code = 'CS002'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='crazypanda429').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='crazypanda429').student_data.get(),
    course = Course.objects.get(code = 'CS003'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='crazypanda429').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='crazypanda429').student_data.get(),
    course = Course.objects.get(code = 'CS004'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='crazypanda429').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()

StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN005'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN006'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN007'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN008'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,9,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN001'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,1,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN002'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,1,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN003'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,1,1))
).save()
StudentCourse(
    student = User.objects.get(username='silvermeercat348').student_data.get(),
    course = Course.objects.get(code = 'FIN004'),
    grade = Grade.objects.get(code='Def'),
    status = Status.objects.get(code = 2),
    semester = StudentSemester.objects.get(student=User.objects.get(username='silvermeercat348').student_data.get(), enrollment_date = datetime(2022,1,1))
).save()