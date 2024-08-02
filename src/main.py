from fastapi import FastAPI

from src.web import explorer
from src.web import creature


app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)


@app.get("/")
def top():
    return "top here"


@app.get("/echo/{thing}")
def echoing(thing):
    return f"echoing {thing}"
