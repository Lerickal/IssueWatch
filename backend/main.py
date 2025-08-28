from fastapi import FastAPI
from database import engine, Base
from routers import issues

app = FastAPI(title="IssueWatch API")

Base.metadata.create_all(bind=engine)

app.include_router(issues.router, prefix="/api", tags=["Issues"])
