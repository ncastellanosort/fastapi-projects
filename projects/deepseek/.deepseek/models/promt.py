from sqlmodel import SQLModel, Field


class Prompt(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question: str = Field(default=None)
    answer: str = Field(default=None)
