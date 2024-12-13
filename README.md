# FINAL-Mini-Project

1. Setting up EC2 instance(ssh, http, https, all traffic)

2. Connect to instance: ssh -i /Users/timur/Desktop/Timur.pem ubuntu@13.61.3.152

3. Update the package list: sudo apt update, sudo apt upgrade

4. Install PostgreSQL client: sudo apt install postgresql-client -y

5. psql -h postgres.cnq042mcc64k.eu-north-1.rds.amazonaws.com -U postgres -d postgres

6. DROP TABLE timetable: deleting the table that i created in my first attempt

7. CREATE TABLE timetable (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    level VARCHAR(20),
    day VARCHAR(20),
    time VARCHAR(20)
     ):

8. INSERT INTO timetable (course_name, level, day, time) (https://classes.webster.edu/)
VALUES
    ('Personal Finance', 'Undergraduate', 'Monday', '10:00 AM'),
    ('Computer Programming I', 'Undergraduate', 'Tuesday', '12:00 PM'),
    ('Design Thinking', 'Graduate', 'Wednesday', '6:00 PM'),
    ('Operating Systems', 'Undergraduate', 'Thursday', '4:30 PM'),
    ('Value Creation', 'Graduate', 'Friday', '3:00 PM');
   
9. Creating the project directory: mkdir my_project, cd my_project, nano app.py

10. Creating a templates directory: mkdir templates, cd templates, nano index.html

11. Intsalling Flask: pip install flask

12. Creating a virtual environment: python3 -m venv venv

13. Activating: source venv/bin/activate

14. Running py file: python3 app.py

15. http:13.61.3.152:8000

