from fastapi import Body, FastAPI, Header, Response

app = FastAPI()


@app.get("/hi")
def greet():
    return "Hello? World!"


@app.get("/hi/{who}")
def path_greet(who):
    return f"Hello {who}?"


@app.get("/hii")
def query_greet(who):
    return f"Hello {who}!"


@app.post("/hi")
def body_greet(who: str = Body(embed=True)):
    return f"Hello? {who}"


@app.get("/hhi")
def header_greet(who: str = Header()):
    return f"Hello? {who}"


@app.get("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent


@app.get("/happy", status_code=202)
def happy():
    return ":)"


@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"
