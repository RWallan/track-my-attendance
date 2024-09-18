# Track My Attendance

**Track My Attendance** is a platform designed to help students easily monitor their class attendance and predict trends in their presence across different subjects.

## Key Features

- **Simplicity First:** A streamlined user experience focused on easy attendance tracking.
- **User-Friendly:** Intuitive interface without unnecessary complexity—no overwhelming menus or buttons.
- **Minimalist Approach:** Offers only the essentials to keep your attendance organized and accessible.
- **Detailed Analytics:** Monitor your attendance trends and predict future attendance patterns.
- **Secure and Reliable:** Built with security best practices to protect user data.

---

## Table of Contents

- [Technology Stack](#technology-stack)
- [Database Schema Overview](#database-schema-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Technology Stack

### Backend

- **[FastAPI](https://fastapi.tiangolo.com/):** High-performance Python web framework for building APIs.
- **[SQLAlchemy](https://www.sqlalchemy.org/):** Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **[Pydantic](https://docs.pydantic.dev/latest/):** Data validation and settings management using Python type annotations.

### Frontend

- **[Svelte](https://svelte.dev/):** Modern and reactive framework for building highly efficient user interfaces.

### Database

- **Relational Database Management System (RDBMS):** Structured database schema for efficient data management.

### Security

- **Password Hashing:** Secure password storage using industry-standard hashing algorithms.
- **JWT Authentication:** Secure user authentication with JSON Web Tokens.
- **Input Validation:** Robust validation to prevent injection attacks and ensure data integrity.

### Testing and CI/CD

- **Testing with Pytest:** Comprehensive test suite for backend and frontend components.
- **Continuous Integration:** Automated testing and deployment using GitHub Actions.

---

## Database Schema Overview

The **Track My Attendance** platform uses a well-structured database schema to manage all aspects of attendance tracking. Below is an overview of the key tables and their relationships:

### Tables

1. **students**
2. **course_types**
3. **courses**
4. **course_modules**
5. **course_agenda**
6. **student_agenda**
7. **presence_history**
8. **presence_lessons_count_history**

---

### 1. `students`

Stores information about the students enrolled in the platform.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each student.
  - `name` (`VARCHAR`): Full name of the student.

---

### 2. `course_types`

Defines the various types of courses available.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each course type.
  - `name` (`VARCHAR`): Name of the course type (e.g., 'Online', 'Onsite', 'Hybrid').

---

### 3. `courses`

Contains details about the courses offered.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each course.
  - `type_id` (`INT`, Foreign Key): References `course_types.id`; indicates the type of the course.
  - `name` (`VARCHAR`): Name of the course.
  - `period_type` (`VARCHAR`): Time period of the course (e.g., 'Diurno' for daytime, 'Vespertino' for evening).
  - `absences_percentage` (`INT`): Maximum allowed absence percentage (0 to 100).
  - `description` (`TEXT`): Detailed description of the course.

---

### 4. `course_modules`

Breaks down courses into manageable modules.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each module.
  - `course_id` (`INT`, Foreign Key): References `courses.id`; associates the module with a course.
  - `name` (`VARCHAR`): Name of the module.
  - `lessons_count` (`INT`): Total number of lessons in the module.
  - `description` (`TEXT`): Detailed description of the module.

---

### 5. `course_agenda`

Schedules modules with specific start and end times.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each agenda entry.
  - `module_id` (`INT`, Foreign Key): References `course_modules.id`; associates the agenda with a module.
  - `instructor_id` (`INT`, Foreign Key, Optional): References `instructors.id`; identifies the instructor (if applicable).
  - `starting_at` (`TIMESTAMP`): Start date and time of the module.
  - `ending_at` (`TIMESTAMP`): End date and time of the module.

---

### 6. `student_agenda`

Associates students with specific course agendas.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each record.
  - `course_agenda_id` (`INT`, Foreign Key): References `course_agenda.id`; links the student to an agenda.
  - `student_id` (`INT`, Foreign Key): References `students.id`; identifies the student.

---

### 7. `presence_history`

Records attendance for each student per lesson.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each attendance record.
  - `student_id` (`INT`, Foreign Key): References `students.id`; identifies the student.
  - `course_agenda_id` (`INT`, Foreign Key): References `course_agenda.id`; associates the attendance with a scheduled module.
  - `attended` (`BOOLEAN`): Indicates attendance status (`TRUE` for attended, `FALSE` for absent).
  - `created_at` (`TIMESTAMP`): Timestamp when the record was created.

---

### 8. `presence_lessons_count_history`

Keeps track of the total number of lessons attended and missed by each student for each course agenda.

- **Fields:**
  - `id` (`INT`, Primary Key): Unique identifier for each record.
  - `student_id` (`INT`, Foreign Key): References `students.id`; identifies the student.
  - `course_agenda_id` (`INT`, Foreign Key): References `course_agenda.id`; associates the counts with a scheduled module.
  - `attended_count` (`INT`): Total number of lessons attended by the student.
  - `missed_count` (`INT`): Total number of lessons missed by the student.

---

### Relationships and Constraints

- **Students and Course Enrollment:**
  - A student can be enrolled in multiple course agendas.
  - `student_agenda.student_id` references `students.id`.

- **Courses and Modules:**
  - A course consists of multiple modules.
  - `course_modules.course_id` references `courses.id`.

- **Modules and Scheduling:**
  - A module can have multiple scheduled agendas.
  - `course_agenda.module_id` references `course_modules.id`.

- **Attendance Tracking:**
  - Attendance is recorded for each student per lesson.
  - `presence_history` records individual attendance events.
  - `presence_lessons_count_history` aggregates attendance data for reporting.

---

## Installation

### Prerequisites

- **Python 3.8+**
- **Node.js and npm**
- **Virtual Environment Tool** (e.g., `venv`, `conda`)
- **Git**

### Backend Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/RWallan/track-my-attendance.git
   cd track-my-attendance/backend
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Backend Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**

   Ensure you have a database set up and configured in your environment variables.

   ```bash
   # Assuming Alembic is used for migrations
   alembic upgrade head
   ```

5. **Start the Backend Server**

   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. **Navigate to the Frontend Directory**

   ```bash
   cd ../frontend
   ```

2. **Install Frontend Dependencies**

   ```bash
   npm install
   ```

3. **Start the Frontend Server**

   ```bash
   npm run dev
   ```

### Accessing the Application

- Open your browser and navigate to `http://localhost:3000` to access the frontend.
- The backend API will be running at `http://localhost:8000`.

---

## Usage

Once the application is running, you can:

- **Create an Account:** Sign up using your email and password.
- **Log In:** Access your dashboard by logging in.
- **Add Courses:** Input your courses and organize them by type and schedule.
- **Track Attendance:** Mark your attendance for each lesson directly from your dashboard.
- **View Reports:** Monitor your attendance trends over time and ensure you meet course requirements.

---

## Roadmap

Planned features and enhancements include:

- [ ] **Database Modeling:** Introduce Presented Modeling
- [ ] **Base CRUD:** Implement all routes provided
	- [ ] 
- **Mobile Application:** Develop mobile apps for iOS and Android platforms.
- **Notifications:** Implement email and push notifications for attendance alerts.
- **Calendar Integration:** Sync course agendas with external calendar services like Google Calendar.
- **Advanced Analytics:** Provide detailed analytics and predictions based on attendance data.
- **Multi-Language Support:** Expand accessibility by supporting multiple languages.


## Planned Routes (WIP)

# Backend API Endpoint Roadmap

Based on the data modeling, here is a detailed list of backend API endpoints for the **Track My Attendance** platform, formatted as per your specified template.

---

## 1. Authentication

- [ ] **POST** `/auth/register`
  - **Description:** Registers a new user (student or instructor).
  - **Request Body:**
    ```json
    {
      "name": "string",
      "email": "string",
      "password": "string",
      "role": "student" | "instructor"
    }
    ```

- [ ] **POST** `/auth/login`
  - **Description:** Authenticates a user and returns an access token.
  - **Request Body:**
    ```json
    {
      "email": "string",
      "password": "string"
    }
    ```

- [ ] **POST** `/auth/refresh`
  - **Description:** Refreshes the access token using a refresh token.
  - **Request Body:**
    ```json
    {
      "refresh_token": "string"
    }
    ```

---

## 2. Students

- [ ] **GET** `/students`
  - **Description:** Retrieves a list of all students.
  - **Request Body:** None

- [ ] **GET** `/students/{student_id}`
  - **Description:** Retrieves details of a specific student.
  - **Request Body:** None

- [ ] **POST** `/students`
  - **Description:** Creates a new student record.
  - **Request Body:**
    ```json
    {
      "name": "string",
      "email": "string",
      "password": "string"
    }
    ```

- [ ] **PUT** `/students/{student_id}`
  - **Description:** Updates information for a specific student.
  - **Request Body:**
    ```json
    {
      "name": "string (optional)",
      "email": "string (optional)",
      "password": "string (optional)"
    }
    ```

- [ ] **DELETE** `/students/{student_id}`
  - **Description:** Deletes a specific student record.
  - **Request Body:** None

---

## 3. Course Types

- [ ] **GET** `/course-types`
  - **Description:** Retrieves a list of all course types.
  - **Request Body:** None

- [ ] **GET** `/course-types/{type_id}`
  - **Description:** Retrieves details of a specific course type.
  - **Request Body:** None

- [ ] **POST** `/course-types`
  - **Description:** Creates a new course type.
  - **Request Body:**
    ```json
    {
      "name": "string"
    }
    ```

- [ ] **PUT** `/course-types/{type_id}`
  - **Description:** Updates a specific course type.
  - **Request Body:**
    ```json
    {
      "name": "string"
    }
    ```

- [ ] **DELETE** `/course-types/{type_id}`
  - **Description:** Deletes a specific course type.
  - **Request Body:** None

---

## 4. Courses

- [ ] **GET** `/courses`
  - **Description:** Retrieves a list of all courses.
  - **Request Body:** None

- [ ] **GET** `/courses/{course_id}`
  - **Description:** Retrieves details of a specific course.
  - **Request Body:** None

- [ ] **POST** `/courses`
  - **Description:** Creates a new course.
  - **Request Body:**
    ```json
    {
      "type_id": "int",
      "name": "string",
      "period_type": "string",
      "absences_percentage": "int (0-100)",
      "description": "string"
    }
    ```

- [ ] **PUT** `/courses/{course_id}`
  - **Description:** Updates a specific course.
  - **Request Body:**
    ```json
    {
      "type_id": "int (optional)",
      "name": "string (optional)",
      "period_type": "string (optional)",
      "absences_percentage": "int (0-100, optional)",
      "description": "string (optional)"
    }
    ```

- [ ] **DELETE** `/courses/{course_id}`
  - **Description:** Deletes a specific course.
  - **Request Body:** None

- [ ] **GET** `/courses/{course_id}/modules`
  - **Description:** Retrieves all modules associated with a specific course.
  - **Request Body:** None

---

## 5. Course Modules

- [ ] **GET** `/modules`
  - **Description:** Retrieves a list of all modules.
  - **Request Body:** None

- [ ] **GET** `/modules/{module_id}`
  - **Description:** Retrieves details of a specific module.
  - **Request Body:** None

- [ ] **POST** `/modules`
  - **Description:** Creates a new module.
  - **Request Body:**
    ```json
    {
      "course_id": "int",
      "name": "string",
      "lessons_count": "int",
      "description": "string"
    }
    ```

- [ ] **PUT** `/modules/{module_id}`
  - **Description:** Updates a specific module.
  - **Request Body:**
    ```json
    {
      "course_id": "int (optional)",
      "name": "string (optional)",
      "lessons_count": "int (optional)",
      "description": "string (optional)"
    }
    ```

- [ ] **DELETE** `/modules/{module_id}`
  - **Description:** Deletes a specific module.
  - **Request Body:** None

- [ ] **GET** `/modules/{module_id}/agenda`
  - **Description:** Retrieves all agenda items associated with a specific module.
  - **Request Body:** None

---

## 6. Course Agenda

- [ ] **GET** `/agenda`
  - **Description:** Retrieves a list of all course agendas.
  - **Request Body:** None

- [ ] **GET** `/agenda/{agenda_id}`
  - **Description:** Retrieves details of a specific agenda item.
  - **Request Body:** None

- [ ] **POST** `/agenda`
  - **Description:** Creates a new agenda item.
  - **Request Body:**
    ```json
    {
      "module_id": "int",
      "instructor_id": "int (optional)",
      "starting_at": "ISO 8601 timestamp",
      "ending_at": "ISO 8601 timestamp"
    }
    ```

- [ ] **PUT** `/agenda/{agenda_id}`
  - **Description:** Updates a specific agenda item.
  - **Request Body:**
    ```json
    {
      "module_id": "int (optional)",
      "instructor_id": "int (optional)",
      "starting_at": "ISO 8601 timestamp (optional)",
      "ending_at": "ISO 8601 timestamp (optional)"
    }
    ```

- [ ] **DELETE** `/agenda/{agenda_id}`
  - **Description:** Deletes a specific agenda item.
  - **Request Body:** None

---

## 7. Student Agenda

- [ ] **GET** `/students/{student_id}/agenda`
  - **Description:** Retrieves all agenda items a specific student is enrolled in.
  - **Request Body:** None

- [ ] **POST** `/students/{student_id}/agenda`
  - **Description:** Enrolls a student in an agenda item.
  - **Request Body:**
    ```json
    {
      "course_agenda_id": "int"
    }
    ```

- [ ] **DELETE** `/students/{student_id}/agenda/{agenda_id}`
  - **Description:** Removes a student from a specific agenda item.
  - **Request Body:** None

---

## 8. Presence History

- [ ] **GET** `/attendance`
  - **Description:** Retrieves all attendance records.
  - **Request Body:** None

- [ ] **GET** `/students/{student_id}/attendance`
  - **Description:** Retrieves attendance records for a specific student.
  - **Request Body:** None

- [ ] **POST** `/attendance`
  - **Description:** Records attendance for a student in a specific agenda item.
  - **Request Body:**
    ```json
    {
      "student_id": "int",
      "course_agenda_id": "int",
      "attended": "boolean"
    }
    ```

- [ ] **PUT** `/attendance/{attendance_id}`
  - **Description:** Updates a specific attendance record.
  - **Request Body:**
    ```json
    {
      "attended": "boolean"
    }
    ```

- [ ] **DELETE** `/attendance/{attendance_id}`
  - **Description:** Deletes a specific attendance record.
  - **Request Body:** None

---

## 9. Presence Lessons Count History

- [ ] **GET** `/students/{student_id}/attendance-summary`
  - **Description:** Retrieves the attendance summary for a specific student.
  - **Request Body:** None

- [ ] **GET** `/agenda/{agenda_id}/attendance-summary`
  - **Description:** Retrieves attendance summaries for all students in a specific agenda.
  - **Request Body:** None

---

## 10. Instructors

*(Assuming the addition of instructors to the system)*

- [ ] **GET** `/instructors`
  - **Description:** Retrieves a list of all instructors.
  - **Request Body:** None

- [ ] **GET** `/instructors/{instructor_id}`
  - **Description:** Retrieves details of a specific instructor.
  - **Request Body:** None

- [ ] **POST** `/instructors`
  - **Description:** Creates a new instructor record.
  - **Request Body:**
    ```json
    {
      "name": "string",
      "email": "string",
      "password": "string"
    }
    ```

- [ ] **PUT** `/instructors/{instructor_id}`
  - **Description:** Updates information for a specific instructor.
  - **Request Body:**
    ```json
    {
      "name": "string (optional)",
      "email": "string (optional)",
      "password": "string (optional)"
    }
    ```

- [ ] **DELETE** `/instructors/{instructor_id}`
  - **Description:** Deletes a specific instructor record.
  - **Request Body:** None

---

## 11. Reports and Analytics

- [ ] **GET** `/reports/students/{student_id}/attendance`
  - **Description:** Generates an attendance report for a specific student.
  - **Request Body:** None

- [ ] **GET** `/reports/courses/{course_id}/attendance`
  - **Description:** Generates an attendance report for a specific course.
  - **Request Body:** None

- [ ] **GET** `/reports/attendance/trends`
  - **Description:** Provides analytics on overall attendance trends.
  - **Request Body:** None

---

## 12. Notifications

*(If notifications feature is implemented)*

- [ ] **POST** `/notifications/students/{student_id}`
  - **Description:** Sends a notification to a specific student.
  - **Request Body:**
    ```json
    {
      "message": "string"
    }
    ```

- [ ] **GET** `/students/{student_id}/notifications`
  - **Description:** Retrieves all notifications sent to a specific student.
  - **Request Body:** None

---

## Implementation Roadmap

- [ ]  **Phase 1: Authentication and User Management**
   - Implement `/auth/register`, `/auth/login`, and `/auth/refresh`.
   - Set up user roles and permissions.

- [ ]  **Phase 2: Core Data Models**
   - Develop endpoints for `students`, `course-types`, `courses`, and `modules`.

- [ ]  **Phase 3: Scheduling and Enrollment**
   - Implement `course agenda` and `student agenda` endpoints.
   - Allow students to enroll in courses and view their schedules.

- [ ]  **Phase 4: Attendance Tracking**
   - Create endpoints for `presence history` and `presence lessons count history`.
   - Enable instructors to record and update attendance.

- [ ]  **Phase 5: Reporting and Analytics**
   - Develop reporting endpoints for attendance summaries and trends.

- [ ]  **Phase 6: Notifications (Optional)**
   - Implement notification system endpoints if required.

- [ ]  **Phase 7: Testing and Documentation**
   - Write unit and integration tests for all endpoints.
   - Document all APIs using Swagger or similar tools.

---

## Example Usage

### Register a New User

- **Endpoint:** `POST /auth/register`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "SecurePass123",
    "role": "student"
  }
  ```

### Record Attendance

- **Endpoint:** `POST /attendance`
- **Request Body:**
  ```json
  {
    "student_id": 123,
    "course_agenda_id": 456,
    "attended": true
  }
  ```

---

Feel free to adjust or expand upon this list as your project requirements evolve.

---

## Contributing

Thank you for your interest in contributing to the **Track My Attendance** project!

### Reporting Bugs

If you discover a bug, please check the [GitHub Issues](https://github.com/RWallan/track-my-attendance/issues) page to see if it has already been reported. If not, please use the "Bug Report" template to provide detailed information about the issue, including steps to reproduce it.

### Suggesting Features

To suggest a new feature or improvement, first check the [GitHub Issues](https://github.com/RWallan/track-my-attendance/issues) to ensure a similar suggestion hasn't already been made. Use the "Feature Request" template to provide a detailed description of your suggestion.

### Questions

If you have any questions or need clarifications, join the discussion on the [GitHub Discussions](https://github.com/RWallan/track-my-attendance/discussions) page.

### Contributing Code

Before submitting code changes, check if there are similar [Pull Requests](https://github.com/RWallan/track-my-attendance/pulls) already open to prevent duplicate efforts. Please follow these guidelines:

#### Requirements for Merging a Pull Request

- **Coding Standards:** Adhere to project coding standards, formatting, and linting rules. Check the guidelines for each component.
- **Testing:** Write comprehensive tests and ensure all tests pass.
- **Test Coverage:** Maintain or improve test coverage—no reductions are allowed.
- **Documentation:** Update documentation and comments where applicable.

---

## License

This project is licensed under the terms of the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **FastAPI Community:** For providing a robust framework that accelerates backend development.
- **Svelte Team:** For creating a frontend framework that enhances user experience.
- **Contributors:** Thanks to everyone who has contributed to the project.

---

## Contact

For further information, you can reach out via:

- **Email:** [support@trackmyattendance.com](mailto:support@trackmyattendance.com)
- **GitHub Issues:** [Track My Attendance Issues](https://github.com/RWallan/track-my-attendance/issues)
- **GitHub Discussions:** [Join the Conversation](https://github.com/RWallan/track-my-attendance/discussions)

---

## Disclaimer

This project is in active development. Features and functionalities are subject to change. Please refer to the [Roadmap](#roadmap) for upcoming changes and planned enhancements.

---

*This README was last updated on September 18, 2024.*
