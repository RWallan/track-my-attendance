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
