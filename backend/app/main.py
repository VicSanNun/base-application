from fastapi import FastAPI, Depends
from app.interfaces.api.routers.hello_router import router as hello_router
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_db
from sqlalchemy import text

app = FastAPI(title="FastAPI Clean Architecture Example")

# origins = [
#     "http://localhost:5173",  # frontend local (Vite)
#     "http://localhost:3000",  # frontend docker 
# ]

origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(hello_router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Clean Architecture!"}

@app.get("/db-check")
def db_check(db=Depends(get_db)):
    result = db.execute(text("SELECT 'Database connected!'"))
    return {"status": result.scalar()}
