import asyncio
from fastapi import FastAPI


app = FastAPI()


@app.get("/hi")
async def greet():
    await asyncio.sleep(2)
    return "Hello? World?"
