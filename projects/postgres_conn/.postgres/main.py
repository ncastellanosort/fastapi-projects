from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import SQLModel, Field, create_engine, Relationship, Session, select
from typing import Optional, List, Annotated

'''

driver

pip install psycopg2-binary

postgresql://<username>:<password>@localhost:<postgresql_port>/<database_name>

'''


URL_DATABASE = 'postgresql://postgres:root@localhost:5432/fastapi_conn'
engine = create_engine(URL_DATABASE)

app = FastAPI()


class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30)


class AuthorUpdate(SQLModel):
    id: Optional[int] = None
    name: str = None


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str
    author_id: int = Field(foreign_key="author.id")


# create tables on startup
@app.on_event("startup")
def create_db_tables():
    SQLModel.metadata.create_all(engine)

# session dependency


def get_db_session():
    with Session(engine) as session:
        yield session


# create author
@app.post('/create_author')
def create_author(author: Author, session: Session = Depends(get_db_session)):
    session.add(author)
    session.commit()
    session.refresh(author)
    author_data = jsonable_encoder(author)
    return JSONResponse(content=author_data, status_code=status.HTTP_200_OK)

# get authors


@app.get('/get_authors')
def get_authors(session: Session = Depends(get_db_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    authors = session.exec(select(Author).offset(offset).limit(limit)).all()
    return authors

# read one author


@app.get('/get_author/{id}')
def get_author(id: int, session: Session = Depends(get_db_session)):
    author = session.get(Author, id)
    if not author:
        raise HTTPException(detail="author not found",
                            status_code=status.HTTP_404_NOT_FOUND)
    author_data = jsonable_encoder(author)
    return JSONResponse(content=author_data, status_code=status.HTTP_200_OK)

# delete author


@app.delete('/delete_author/{id}')
def delete_author(id: int, session: Session = Depends(get_db_session)):
    author = session.get(Author, id)
    if not author:
        raise HTTPException(detail="author not found",
                            status_code=status.HTTP_404_NOT_FOUND)
    session.delete(author)
    session.commit()
    author_data = jsonable_encoder(author)
    return JSONResponse(content={"author": author_data, "deleted": True}, status_code=status.HTTP_200_OK)

# partially update the author


@app.patch('/update/{id}', response_model=Author)
def update_author(author_id: int, author: AuthorUpdate, session: Session = Depends(get_db_session)):
    author_db = session.get(Author, author_id)
    if not author_db:
        raise HTTPException(detail="author not found",
                            status_code=status.HTTP_404_NOT_FOUND)

    author_data = author.model_dump(exclude_unset=True)

    author_db.sqlmodel_update(author_data)
    session.add(author_db)
    session.commit()
    session.refresh(author_db)
    author_data = jsonable_encoder(author_db)
    return JSONResponse(content=author_data, status_code=status.HTTP_200_OK)
