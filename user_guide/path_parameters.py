'''

- path parameters -

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
   return {"item_id": item_id}

the value of the path parameter item_id will be passed to your function as the argument item_id.

- parameters with types -

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int): -> int type
   return {"item_id": item_id}

- order matters -

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
   return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
   return {"user_id": user_id}

'''