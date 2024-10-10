"""Main module."""
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse

# Base de datos
from config.database import database as connection
from routes.user_route import user_router
from contextlib import asynccontextmanager
from helpers.api_key_auth import get_api_key


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(
    title="Receipt Master",
    version="1.0",
    contact={"name": "Juan Pablo Acosta Y Alejandro Valencia",
             "url": "https://github.com/JPablo67",
             "email": "juanpa.995@gmail.com"},
    description="Receipt Master es una API que permite a los usuarios administrar sus recibos de forma eficiente.",


    
)


@app.get("/")
def read_root():
    """
    Redirects to the Swagger UI documentation.
    """
    return RedirectResponse(url="/docs")


app.include_router(
    user_router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_api_key)],
)
