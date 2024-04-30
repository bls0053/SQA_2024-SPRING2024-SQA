
## Project Report

### Activities and Lessons Learned

- 4.a. In 4a we had the task of creating a git hook that analyzes our security vulnerabilities and exports them to a csv file. To do this I navigated to .git/hooks directory on my local Repo and made a pre-commit file that uses bandit to accomplish the given task. With this assignment I learned how to use bandit and also how to use a hook to make changes to my repository.

> Refer to logs-screenshots.docx for our images.

- 4.b. In 4b I created a file that is called fuzz.py. This file fuzzes 5 files of my choosing in our repo and prints their output. This helps us look for bugs and ensures that everything is working as intended. This part of the workshop allowed me to learn more about python, fuzzing, and GitHub actions. In this workshop, one of the requirements was that I use GitHub actions to automatically run my fuzz.py file when a push is made to the repository. This was done with the fuzzer.yaml file that is in .github/workflows in our repository.

- 4.c. In section 4c we had the task of integrating foresics by modifying 5 Python methods. Below I will list the 5 modified methods. This part of the workshop allowed me to gain further insight into why certain files should be logged to prevent certain machine learning oriented attacks.

    - **/FAME-ML/main.py** - susceptable to model tricking
        - getAllPythonFilesinRepo()
        - runFameMl()

    - **FAME-ML/lint_engine.py** - susceptable to poisoning attacks when data and models are loaded
        - getDataLoadCountb()
        - getDataLoadCountc()
        - getModelLoadCountb()

- 4.d. In section 4d we had the task of integrating continuous integration with GitHub Actions. To do this, I added the codacity-analysis.yaml file into the .github/workflows directory so that the GitHub Action:
    
    - Analyzes each commit/pull request by running all supported static code analysis tools for each language used in this repo
    - Prints the analysis onto the console
    - Fails the workflow if it finds 1 or more issues in the code

This uses the default settings for codacity to achieve continuous integration and ensure that the code stays error free as it is being developed.






