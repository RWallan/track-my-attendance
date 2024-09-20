# Roadmap

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
