# Student-Teacher-Staff Management System

This Python code provides three classes for managing students, teachers, and staff members in a school.

## Class Definitions

### Student

The `Student` class represents a student in a school. It has the following attributes:

- `first_name` (str): the student's first name.
- `last_name` (str): the student's last name.
- `age` (int): the student's age.

It also has the following methods:

- `my_fname()`: prints the student's first name.
- `my_lname()`: prints the student's last name.
- `my_info()`: prints the student's full name.

### Teacher

The `Teacher` class represents a teacher in a school. It has the following attributes:

- `first_name` (str): the teacher's first name.
- `last_name` (str): the teacher's last name.
- `age` (int): the teacher's age.

It also has the following methods:

- `my_fname()`: prints the teacher's first name.
- `my_lname()`: prints the teacher's last name.
- `my_info()`: prints the teacher's full name.

### Staff

The `Staff` class represents a staff member in a school. It has the following attributes:

- `first_name` (str): the staff member's first name.
- `last_name` (str): the staff member's last name.
- `age` (int): the staff member's age.

It also has the following methods:

- `my_fname()`: prints the staff member's first name.
- `my_lname()`: prints the staff member's last name.
- `my_info()`: prints the staff member's full name.

## Example Usage

```python
# Create a student
student = Student("John", "Doe", 18)

# Print the student's first name
student.my_fname() # Output: My first name is: John

# Print the student's last name
student.my_lname() # Output: My last name is: Doe

# Print the student's full name
student.my_info() # Output: My full name is: John Doe
```

## Output

```python
My first name is: John
My last name is: Doe
My full name is: John Doe
```