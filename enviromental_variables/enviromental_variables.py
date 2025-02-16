'''

is a variable that live outside python.
it lives in the os and could be read by python.

useful to store or handle application secrets.

to create an enviromental variable in windows:
   $Env:MY_NAME = "Wade Wilson"

'''

# To read the env variables in python
import os

name = os.getenv("MY_NAME", "World") # the second argument is the default
print(f"Hello {name} from Python")