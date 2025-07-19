### ✅ app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import wheel_specifications, bogie_checksheet
from .database import Base, engine

# Drop all tables (for fresh DB setup in development)
# Base.metadata.drop_all(bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace '*' with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(wheel_specifications.router)
app.include_router(bogie_checksheet.router)
