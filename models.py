from sqlmodel import SQLModel, Field
from typing import Optional

class Card(SQLModel, table=True):
    id: Optional[int] = Field(index=True, default=None, primary_key=True) 
    category: str
    question: str
    response1: str
    response2: str
    response3: str
    response4: str
    correct: str
    seen: str
