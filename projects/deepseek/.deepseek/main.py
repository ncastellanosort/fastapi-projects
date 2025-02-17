from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.postgres_conn import engine
from sqlmodel import SQLModel
from routers.deepseek_router import deepseek_rt

app = FastAPI()

origins = ['http://localhost:3000/', 'http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # any response that should be accessible by the browser
    expose_headers=['X-token-auth', 'X-token-login']
)

@app.on_event('startup')
def create_tables():
    SQLModel.metadata.create_all(engine)


app.include_router(deepseek_rt)
    
