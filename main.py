from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()


@app.get('/health')
def health_check():
    return Response(status_code=200)
