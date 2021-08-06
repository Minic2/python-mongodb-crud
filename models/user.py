from pydantic import BaseModel

from typing import Optional
from pydantic.errors import EmailError

class User(BaseModel):

    id:Optional[str]
    name:str
    email:str
    password:str
