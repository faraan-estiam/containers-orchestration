from uuid import uuid4
from fastapi import APIRouter
from classes.models import Item, ItemNoId

router = APIRouter(
  prefix="/items"
)

@router.get("/", response_model=list[Item])
async def get_items ():
  return []