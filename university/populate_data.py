from courses.models import Department
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
    new_user = User.objects.create_user(username=data['login']['username'], first_name=data['name']['first'], last_name=data['name']['last'], email=data['email'], password=data["login"]['password'], user_type=UserType.objects.get(code='ST'))
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
    new_user = User.objects.create_user(username=data['login']['username'], first_name=data['name']['first'], last_name=data['name']['last'], email=data['email'], password=data["login"]['password'], user_type=UserType.objects.get(code='TE'))
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
    new_user = User.objects.create_user(username=data['login']['username'], first_name=data['name']['first'], last_name=data['name']['last'], email=data['email'], password=data["login"]['password'], user_type=UserType.objects.get(code='SF'))
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

#Adding Semesters
Semester(name='Fall', from_month=9, to_month=12).save()
Semester(name='Spring', from_month=1, to_month=4).save()

#Adding Courses
Course(dept=Department.objects.get(code='CS'), degree=Degree.objects.get(code='MSCS'), name='Master of Science in Computer Science', credits=30).save()
