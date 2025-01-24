from pydantic import BaseModel
# from typing import List


class Task(BaseModel):
    id: int
    name: str
