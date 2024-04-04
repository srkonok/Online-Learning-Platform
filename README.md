
---

# Online Learning Platform Backend

This is the backend system for an online learning platform built with Django and MySQL. It provides APIs for managing courses and student enrollments.

## Table of Contents

- [Online Learning Platform Backend](#online-learning-platform-backend)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [API Endpoints](#api-endpoints)
      - [Course API:](#course-api)
      - [Enrollment API:](#enrollment-api)
    - [Examples](#examples)
      - [GET /courses:](#get-courses)
      - [POST /courses:](#post-courses)
  - [Testing](#testing)
  - [Dependencies](#dependencies)

## Getting Started

### Prerequisites

Before setting up the application, ensure you have the following installed:

- Python 3.x
- MySQL

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:srkonok/Online-Learning-Platform.git
   ```

2. Navigate to the project directory:

   ```bash
   cd online-learning-platform
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Update the MySQL database settings in `learning_platform/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'online_learning_platform',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Apply migrations to create database tables:

   ```bash
   python manage.py migrate
   ```

## Usage

### API Endpoints

#### Course API:

- **GET /courses**: Retrieve a list of available courses.
- **GET /courses/:id**: Retrieve a specific course by its ID.
- **POST /courses**: Create a new course.

#### Enrollment API:

- **POST /enrollments**: Allow students to enroll in a course.

### Examples

#### GET /courses:

Retrieves a list of available courses.

Request:

```bash
curl -X GET http://localhost:8000/courses/
```

Response:

```json
[
    {
        "title": "Python Programming",
        "description": "Learn Python programming language",
        "instructor": "John Doe",
        "duration": 60,
        "price": 49.99
    },
    {
        "title": "Web Development",
        "description": "Learn web development with Django",
        "instructor": "Jane Smith",
        "duration": 90,
        "price": 69.99
    }
]
```

#### POST /courses:

Creates a new course.

Request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "JavaScript Basics", "description": "Learn JavaScript fundamentals", "instructor": "Alice Johnson", "duration": 45, "price": 39.99}' http://localhost:8000/courses/
```

Response:

```json
{
    "title": "JavaScript Basics",
    "description": "Learn JavaScript fundamentals",
    "instructor": "Alice Johnson",
    "duration": 45,
    "price": 39.99
}
```

## Testing

To run the test suite, execute the following command:

```bash
python manage.py test
```

## Dependencies

The project depends on the following Python packages:

- Django
- mysqlclient

These dependencies are listed in the `requirements.txt` file and can be installed using `pip`.

---

