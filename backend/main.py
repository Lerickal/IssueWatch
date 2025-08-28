from fastapi import FastAPI
from database import engine, Base
from routers import issues, users

app = FastAPI(title="IssueWatch API")

Base.metadata.create_all(bind=engine)

app.include_router(issues.router, prefix="/api", tags=["Issues"])
app.include_router(users.router, prefix="/api", tags=["Users"])
