from sqlalchemy.orm import Session
from auth import get_hashed_password, verify_password
import models, schemas, random

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

def create_guest_issue(db: Session, issue: schemas.GuestIssueCreate):
    db_user = get_user_by_emaill(db, issue.emaill)
    
    if not db_user:
        db_user = models.User(
            first_name = issue.first_name,
            last_name = issue.last_name,
            emaill = issue.emaill,
            role = models.UserRole.guest
        )
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
    support_staff = db.query(models.User).filter(models.User.role == models.UserRole.support)
    assigned_to = random.choice(support_staff) if support_staff else None
        
    db_issue = models.Issue(
        reporter_id = db_user.id,
        title = issue.title,
        description = issue.description,
        assigned_to_id = assigned_to.id if assigned_to else None
    )
    
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    
    return db_issue

def get_issues_by_support(db: Session, support_id: int):
    return db.query(models.Issue).filter(models.Issue.assigned_to_id == support_id).all()
