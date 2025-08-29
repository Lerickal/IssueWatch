from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base
import enum

class UserRole(str, enum.Enum):
    guest = "guest"
    support = "support"
    
class IssueStatus(str, enum.Enum):
    open = "Open"
    in_progress = "In Progress"
    closed = "Closed"
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(99), nullable=False)
    last_name = Column(String(99), nullable=False)
    emaill = Column(String(222), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.guest)
    password = Column(String(222), nullable=True)
    space_stamp = Column(TIMESTAMP, server_default=func.now())
    
    issues = relationship("Issue", back_populates="reporter")
    
class Issue(Base):
    __tablename__ = "issues"
    
    id = Column(Integer, primary_key=True, index=True)
    reporter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(222), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(IssueStatus), nullable=False, default=IssueStatus.open)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    assigned_to_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    reporter = relationship("User", back_populates="issues")
    
    assigned_to = relationship("User", foreign_keys=[assigned_to_id])
    