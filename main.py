from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.database import engine
from src.model.index import metadata
from src.routes import routes

metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in routes:
    app.include_router(route)
