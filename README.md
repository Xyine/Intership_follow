# Internship Follow

## Overview
**Internship Follow** is a Python-based project designed to help track internship research and tasks efficiently. It provides features like task logging, statistical visualization, and more, helping users stay organized and monitor their progress effectively.

---

## Features
- Log tasks with descriptions, deadlines, and completion status.
- Generate visual statistics (e.g., charts) for:
  - Task progress
  - Categories of tasks
  - Time allocation
- User-friendly command-line interface (CLI).
- Modular code structure for easy extension and maintenance.

---

## Project Structure
```plaintext
Intership_follow/
├── README.md
├── src/                     # Source code
│   ├── __init__.py 
│   ├── backend/             # Backend related code
│   │   ├── __init__.py      
│   │   ├── main.py          # FastAPI application (API routes)
│   │   ├── models.py        # Data models (e.g., Task)
│   │   ├── database.py      # Functions to interact with database (e.g., add_task, get_tasks)
│   ├── frontend/            # Frontend related code (PyQt/PySide)
│   │   ├── __init__.py
│   │   ├── main.py          # PyQt/PySide window for user interface
│   │   ├── pages.py         # Different pages for navigation
├── .gitignore               # Files and folders to ignore in git
├── requirements.txt         # List of dependencies for the project
└── README.md                # Project documentation 

```

---

## Requirements

    Python 3.8 or higher
    Dependencies listed in requirements.txt

---

## Installation

Follow these steps to set up and run the project:

  1. Clone the repository:

    git clone https://github.com/your-username/Intership_follow.git
    cd Intership_follow

  2. Set up a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

  3. Install dependencies:

    pip install -r requirements.txt

---

## Usage

  1. Run the application:

    python src/main.py

  2. Follow the prompts to:
       - Add tasks
       - View statistics
       - Export logs

---

## Contributing

Contributions are welcome! To contribute:

  1. Fork the repository.
  2. Create a new branch for your feature or bug fix:

    git checkout -b feature-name

  3. Commit your changes:

    git commit -m "Add feature description"

  4. Push to your branch:

    git push origin feature-name

  5. Open a pull request.
