4a)	In 4a we had the task of creating a git hook that analyzes our security vulnerabilities and exports them to a csv file. To do this I navigated to .git/hooks directory on my local Repo and made a pre-commit file that uses bandit to accomplish the given task. With this assignment I learned how to use bandit and also how to use a hook to make changes to my repository. 

Refer to logs-screenshots.docx for our images.

4b)	In 4b I created a file that is called fuzz.py. This file fuzzes 5 files of my choosing in our repo and prints their output. This helps us look for bugs and ensures that everything is working as intended. This part of the workshop allowed me to learn more about python, fuzzing, and GitHub actions. In this workshop, one of the requirements was that I use GitHub actions to automatically run my fuzz.py file when a push is made to the repository. This was done with the fuzzer.yaml file that is in .github/workflows in our repository.


