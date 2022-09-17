from fastapi import FastAPI

app = FastAPI()

@app.get("/consumer")
async def event():
    return {"message": "Hello World"}
