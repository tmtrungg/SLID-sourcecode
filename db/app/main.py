import os
from dotenv import load_dotenv

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1 import api_v1_routers

from logging import INFO, Formatter, getLogger, StreamHandler

from app.db import *

# Load environment variables
load_dotenv()

Base.metadata.create_all(bind=engine)


logger = getLogger('app')
logger.setLevel(INFO)
handler = StreamHandler()
formatter = Formatter("%(msg)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        if request.url.path == "/":
            # Redirect to /docs
            return RedirectResponse(url="/docs", status_code=302)
        response = await call_next(request)
        
    except Exception as e:
        logger.exception(e)
        response = Response(content="Internal server error", status_code=500)
    finally:
        request.state.db.close()
    return response


@app.get("/", include_in_schema=False)
async def root():
    return {"messages": "Root URL of the API"}


app.include_router(api_v1_routers)
