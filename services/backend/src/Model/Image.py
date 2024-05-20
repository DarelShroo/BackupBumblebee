from PIL import Image as PILImage
from typing import Union
from pydantic import BaseModel

class Image(BaseModel):
    file: PILImage
    categories: Union[str, tuple]
