from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from Service .ConnectionService import ConnectionService

router = APIRouter()
manager = ConnectionService()

@router.websocket("/server")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Received:{data}",websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.send_personal_message("Bye!!!",websocket)