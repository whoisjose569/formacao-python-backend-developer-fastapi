from fastapi import FastAPI, Request
from src.controllers import post
from src.controllers import auth
from contextlib import asynccontextmanager
from src.database import database, metadata, engine
from fastapi.responses import JSONResponse
from src.exceptions import NotFoudPostError
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        "name": "auth",
        "description": "Operações de autenticação",
    },
    {
        "name": "post",
        "description": "Operações de post",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

servers = [
    {"url": "https://stag.example.com", "description": "Staging environment"},
    {"url": "https://prod.example.com", "description": "Production environment"},
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts  # noqa

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(
    title="DioBlogApi", lifespan=lifespan, openapi_tags=tags_metadata, servers=servers
)

app.include_router(post.router, tags=["post"])
app.include_router(auth.router)


@app.exception_handler(NotFoudPostError)
async def not_found_post(request: Request, exc: NotFoudPostError):
    return JSONResponse(
        status_code=418,
        content={"message": f"Post not found"},
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allo_methods=["*"],
    allow_headers=["*"],
)
