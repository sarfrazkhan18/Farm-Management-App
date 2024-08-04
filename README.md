     # Farm Management App

This is a web-based farm management application built with Python and Flask. It helps farmers manage their crops, tasks, cows, and milk production records.

## Features

- Crop Management: Add and view crop information
- Task Tracking: Create and monitor farm tasks
- Cow Inventory: Maintain a record of cows
- Milk Production: Track milk production for each cow

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/farm-management-app.git
   cd farm-management-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python
   >>> from database import init_db
   >>> init_db()
   >>> exit()
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open a web browser and go to `http://127.0.0.1:5000/`

## Project Structure


├── app.py (Main Flask application)
├── database.py (Database operations)
├── requirements.txt (Project dependencies)
├── README.md (This file)
│
├── templates/ (HTML templates)
│ ├── layout.html
│ ├── index.html
│ ├── crops.html
│ ├── tasks.html
│ ├── cows.html
│ └── milk_production.html
│
└── static/
└── css/
└── style.css
