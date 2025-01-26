from fastapi import FastAPI, Request, WebSocket

app = FastAPI()


@app.get("/")
async def root(request: Request):
    return {"status": 200}


@app.websocket("/connect")
async def device_connect(request: Request):
    return {}
