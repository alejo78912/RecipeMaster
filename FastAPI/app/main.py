"""Main module for Receipt Master."""
from contextlib import asynccontextmanager  # Standard library import first
from fastapi import FastAPI, Depends  # Third-party imports second
from starlette.responses import RedirectResponse
from config.database import database as connection  # First-party imports last
from routes.user_route import user_router
from helpers.api_key_auth import get_api_key


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Lifespan function to handle the database connection.

    Args:
        _app (FastAPI): The FastAPI application instance (currently unused).
    """
    # Connect to the database if the connection is closed
    if connection.is_closed():
        connection.connect()
    try:
        yield  # The application runs here
    finally:
        # Close the connection when the application stops
        if not connection.is_closed():
            connection.close()


app = FastAPI(
    title="Receipt Master",
    version="1.0",
    contact={
        "name": "Juan Pablo Acosta Y Alejandro Valencia",
        "url": "https://github.com/JPablo67",
        "email": "juanpa.995@gmail.com"
    },
    description="Receipt Master es una API de recetas",
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
