
## Project Report

### Activities

- 4.a. In section 4a we had the task of creating a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed.

- 4.b. In Section 4b we had the task of creating a fuzz.py file that will automatically fuzz 5 Python methods. Additionally we reported any bugs encountered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions.

- 4.c. In section 4c we had the task of integrating foresics by modifying 5 Python methods. Below I will list the 5 modified methods.

    - **/FAME-ML/main.py** - susceptable to model tricking
        - getAllPythonFilesinRepo()
        - runFameMl()

    - **FAME-ML/lint_engine.py** - susceptable to poisoning attacks when data and models are loaded
        - getDataLoadCountb()
        - getDataLoadCountc()
        - getModelLoadCountb()

- 4.d. In section 4d we had the task of integrating continuous integration with GitHub Actions.

### Lessons Learned




