from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Aporte",
    description=(
        "Plataforma local de análise e comparação de investimentos."
    ),
    version="0.1.0",
)

app.include_router(router, prefix="/api/v1")
