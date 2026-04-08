from pydantic import BaseModel
from typing import List

class CommitSummary(BaseModel):
    message: str
    files: List[str]