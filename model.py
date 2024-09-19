from typing import Optional
from pydantic import BaseModel

class Coraline(BaseModel):

    id: Optional [int] = None
    nome: str
    Interpretador: str
    Parentesco: str
    
