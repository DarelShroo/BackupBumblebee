from fastapi import FastAPI
from Controller import searchController, webSocketController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", 
                   "http://192.168.1.137:8080", 
                   "http://192.168.1.142:8080",  
                   "http://192.168.1.137:8000", 
                   "http://192.168.1.142:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(searchController.router)
app.include_router(webSocketController.router)