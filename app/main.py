from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import connect_db
from app.core.database import disconnect_db


# include routers from each module below
from app.modules.healthcheck.router import router as healthcheck_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to database
    await connect_db()

    yield
    # disconnect db connection when application shuts down
    await disconnect_db()


app = FastAPI(
    title="My API",
    lifespan=lifespan,
)

# app.include_router(auth_router)
app.include_router(healthcheck_router)