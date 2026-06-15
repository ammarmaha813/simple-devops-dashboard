from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


APP_NAME = "DevOps Dashboard"
APP_VERSION = "1.0.0"
APP_STATUS = "healthy"

app = FastAPI(title=APP_NAME, version=APP_VERSION)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


def current_datetime() -> datetime:
    return datetime.now().astimezone()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    now = current_datetime()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": APP_NAME,
            "version": APP_VERSION,
            "status": APP_STATUS,
            "current_time": now.strftime("%H:%M:%S"),
            "current_date": now.strftime("%A, %B %d, %Y"),
        },
    )


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": APP_STATUS}


@app.get("/api/info")
async def info() -> dict[str, str]:
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "status": APP_STATUS,
    }


@app.get("/api/time")
async def server_time() -> dict[str, str]:
    return {"time": current_datetime().strftime("%H:%M:%S")}
