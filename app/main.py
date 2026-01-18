from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.graph.incident_graph import incident_graph

app = FastAPI(title="Self-Healing Agentic RAG")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/incident")
async def incident(payload: dict):
    result = incident_graph.invoke(payload)
    return {"status": "processed", "result": result}
