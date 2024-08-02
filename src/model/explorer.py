from pydantic import BaseModel, Field


class Explorer(BaseModel):
    name: str = Field(..., min_length=2)
    country: str = Field(..., min_length=2)
    description: str
