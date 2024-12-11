# Capstone Project - CS50’s Web Programming with Python and JavaScript

## Description

This is a mock build of a generic University portal that supports:-

* Registration of students to the portal by an Admin
* Allows students to register for a degree
* This will enable students to register for a course
* Students can access their lecture videos and notes.
* Students can add a profile picture and a bio
* Students can also see other students and their profile

## Distinctiveness and Complexity

### Distinctiveness

This project satisfies the requirement of being distinct from other course projects, as it focuses on creating a university portal that facilitates academic workflows. It is neither a social network nor an e-commerce platform, and here’s why:

#### Not a Social Network:

- Unlike Project 4, this portal does not allow for user-to-user communication (e.g., messaging, commenting, or posting updates).
- The project emphasizes academic management rather than social interactions, with features like course registration, degree tracking, and access to lecture materials.

#### Not an E-Commerce Platform:

- Distinct from Project 2, this application does not list products or process transactions.
- The functionality is centered around academic registrations and course management rather than shopping or financial operations.

#### Unique Purpose:

- The primary goal is to streamline the academic experience for students, teaching staff, and administrators, offering tailored features like a course dashboard, degree progress tracking, and interactive profile management.

### Complexity

This project goes beyond the baseline requirements for course projects and demonstrates advanced complexity in several areas:

#### Backend Design with Django:

- The project employs Django to manage intricate relationships between multiple [University Models](#modelspy) and [Course Models](#modelspy-1).
- Each model is thoughtfully designed to handle complex academic workflows, ensuring data consistency and logical relationships.

#### Dynamic Frontend with JavaScript:

- JavaScript is utilized for frontend interactions, including:
  - A dynamic sidebar and responsive navigation.
  - Interactive dashboards that allow students to view and manage their academic progress.

#### Role-Based Access Control:

- The project supports three distinct user roles: `Student`, `Teaching Staff`, and `Administrator`.
- Each role has unique access rights and user interfaces tailored to their responsibilities:
  - **Students**: Can register for courses and degrees, view course materials, and edit profiles.
  - **Teaching Staff**: Limited access to view and edit personal profiles.
  - **Administrators**: Manage user registrations, enrollments, and oversee the system.

#### Mobile-Responsiveness:

- The project ensures an optimal experience across devices through responsive design principles.
- Bootstrap is integrated to achieve cross-device compatibility, and custom CSS fine-tunes the visual layout.

#### File Management:

- The portal handles media uploads for profile pictures and course materials, leveraging Django’s media management capabilities.

### Technical Features that Distinguish the Project

#### Model Relationships:

- Complex relationships between students, courses, degrees, and semesters ensure the application is academically accurate and scalable.

#### User Experience Design:

- The inclusion of interactive elements, such as modals and dynamic dashboards, enhances user engagement.
- Navigation is intuitive, and the system adapts seamlessly between mobile and desktop environments.

#### Security and Scalability:

- The use of role-based permissions ensures secure access.
- The modular design makes the application scalable for future features, such as adding multi-semester tracking or analytics dashboards.

### Summary of Compliance

This project:

- Is distinct from social networks and e-commerce sites.
- Utilizes Django extensively, including models for backend management.
- Incorporates JavaScript on the frontend for interactive elements.
- Is mobile-responsive and user-friendly, adhering to modern web design standards.

By addressing these elements, the project demonstrates a high level of distinctiveness and complexity, satisfying the course’s expectations.

## Technical Description

The website utilizes the Python Django framework as its backend to generate templates and store data. It also uses JS to render the dynamic sidebar to navigate across the site. The styling is done using CSS.

### Additional Python Libraries

* django-crispy-forms
* crispy-bootstrap4

There are two apps in the project:-

* University App
  * Used to render
    * The basic layout of the site
    * Render the profile pages
    * User Registration
    * Login page
  * All the JS used in the site is added by the University app
  * It also adds the additional styling done on the website
  * It is also used to manage all the User related models

* Courses App
  * Used to render
    * Courses Dashboard
    * Registration for a degree
    * Registration for courses
    * Degree page
  * It is used to manage all the Degree and course-related models, with relationships between Students and their semesters, courses, and degrees.

All photos are stored in the ***media*** directory.

### University App

#### Templates

1. **layout.html**
  
    * Used to render the general layout of the page including the sidebar on the desktop view and the top drawer in the mobile view.
    * Adds all the CSS styling to the pages.
    * Adds all the JS scripts to the project.
    * The project also uses external JS libraries for Bootstrap, React and Bootstrap-icons.

    ![Image](/project-screenshots/drawer-desktop.jpg)

    ![Image](/project-screenshots/drawer-mobile.jpg)

2. **register.html**
  
    * Used to render the user Registration page.
    * **Only admins with permission to add new users will see this registration page.**
    * The page uses crispy forms library to format and render the registration form. Crispy also helps indicate what fields are required.

    ![Image](/project-screenshots/user-registration.jpg)

3. **login.html**
  
    * This file renders the login page.

    ![Image](/project-screenshots/login.jpg)

4. **profile.html**
  
    * Used to render the user profile.

    ![Image](/project-screenshots/profile.jpg)

5. **editprofile.html**
  
    * Renders the Profile Edit page for a user to edit their information on the portal.

    ![Image](/project-screenshots/edit-profile.jpg)

6. **index.html**
  
    * Used to render the main page of the University Portal. This page contains a little and is kept simple.

    ![Image](/project-screenshots/index.jpg)

#### Static Files

1. **university.js**: This file contains the JS script to control the sidebar and all the navigation across the site.
2. **courses.js**: This file contains the JS script to handle the degree page and add the degree status modal.
![Image](/project-screenshots/course-js.jpg)
3. **styles.css**: Contains all the CSS required for styling the site.

#### models.py

1. **UserType**: Stores the different types of users that are support. The types are:-
    * Student
    * Teaching
    * Admin
2. **User**: The main user model which stores all types of users. It inherits the AbstractUser class defined by Django. This abstraction was done to add the user_type, photo and bio fields to the User model.
3. **Address**: A separate model that is used to store the full address. This was created separately to store all parts of the address.
4. **Student**: Model used to specify what users are Students and connect them with the Addressess.
Teaching: Model used to specify what users are in the Teaching staff and connect them with the Addressess.

#### views.py

1. **login_view**: View to allow users to login to their accounts.
2. **logout_view**: View to allow users to logout.
3. **profile**: View to fetch a user profile and render it.
4. **editprofile**: View to render the profile edit form. It also accepts the form data and edits the profile stored for each user.

#### forms.py

1. **AddressForm**: Used to render the address part of the user registration form.
2. **UserForm**: Used to render everything apart from the address section of the registration form.
3. **UserProfileForm**: Form specifically used to render on the Profile edit page.

### Courses App

#### Templates

1. course.html
    * Render a course page of a particular course. It hosts the video lectures and notes.

    ![Image](/project-screenshots/course.jpg)

2. dashboard.html
    * Render the course dashboard which shows all the courses a user is registered in.

    ![Image](/project-screenshots/dashboard.jpg)

3. degree.html
    * Render the degree page which shows the degree that the student is registered.

    ![Image](/project-screenshots/degree.jpg)

    * If you click on the degree, a modal loads up with the current status of the degree.

    ![Image](/project-screenshots/course-js.jpg)

4. registration.html
    * This file is used to render both the course registration and degree registration forms.

    ![Image](/project-screenshots/degree-registration.jpg)

    ![Image](/project-screenshots/course-registration.jpg)

#### models.py

1. **Department**: This model is used to store the various departments that a University could have. Currently it only has one relationship which is with the Course model.
2. **Degree**: Model used to store the various degree that the university offers.
3. **Semester**: Model used to track the semester that have happened in the university.
4. **Schedule**: This is used to store the days when a Course lecture will take place. Hence it is has a relationship with the Course Model.
5. **Status**: This is a model that has been created to indicate the status of a student related to a course or a degree. It has 6 different values, Failed, Dropped, Enrolled, Completed, Applied and Default.
6. **Grade**: Used to define a separate Grade Model to indicate what each grade means.
7. **Course**: This model is used to store all the courses that are offered at the University. It also is related to a degree, schedule and semester.
8. **StudentDegree**: This is model created to define a relationship between Student and Degree Models. It stores all the data that is related to a Student and their Degree.
9. **StudentSemester**: This is model created to define a relationship between Student and Semester Models. It stores all the data that is related to a Student and a particular Semester.
10. **StudentCourse**: This is model created to define a relationship between Student and Course Models. It stores all the data that is related to a Student and a particular Course.
11. **TeachingCourse**: This is model created to define a relationship between Teaching and Course Models. It stores all the data that is related to a professor and a particular Course that they teach.
12. **Current**: Basically serves as a clock for this project which defines the current state of time, what Semester is the latest one. I have not been able to use multiple semesters in this project yet but it is something that I would like to test later.
13. **CourseContent**: Stores all the content related to a Course like lecture videos and notes URLs.

#### views.py

1. **dashboard**: Renders a dashboard of courses for the students where they can see all the courses they have registered in for a particular semester.
2. **degree**: Renders the Degree page where the students can see what degree they have registered in.
3. **registerDegree**: Renders the Degree registration page where the users can register for a degree.
4. **getDegree**: This is an endpoint that provides the Degree information for any request that is made to it.
5. **course**: Render the course page which shows the contents of a particular course.
6. **registerCourse**: Allows students to register for a course.

#### forms.py

1. **DegreeForm**: Used to render a form for students to register for a degree.
2. **CourseForm**: Used to render a form for students to register for a course.

## How it works

### Adding a Student

1. Login as the admin with username ***sauron*** and password ***password***

![Image](/project-screenshots/login-as-sauron.jpg)

2. Go to Admin → User Registration

![Image](/project-screenshots/user-registration.jpg)

3. Fill out the user registration form. Make sure you select the **User Type** as **student**

![Image](/project-screenshots/gollum-registration.jpg)

4. Now go to the admin console.

![Image](/project-screenshots/admin-console.jpg)

5. Go to Student Semesters and add a Student Semester using the student you just created. Only students who are enrolled in a semester can register for courses or degrees.

![Image](/project-screenshots/student-semester.jpg)

6. Now, the newly created user will have access to add Courses and Degree.
7. Logout and Log back in using the newly created student

![Image](/project-screenshots/gollum-login.jpg)

8. If you go to the courses page right now you will get an error asking to enroll in courses first
9. Go to Admin → Degree Registration
10. Register for a Degree

![Image](/project-screenshots/degree-registration.jpg)

11. Once registered you should be redirected to the degree page.

![Image](/project-screenshots/degree.jpg)

12. Now go to Admin → Course Registration and register for multiple courses

![Image](/project-screenshots/course-registration.jpg)

13. Once courses are registered, you will start seeing courses appearing on the Courses Dashboard

![Image](/project-screenshots/gollum-courses.jpg)

14. Once courses are registered, you will start seeing courses appearing on the Courses Dashboard

![Image](/project-screenshots/gollum-single-course.jpg)

15. To Edit the student profile go to Profile → Edit Profile.
16. Choose a photo for a profile picture and add a bio! Then click save.

![Image](/project-screenshots/gollum-edit-profile.jpg)

17. Go to Profile → My Profile to see the updated profile.

![Image](/project-screenshots/gollum-profile.jpg)

### Adding a Teaching Staff

1. Login as the admin with username ***sauron*** and password ***password***.

![Image](/project-screenshots/login-as-sauron.jpg)

2. Go to Admin → User Registration

![Image](/project-screenshots/user-registration.jpg)

3. Fill out the user registration form. Make sure you select the **User Type** as **teaching**

![Image](/project-screenshots/saruman-registration.jpg)

4. Click Register.
5. Once saved, you can login as the new user and make changes. 
6. Users added as Teaching in this project only have access to the Profile section.

![Image](/project-screenshots/saruman-view.jpg)

### Adding a University Admin

1. Login as the admin with username ***sauron*** and password ***password***.

![Image](/project-screenshots/login-as-sauron.jpg)

2. Go to Admin → User Registration

![Image](/project-screenshots/user-registration.jpg)

3. Fill out the user registration form. Make sure you select the **User Type** as **admin**

![Image](/project-screenshots/elrond-registration.jpg)

4. Click Register.
5. Once saved, you can login as the new user and make changes. 
6. The new admin should also be able to login to the Django console.

![Image](/project-screenshots/elrond-adming-console.jpg)