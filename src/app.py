from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck() -> dict[str, str]:
    now = datetime.now().strftime("%H:%M:%S")
    return {"message": f"hello the time is {now}"}
