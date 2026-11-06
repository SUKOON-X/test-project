from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def homepage():
    return {"message": "hello world"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)