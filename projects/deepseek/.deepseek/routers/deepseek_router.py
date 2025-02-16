from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select
from db.postgres_conn import get_db_session
from typing import Annotated
from models.promt import Prompt
from tools.deepseek import tell_deepseek

deepseek_rt = APIRouter(prefix='/deepseek')

@deepseek_rt.get('/')
def get_prompts(session: Session = Depends(get_db_session), offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    prompts = session.exec(select(Prompt).offset(offset).limit(limit)).all()
    return prompts

@deepseek_rt.post('/post')
def send_prompt(prompt: Prompt, session: Session = Depends(get_db_session)):
    user_question = prompt.question + ", en espanol"

    res = tell_deepseek(user_question)
    prompt.answer = res
    
    session.add(prompt)
    session.commit()
    session.refresh(prompt)
    prompt_data = jsonable_encoder(prompt)
    
    return JSONResponse(content=prompt_data, status_code=status.HTTP_201_CREATED)

deepseek_rt.get('/greeting')
def greeting():
    return JSONResponse(content="Good morning", status_code = status.HTTP_200_OK)
