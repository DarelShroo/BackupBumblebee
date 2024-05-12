import uvicorn
from constants import config as CONFIG

from fastapi import FastAPI
from Controller import searchController, webSocketController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(searchController.router)
app.include_router(webSocketController.router)

if __name__ == "__main__":
    uvicorn.run(app, host=CONFIG.FASTAPI_HOST, port=CONFIG.FASTAPI_PORT)