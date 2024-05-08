from fastapi import FastAPI
import Controller
import Controller.searchController

app = FastAPI()

app.include_router(Controller.searchController.router)