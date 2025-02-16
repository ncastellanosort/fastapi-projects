'''

used to isolate the dependencies of the project from the system dependencies.

1. create a directory for your project.

2. create a virtual environment in the directory with:
   python -m venv <.name_of_the_virtual_environment>

3. activate the virtual environment with:
   .<name_of_the_virtual_environment>\Scripts\Activate.ps1

4. check if the virtual enviroment is active:
   Get-Command Python
if it shows the python path from the virtual environment, it's active.

5. upgrade pip:
   python -m pip install --upgrade pip

6. add .gitignore:
   echo "*" > .<name_of_the_virtual_environment>/.gitignore

7. start installing packages

8. deactivate the virtual enviroment:
   deactivate

'''