from pydantic import BaseModel, EmailStr
from typing import Optional, Union

class User(BaseModel):
    username: Optional[str] = None 
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    password: str
    otp: Optional[str] = None
