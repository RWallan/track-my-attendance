# Track My Attendance

**Track My Attendance** is a platform designed to help students easily monitor their class attendance and predict trends in their presence across different subjects.

## Key Features

- **Simplicity First:** A streamlined user experience focused on easy attendance tracking.
- **User-Friendly:** Intuitive interface without unnecessary complexity—no overwhelming menus or buttons.
- **Minimalist Approach:** Offers only the essentials to keep your attendance organized and accessible.
- **Detailed Analytics:** Monitor your attendance trends.
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
