from fastapi import FastAPI
from app.routers.menu import router as menu_router

app = FastAPI(title="WAD Individu API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(menu_router)