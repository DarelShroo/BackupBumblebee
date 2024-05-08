from pydantic import BaseModel
from typing import Dict

class WhatsApp(BaseModel):
    folder_routes: Dict[str, list]