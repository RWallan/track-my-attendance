# Roadmap

Planned features and enhancements include:

> This may change.

- [ ] **Database Modeling:** Introduce Presented Modeling
- [ ] **Base CRUD:** Implement all routes provided
- [ ] **Mobile Application:** Develop mobile apps for iOS and Android platforms.
- [ ] **Notifications:** Implement email and push notifications for attendance alerts.
- [ ] **Advanced Analytics:** Provide detailed analytics based on attendance data.
- [ ] **Multi-Language Support:** Expand accessibility by supporting multiple languages.

## Planned Routes (WIP)

## 1. Authentication

- [ ] **POST** `/auth/register`
  - **Description:** Registers a new user.

- [ ] **POST** `/auth/login`
  - **Description:** Authenticates a user and returns an access token.

- [ ] **POST** `/auth/refresh`
  - **Description:** Refreshes the access token using a refresh token.

---

## 2. Students

- [ ] **GET** `/students/me`
  - **Description:** Retrieves details about logged user

- [ ] **POST** `/students`
  - **Description:** Creates a new student record.

- [ ] **PUT** `/students/me`
  - **Description:** Updates information for a specific student.

- [ ] **DELETE** `/students/me`
  - **Description:** Deletes a specific student record.

---

## 4. Courses

- [ ] **GET** `/courses`
  - **Description:** Retrieves a list of all courses.

- [ ] **GET** `/courses/{course_id}`
  - **Description:** Retrieves details of a specific course.

- [ ] **POST** `/courses`
  - **Description:** Creates a new course.

- [ ] **PUT** `/courses/{course_id}`
  - **Description:** Updates a specific course.

- [ ] **DELETE** `/courses/{course_id}`
  - **Description:** Deletes a specific course.

- [ ] **GET** `/courses/{course_id}/modules`
  - **Description:** Retrieves all modules associated with a specific course.

---

## 5. Course Modules

- [ ] **GET** `/modules`
  - **Description:** Retrieves a list of all modules.

- [ ] **GET** `/modules/{module_id}`
  - **Description:** Retrieves details of a specific module.

- [ ] **POST** `/modules`
  - **Description:** Creates a new module.

- [ ] **PUT** `/modules/{module_id}`
  - **Description:** Updates a specific module.

- [ ] **DELETE** `/modules/{module_id}`
  - **Description:** Deletes a specific module.

- [ ] **GET** `/modules/{module_id}/agenda`
  - **Description:** Retrieves all agenda items associated with a specific module.

---

## 6. Course Agenda

- [ ] **GET** `/agenda`
  - **Description:** Retrieves a list of all course agendas.

- [ ] **GET** `/agenda/{agenda_id}`
  - **Description:** Retrieves details of a specific agenda item.

- [ ] **POST** `/agenda`
  - **Description:** Creates a new agenda item.

- [ ] **PUT** `/agenda/{agenda_id}`
  - **Description:** Updates a specific agenda item.

- [ ] **DELETE** `/agenda/{agenda_id}`
  - **Description:** Deletes a specific agenda item.

---

## 7. Student Agenda

- [ ] **GET** `/students/{student_id}/agenda`
  - **Description:** Retrieves all agenda items a specific student is enrolled in.

- [ ] **POST** `/students/{student_id}/agenda`
  - **Description:** Enrolls a student in an agenda item.

- [ ] **DELETE** `/students/{student_id}/agenda/{agenda_id}`
  - **Description:** Removes a student from a specific agenda item.

---

## 8. Presence History

- [ ] **GET** `/attendance`
  - **Description:** Retrieves paginated attendance records.

- [ ] **GET** `/students/{student_id}/attendance`
  - **Description:** Retrieves paginated attendance records for a specific student.

- [ ] **POST** `/attendance`
  - **Description:** Records attendance for a student in a specific agenda item.

- [ ] **PUT** `/attendance/{attendance_id}`
  - **Description:** Updates a specific attendance record.

- [ ] **DELETE** `/attendance/{attendance_id}`
  - **Description:** Deletes a specific attendance record.

---

## 9. Presence Lessons Count History

- [ ] **GET** `/students/{student_id}/attendance-summary`
  - **Description:** Retrieves the attendance summary for a specific student.
  - **Request Body:** None

- [ ] **GET** `/agenda/{agenda_id}/attendance-summary`
  - **Description:** Retrieves attendance summaries for all students in a specific agenda.
  - **Request Body:** None


---

## 11. Reports and Analytics

- [ ] **GET** `/reports/students/{student_id}/attendance`
  - **Description:** Generates an attendance report for a specific student.

- [ ] **GET** `/reports/courses/{course_id}/attendance`
  - **Description:** Generates an attendance report for a specific course.

- [ ] **GET** `/reports/attendance/trends`
  - **Description:** Provides analytics on overall attendance trends.

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

- [ ]  **Phase 5: Reporting and Analytics**
   - Develop reporting endpoints for attendance summaries and trends.

- [ ]  **Phase 7: Testing and Documentation**
   - Write unit and integration tests for all endpoints.
   - Document all APIs using Swagger or similar tools.
