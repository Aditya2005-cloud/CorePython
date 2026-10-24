# Core Python Practice

A collection of Python exercises and small projects created while learning Python. The repository covers fundamentals such as variables, collections, loops, functions, modules, file handling, exceptions, and object-oriented programming.

## Projects

| Folder | Description |
| --- | --- |
| `AnimalZoo_basic-Python` | Basic object-oriented programming with animal classes |
| `expense_manager` | Small expense and budget management project |
| `File_Handling` | Practice with reading and writing files |
| `Library Management System` | Library and book management exercise |
| `Modules&Packages(learning File handling)` | Practice with Python modules and packages |
| `password_manager` | Command-line account manager using local JSON storage |
| `PracticeFolder_Python` | Small examples for importing and calling Python files |
| `RFC6238` | RFC 6238 / time-based one-time password experiments |
| `school_project_basic-PYTHON` | Basic school project using classes |
| `somthingNew` | Miscellaneous Python experiments |

The Python files in the repository root are short exercises and examples. Many can be run individually; some ask for input in the terminal.

## Requirements

- Python 3.10 or newer is recommended.
- Some projects may have their own dependencies. Check for a `requirements.txt` file inside that project before running it.

## Run an example

Clone the repository, open a terminal in the project folder, and run a Python file:

```bash
git clone <your-repository-url>
cd CorePython
python day1_cal.py
```

On Windows, use `py` if `python` is not available:

```powershell
py day1_cal.py
```

For example, to start the password manager:

```bash
cd password_manager
python main.py
```

The password manager currently stores passwords as plain text in its local JSON file. Do not use it to store real credentials.

## Repository notes

- These projects are learning exercises and may have different levels of completion.
- Run each project from its own folder when it relies on local files or modules.
- Generated Python cache files and virtual environments are excluded through `.gitignore`.
