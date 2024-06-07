from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app import models
from app.routers import flyer
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(flyer.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>PinDrop API</title>
        </head>
        <body>
            <h1>Welcome to the PinDrop API</h1>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content)
