Employee Management System(3.5)

Write SQL queries for all the following questions using the `employees` table and sample data provided below.

Table: `employees`

Columns: `employee_id`, `employee_name`, `department`, `city`, `salary`, `joining_date`, `experience`, `age`, `gender`,
 `employment_type`, `skills`, `email`, `manager_id`

Sample Data

| employee_id | employee_name | department | city | salary | joining_date | experience | age | gender | employment_type | skills | email | manager_id |
|---:|---|---|---|---:|---|---:|---:|---|---|---|---|---:|
| 101 | Amit Sharma | IT | Indore | 75000 | 2023-05-10 | 5 | 30 | MALE | FULL_TIME | JAVA,SQL,SPRING | amit@company.com | 501 |
| 102 | Sneha Patel | Finance | Pune | 65000 | 2024-02-15 | 4 | 28 | FEMALE | FULL_TIME | SQL,PYTHON | sneha@company.com | 502 |
| 103 | Rahul Verma | Development | Delhi | 85000 | 2022-08-20 | 7 | 32 | MALE | FULL_TIME | JAVA,SQL,REACT | rahul@company.com | 501 |
| 104 | Anjali Gupta | HR | Mumbai | 35000 | 2023-11-01 | 3 | 27 | FEMALE | CONTRACT | SQL | NULL | 503 |
| 105 | Suresh Kumar | IT | Bhopal | 28000 | 2021-06-12 | 6 | 35 | MALE | FULL_TIME | JAVA,SPRING | NULL | NULL |
| 106 | Priya Singh | Development | Indore | 95000 | 2025-01-10 | 4 | 29 | FEMALE | FULL_TIME | PYTHON,REACT,SQL | priya@company.com | 501 |
| 107 | Arjun Mehta | Finance | Delhi | 45000 | 2022-03-25 | 3 | 26 | MALE | PART_TIME | SQL,PYTHON | arjun@company.com | NULL |
| 108 | Simran Kaur | IT | Pune | 55000 | 2024-07-18 | 5 | 31 | FEMALE | FULL_TIME | JAVA,SQL,REACT | simran@company.com | 504 |

Note: The `skills` column is a MySQL `SET` column. Use appropriate conditions to check individual skills.

Questions

Q1. (0.5 Marks)

Display employees belonging to IT, Finance, or Development whose salary is between ₹40,000 and ₹90,000, experience is greater than 3 years, email and manager ID are both NOT NULL, and city is neither Mumbai nor Bhopal.

Q2. (0.5 Marks)

Display employees whose names start with 'A' or contain the letter 'a', who joined after '2023-01-01', and whose salary is greater than ₹50,000 OR experience is greater than 6 years. Exclude employees from HR and Mumbai.

Q3. (0.5 Marks)

Display FULL_TIME employees from IT or Development who have **both JAVA and SQL skills or both PYTHON and REACT skills**, earn more than ₹60,000, and have a non-NULL email.

Q4. (0.5 Marks)

Display employees from IT, Finance, or HR whose age is between 25 and 40, salary is NOT between ₹30,000 and ₹60,000, experience is greater than 2 years, and city is neither Mumbai nor Bhopal.

Q5. (0.5 Marks)

Display employees who joined between '2022-01-01' and '2025-12-31', have JAVA or PYTHON skills, earn more than ₹45,000, and have either email or manager ID as NULL. Their experience must be greater than 3 years.

Q6. (0.5 Marks)

Display employees whose names start with 'S' or contain the letter 'a', belong to IT or Finance, earn between ₹40,000 and ₹1,00,000, have more than 2 years of experience, and have both email and manager ID NOT NULL. They must have JAVA or PYTHON skills. Display the results ordered by department in ascending order and salary in descending order.

NOTE: Table creation and insertion will be .5 marks

=====================================


(101, 'Amit Sharma', 'IT', 'Indore', 75000, '2023-05-10', 5, 30, 'MALE', 'FULL_TIME', 'JAVA,SQL,SPRING', 'amit@company.com', 501),
(102, 'Sneha Patel', 'Finance', 'Pune', 65000, '2024-02-15', 4, 28, 'FEMALE', 'FULL_TIME', 'SQL,PYTHON', 'sneha@company.com', 502),

(103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'MALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'rahul@company.com', 501),

(104, 'Anjali Gupta', 'HR', 'Mumbai', 35000, '2023-11-01', 3, 27, 'FEMALE', 'CONTRACT', 'SQL', NULL, 503),

(105, 'Suresh Kumar', 'IT', 'Bhopal', 28000, '2021-06-12', 6, 35, 'MALE', 'FULL_TIME', 'JAVA,SPRING', NULL, NULL),

(106, 'Priya Singh', 'Development', 'Indore', 95000, '2025-01-10', 4, 29, 'FEMALE', 'FULL_TIME', 'PYTHON,REACT,SQL', 'priya@company.com', 501),

(107, 'Arjun Mehta', 'Finance', 'Delhi', 45000, '2022-03-25', 3, 26, 'MALE', 'PART_TIME', 'SQL,PYTHON', 'arjun@company.com', NULL),

(108, 'Simran Kaur', 'IT', 'Pune', 55000, '2024-07-18', 5, 31, 'FEMALE', 'FULL_TIME', 'JAVA,SQL,REACT', 'simran@company.com', 504);


# mysql> show databases;
# +----------------------------+
# | Database                   |
# +----------------------------+
# | batch19                    |
# | batch20                    |
# | batch21                    |
# | company_db                 |
# | employee                   |
# | employee_12                |
# | employee_13                |
# | employee_management        |
# | employee_management_system |
# | gym                        |
# | hospital                   |
# | information_schema         |
# | job_management_system      |
# | library                    |
# | library_management_system  |
# | movie                      |
# | mysql                      |
# | performance_schema         |
# | product_management_system  |
# | school2                    |
# | school_db                  |
# | shop_db                    |
# | student                    |
# | sys                        |
# | today                      |
# +----------------------------+
# 25 rows in set (0.01 sec)

# mysql> create database employee_management_system2;
# Query OK, 1 row affected (0.02 sec)

# mysql> use employee_management_system2;
# Database changed
# mysql> create table employees(employee_id int ,employee_name varachar(20),department varchar(20),city varchar(20),salary decimal(10,2),joining_date date,experience int,age int,gender enum('male','female'),employment_type enum ('full time','part time'),skills set ('python','sql','java','spring','react'),email varchar(20),manager_id int );
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'varachar(20),department varchar(20),city varchar(20),salary decimal(10,2),joinin' at line 1
# mysql> create table employees(employee_id int ,employee_name varchar(20),department varchar(20),city varchar(20),salary decimal(10,2),joining_date date,experience int,age int,gender enum('male','female'),employment_type enum ('full time','part time'),skills set ('python','sql','java','spring','react'),email varchar(20),manager_id int );
# Query OK, 0 rows affected (0.05 sec)

# mysql> desc employee_management_system2;
# ERROR 1146 (42S02): Table 'employee_management_system2.employee_management_system2' doesn't exist
# mysql> desc employees;
# +-----------------+---------------------------------------------+------+-----+---------+-------+
# | Field           | Type                                        | Null | Key | Default | Extra |
# +-----------------+---------------------------------------------+------+-----+---------+-------+
# | employee_id     | int                                         | YES  |     | NULL    |       |
# | employee_name   | varchar(20)                                 | YES  |     | NULL    |       |
# | department      | varchar(20)                                 | YES  |     | NULL    |       |
# | city            | varchar(20)                                 | YES  |     | NULL    |       |
# | salary          | decimal(10,2)                               | YES  |     | NULL    |       |
# | joining_date    | date                                        | YES  |     | NULL    |       |
# | experience      | int                                         | YES  |     | NULL    |       |
# | age             | int                                         | YES  |     | NULL    |       |
# | gender          | enum('male','female')                       | YES  |     | NULL    |       |
# | employment_type | enum('full time','part time')               | YES  |     | NULL    |       |
# | skills          | set('python','sql','java','spring','react') | YES  |     | NULL    |       |
# | email           | varchar(20)                                 | YES  |     | NULL    |       |
# | manager_id      | int                                         | YES  |     | NULL    |       |
# +-----------------+---------------------------------------------+------+-----+---------+-------+
# 13 rows in set (0.01 sec)
#  INSERT INTO employees
#     -> (employee_id, employee_name, department, city, salary, joining_date, experience, age, gender, employment_type, skills, email, manager_id)
#     -> VALUES
#     -> (101, 'Amit Sharma', 'IT', 'Indore', 75000, '2023-05-10', 5, 30, 'male', 'full time', 'java,sql,spring', 'amit@company.com', 501),
#     -> (102, 'Sneha Patel', 'Finance', 'Pune', 65000, '2024-02-15', 4, 28, 'female', 'full time', 'sql,python', 'sneha@company.com', 502),
#     -> (103, 'Rahul Verma', 'Development', 'Delhi', 85000, '2022-08-20', 7, 32, 'male', 'full time', 'java,sql,react', 'rahul@company.com', 501),
#     -> (104, 'Anjali Gupta', 'HR', 'Mumbai', 35000, '2023-11-01', 3, 27, 'female', 'part time', 'sql', NULL, 503),
#     -> (105, 'Suresh Kumar', 'IT', 'Bhopal', 28000, '2021-06-12', 6, 35, 'male', 'full time', 'java,spring', NULL, NULL),
#     -> (106, 'Priya Singh', 'Development', 'Indore', 95000, '2025-01-10', 4, 29, 'female', 'full time', 'python,react,sql', 'priya@company.com', 501),
#     -> (107, 'Arjun Mehta', 'Finance', 'Delhi', 45000, '2022-03-25', 3, 26, 'male', 'part time', 'sql,python', 'arjun@company.com', NULL),
#     -> (108, 'Simran Kaur', 'IT', 'Pune', 55000, '2024-07-18', 5, 31, 'female', 'full time', 'java,sql,react', 'simran@company.com', 504);
# Query OK, 8 rows affected (0.01 sec)
# Records: 8  Duplicates: 0  Warnings: 0
