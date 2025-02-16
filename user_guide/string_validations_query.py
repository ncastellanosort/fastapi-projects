'''

- string validations for query params -

declare additional info or validation for the params

- additional validation -

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None): <- use of Annotated
   results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
   if q:
      results.update({"q": q})
   return results

Query(max_length=50, max_length=50) is telling fastapi that now it must have an extra validation

- query parameter list -

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
   query_items = {"q": q}
   return query_items

'''
