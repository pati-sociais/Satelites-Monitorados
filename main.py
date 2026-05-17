from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from satellites import satellites

app = FastAPI()

# Libera acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "API de Monitoramento de Satélites"
    }

@app.get("/satellites")
def get_satellites():
    return satellites