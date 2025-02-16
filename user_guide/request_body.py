'''

- request body -

request body is a data sent by the client to the api [client -> server]

- response body -

response body is the data the api sends to the client [server -> client]

the api almost always has to send a response body, but the client does not

to declare a request body, use pydantic


from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel): <- data model
   name: str
   description: str | None = None
   price: float
   tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item): <- declared as a parameter
   return item




'''