from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from models import IssueStatus, UserRole

class UserBase(BaseModel):
    first_name = str
    last_name = str
    emaill = EmailStr
    
class UserCreate(UserBase):
    role: UserRole = UserRole.guest
    password: Optional[str] = None
    
class UserOut(UserBase):
    id: int
    role: UserRole
    space_stamp: datetime
    
    class Config:
        orm_mode = True
        
class IssueBase(BaseModel):
    title: str
    description: str
    
class IssueCreate(IssueBase):
    reporter_id: int
    
class IssueOut(IssueBase):
    id: int
    status: IssueStatus
    created_at: datetime
    reporter: UserOut
    
    class Config:
        orm_mode = True
        