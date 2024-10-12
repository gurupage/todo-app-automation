# React ToDo App Test Automation

This project is an automation test of a Todo application built with React, using Python and Playwright.
The purpose is to improve my test automation skills and include it in my portfolio.

## Main Tests
- **Add ToDo:** Add a new task to the list.
- **Confirm ToDo Added:** Verify that the new task appears in the list.
- **Mark ToDo as Completed:** Change the status of a task to completed and confirm the change.
- **Delete ToDo:** Remove a task from the list and ensure it no longer appears.

## Technologies Used
- **React** - Front-end library
- **JavaScript (ES6)** - Programming language
- **Python 3.9.1** - Test scripting language
- **pytest** - Testing framework for Python
- **Playwright** - Test automation framework
- **Node.js** - JavaScript runtime environment

## Prerequisites
- Node.js installed
- Python 3.9.1 installed
- Git installed

## Detailed Test Procedures

### Set Up The Test Environment 

**Cloning the Repository**
```powershell
git clone https://github.com/your-username/todo-app-automation.git
cd todo-app-automation
```

**Install Dependencies**
- **Front End(React)**
```powershell
cd react-todo-app
npm install
cd ..
```

- **Backend**
```powershell
cd tests
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install pytest playwright
playwright install
```

**Activate the App**
- **React App**
```powershell
cd react-todo-app
npm start
cd ..
```

**Confirm the Test Environment**
- Confirm to the playwright is installed and install the required browser
```powershell
cd tests
pip list
playwright show
playwright --version
```

### Test Execution
- Enter the command at root directory of the project
```powershell
cd C:\Users\User\todo-app-automation
.\venv\Scripts\Activate
Run the Tests
pytest
```