from pydantic import BaseModel, Field


class Creature(BaseModel):
    name: str = Field(..., min_length=2)
    country: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description="ISO two-character code",
    )
    area: str
    description: str
    aka: str
