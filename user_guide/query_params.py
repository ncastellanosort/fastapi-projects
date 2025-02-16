'''

- query params - http://127.0.0.1:8000/items/?skip=0&limit=10

when you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): <- skip and limit are the query params
   return fake_items_db[skip : skip + limit]

- optional parameters -

set them default with None

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
   if q:
      return {"item_id": item_id, "q": q}
   return {"item_id": item_id}

- multiple path and query parameters

can be declared at the same time and will be detected by name

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}") <- path params
async def read_user_item(
   user_id: int, item_id: str, q: str | None = None, short: bool = False <- query params
):
   item = {"item_id": item_id, "owner_id": user_id}
   if q:
      item.update({"q": q})
   if not short:
      item.update(
            {"description": "This is an amazing item that has a long description"}
      )
   return item

- required query params -

make a query param required only not declare any default value

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str): <- no default value
   item = {"item_id": item_id, "needy": needy}
   return item

'''