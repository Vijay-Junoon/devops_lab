# Student Grade Calculator

A simple Python command-line application that calculates a student's average marks and assigns a grade based on the average.

The application accepts:

* Student name
* Number of subjects
* Subject names
* Marks for each subject

It then displays the student's marks, average, and final grade.

## Grade Criteria

|  Average | Grade |
| -------: | :---- |
|      90+ | O     |
|    80–89 | A+    |
|    70–79 | A     |
|    60–69 | B+    |
|    50–59 | B     |
|    40–49 | C     |
| Below 40 | Fail  |

## Technologies Used

* Python
* Docker

## Run Locally

Make sure Python is installed, then run:

```bash
python app.py
```

Example:

```text
Enter student name: Vijay
Enter number of subjects: 3
Enter subject name and marks:
Python 90
DBMS 85
ML 92

RESULT

Student: Vijay

Python - 90
DBMS - 85
ML - 92

AVERAGE: 89.00
GRADE: A+
```

## Run Using Docker

### 1. Build the Docker image

```bash
docker build -t student-grade-app .
```

### 2. Run the container

Since the application accepts user input, use the `-it` flags:

```bash
docker run -it student-grade-app
```

The application will then run interactively inside the Docker container.

## Project Structure

```text
student-grade-calculator/
│
├── app.py
├── Dockerfile
└── README.md
```

## Dockerfile

The application uses a lightweight Python image:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "-u", "app.py"]
```

## Purpose

This project was created as a basic introduction to:

* Python functions and dictionaries
* User input and loops
* Dockerfiles
* Docker image creation
* Running Python applications inside Docker containers
