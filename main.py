import json
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def get():
    return FileResponse('index.html')


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    i = 1
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        data = json.loads(data)
        data['number'] = i
        i += 1
        await websocket.send_text(json.dumps(data))


if __name__ == "__main__":
    uvicorn.run(app)
