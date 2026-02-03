from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from src.main.controllers.location_controller import router as location_router
from src.main.controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(location_router)
app.include_router(user_router)
