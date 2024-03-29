import uvicorn

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.item import router as item
from app.routes.category import router as category
from app.routes.blog import router as blog
from app.routes.healthcheck import healthcheck_router as healthcheck
from app.registry import lifespan

app = FastAPI()

app = FastAPI(lifespan=lifespan, docs_url="/api/docs", redoc_url=None)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

v1_router = APIRouter()
v1_router.include_router(prefix="/item", router=item, tags=['Item'])
v1_router.include_router(prefix="/category", router=category, tags=['Category'])
v1_router.include_router(prefix="/blog", router=blog, tags=['Blog'])

app.include_router(v1_router, prefix='/v1')


health_check_router = APIRouter()
health_check_router.include_router(
    prefix="/healthcheck", router=healthcheck, tags=["Health check"]
)
app.include_router(health_check_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
