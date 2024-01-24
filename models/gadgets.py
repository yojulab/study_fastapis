from typing import List, Optional

from fastapi import Form
from pydantic import BaseModel, EmailStr
from typing import Optional

class Gadget(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
