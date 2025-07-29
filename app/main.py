from fastapi import FastAPI, Depends, Query, HTTPException
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import User
from .schemas import UserOut
from .database import get_async_session

app = FastAPI()

@app.get("/users", response_model=List[UserOut])
async def list_users(
    role: Optional[str] = Query(None, description="Filter by user role"),
    status: Optional[str] = Query(None, description="Filter by user status"),
    session: AsyncSession = Depends(get_async_session),
):
    query = select(User)
    if role:
        query = query.where(User.role == role)
    if status:
        query = query.where(User.status == status)
    result = await session.execute(query)
    users = result.scalars().all()
    return users
