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
