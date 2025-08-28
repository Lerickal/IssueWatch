from sqlalchemy.orm import Session
from auth import get_hashed_password
import models, schemas

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_emaill(db: Session, emaill: str):
    return db.query(models.User).filter(models.User.emaill == emaill).first()

def create_user(db: Session, user: schemas.UserCreate):
    user_data = user.dict()
    if user_data.get("password"):
        user_data["password"] = get_hashed_password(user.password)
        
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_issues(db: Session):
    return db.query(models.Issue).all()

def create_issue(db: Session, issue: schemas.IssueCreate):
    db_issue = models.Issue(**issue.dict())
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

def update_issue_status(db: Session, issue_id: int, status: models.IssueStatus):
    issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if issue:
        issue.status = status
        db.commit()
        db.refresh(issue)
    return issue
