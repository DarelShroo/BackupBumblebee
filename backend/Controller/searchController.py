from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List,  Dict
from Model.Search import Search

router = APIRouter()

@router.post('/search')
async def file_user_search(search_data: Search):
    file_name = search_data.file_name
    folders = search_data.folders
    return search_data

@router.post('/search/file')
async def oneFileToFind(search_data: Dict[str, str]):
    file_name = search_data.get("file_name")
    type = search_data.get("type")
    return {"search_data": search_data}

@router.post('/search/type')
async def typesFileToFind(type_files: Dict):
    return type_files

@router.get('/search/all')
async def file_user_search():
    return "all"

@router.post('/search/folders')
async def foldersToSearch(list_folders_to_search: List[str]):
    return ""

@router.post('/search/app')
async def appFilesSearch(list_app_to_search: List[str]):
    return list_app_to_search
