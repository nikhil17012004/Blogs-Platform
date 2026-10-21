from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config import settings

# Connection to database
engine = create_async_engine(settings.database_url)

# Creates a async db session. A session is basically a transaction with a db. Each request gets its own session
AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


# This provides session to our routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
