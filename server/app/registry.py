from app.config.settings import SETTINGS
from app.database import create_tables


async def lifespan(_):
    yield
    print("shutdown")
