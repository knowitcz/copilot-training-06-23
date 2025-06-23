from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db import SQLModel, engine
from app.api.account_routes import router as account_router
from app.startup import create_default_accounts

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

# Serve static files from /static
@app.get("/")
def serve_static_files():
    return StaticFiles(directory="app/static", html=True)

app.include_router(account_router, prefix="/api/v1", tags=["account"])

create_default_accounts()