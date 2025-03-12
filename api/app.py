from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


from api.modules import router
from api.config import APP_NAME, APP_DESCRIPTION
from api.database import create_db_and_tables, add_initial_data
import anyio


@asynccontextmanager
async def lifespan(app: FastAPI):
    await anyio.to_thread.run_sync(create_db_and_tables)
    await anyio.to_thread.run_sync(add_initial_data)
    yield


app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    docs_url='/',
    redoc_url=None,
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=404, content={'detail': 'Resource not found'})


app.include_router(router)
