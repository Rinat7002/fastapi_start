from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database deleted")
    await create_tables()
    print("Database created")
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)







