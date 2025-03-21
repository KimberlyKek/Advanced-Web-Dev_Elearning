# CM3035 - Advanced-Web-Dev: Elearning Website

An online learning website is designed to create an interactive and engaging learning environment for both students and teachers. Students can access a variety of courses, enroll themselves to the course, interact with peers and teachers through discussion forums and leave feedback for the course. Teachers can easily create and manage courses, upload materials, remove students from the course and search for students and other teachers. With real-time communication tools and resource sharing, the platform fosters a collaborative learning experience, making education accessible and effective for all.

## Flow Chart
![image](https://github.com/user-attachments/assets/c0509a31-3228-4923-ad91-5e416154fe29)

## Student and Teacher Dashboards
![image](https://github.com/user-attachments/assets/963851f7-a4e5-4c51-b275-781ffe2274ca)
![image](https://github.com/user-attachments/assets/0cb5b019-b02c-47e6-94de-21a287f161d3)

## Course Dashboard
![image](https://github.com/user-attachments/assets/22a9da60-10d3-4b1f-9f85-edcc437eb28b)
![image](https://github.com/user-attachments/assets/8b17e71a-d2a3-48f2-b05b-d7fdd3377a0e)
![image](https://github.com/user-attachments/assets/b83844d2-d4fe-4f8c-be98-5538c533ba90)
![image](https://github.com/user-attachments/assets/a41437d8-1a19-493b-8f76-8f82c3ef76ab)

## Features
- **User Authentication**: Users sign up and log in as student or teacher
- **Update Profile**: Edit user's username, email, avator and status
- **Enroll Course**: Students to enroll into a course
- **Create Course**: Teachers to create a new course
- **Search Users**: Teachers to search for students and other teachers only
- **Upload Course Materials**: Teachers to upload files on the course dashboard to share to students enrolled to the same course
- **View Course Materials**: Teachers and students to view and download the files on the course dashboard
- **Create Announcements**: Teachers to make an announcements to students on the course dashboard
- **View Announcements**: Teachers and students to view the announcements
- **Students List**: Teachers and students can view other students' info enrolled to the same course
- **Remove Students**: Teachers to remove students from the course
- **Create Feedback**: Students to create feedback based on the course enrolled on the course dashboard
- **View Feedback**: Teachers to view the feedback created by the students
- **Course Chatroom**: Students and teachers can communicate through the chatroom page

## Technologies Used
- **Frontend**:
  - HTML
  - CSS3
  - JavaScript
  - Python
- **Backend**:
  - Django
  - SQLite

## Installation Instructions: 
  
1. Create Vitural Environment: <br>
```
python -m venv (env name)
```
2.  Clone the respository and save it to where your environment is stored: <br>
```
git clone https://github.com/KimberlyKek/Advanced-Web-Dev_Elearning.git
```
3. Install all the packages: <br>
```
pip install -r requirements.txt
```
4. Enter environment: <br>
```
(env name)\Scripts\Activate.bat
```
5. Run the application: <br>
```
python manage.py runserver 127.0.0.1:8080
```
  
