'''

type hints are used to specify the type of the variable, function arguments, and return type of the function.
help us to get auto-completion and type checking in the IDE.

'''

# Example

def get_full_name(first_name: str, last_name: str):
   full_name = first_name.title() + " " + last_name.title()
   return full_name

def get_name_with_age(name: str, age: int):
   name_with_age = name + " is this old: " + age
   return name_with_age

'''

simple types are:
int, bool, float, str

'''


'''

generic types

there are some data structures that can contain other values, like dict, list, set and tuple. 
And the internal values can have their own type too.

need to use the module called typing

'''

# list example

def process_items(items: list[str]):
   for item in items:
      print(item)

# tuple and set example

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
   return items_t, items_s

'''

items t has a tuple of 3 elements, the first two are integers and the last one is a string.
items s has a set of bytes.

'''

# dict example

def process_items(prices: dict[str, float]):
   for item_name, item_price in prices.items():
      print(item_name)
      print(item_price)

'''

the first one is the key and the second one is the value.

'''

'''

union

variable that can have more than one type.

'''

def process_item(item: int | str):
   print(item)

'''

item can be an integer or a string.

'''

'''

possibly None
variable that could have any type but it could be also None.

need to import Optional from typing

'''

from typing import Optional

from typing import Optional


def say_hi(name: Optional[str] = None):
   if name is not None:
      print(f"Hey {name}!")
   else:
      print("Hello World")

'''

using Union or Optional
better to use Union

'''

def say_hi(name: str | None):
   print(f"Hey {name}!")

'''

classes as types

'''

class Person:
   def __init__(self, name: str):
      self.name = name


def get_person_name(one_person: Person) -> str:
   return one_person.name

'''

Pydantic models
library to perform data validation and parsing using Python type hints.
first you declare a class with the atributtes and types, then you can use the class to validate the data.

'''

from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
   id: int
   name: str = "John Doe"
   signup_ts: datetime | None = None
   friends: list[int] = []


external_data = {
   "id": "123",
   "signup_ts": "2017-06-01 12:22",
   "friends": [1, "2", b"3"],
}

'''

the ** operator is used to unpack the dictionary into the constructor of the class.
takes the key-value pairs of the dictionary and passes them as arguments to the constructor.

'''

user = User(**external_data)
print(user)

'''

type hints with metadata
python doesn't do anythin with this metadata.
you can use it to provide fastapi more information about the type.

'''

from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
   return f"Hello {name}"