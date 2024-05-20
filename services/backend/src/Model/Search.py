from typing import List, Dict, Union, Tuple
from datetime import datetime
from pydantic import BaseModel

class Search(BaseModel):
   file_name: str
   category: Tuple
   app: List
   folders: List
   size: Dict
   date: Union[datetime, str]
       