from fastapi import FastAPI
from db.postgres_conn import engine
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware
from routers.car_router import car_rt

app = FastAPI()

origins = ["http://localhost:3000/", "http://localhost:3000"]


@app.on_event("startup")
def create_tables():
    SQLModel.metadata.create_all(engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car_rt)
