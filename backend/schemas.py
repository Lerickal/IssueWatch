from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime, timedelta
from models import IssueStatus, UserRole

class UserBase(BaseModel):
    first_name: str
    last_name: str
    emaill: EmailStr
    
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
    reporter_id: Optional[int] = None
    
class IssueOut(IssueBase):
    id: int
    status: IssueStatus
    created_at: datetime
    reporter: UserOut
    assigned_to: Optional[UserOut] = None
    
    class Config:
        orm_mode = True
        
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class TokenData(BaseModel):
    emaill: str | None = None
    
class GuestIssueCreate(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    emaill: EmailStr
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    
    @validator('*', pre=True, always=True)
    def not_empty(cls, v):
        if isinstance(v, str) and not v.strip():
            raise ValueError("Field cannot be empty or whitespace")
        
        return v
    
