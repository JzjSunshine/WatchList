"""
create app
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


from .v1 import v1

app = FastAPI()

app.include_router(v1,prefix="/api")

