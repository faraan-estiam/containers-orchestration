from fastapi import APIRouter
from app.classes.models import Item, ItemNoId
from app.database.db import connect

router = APIRouter(
  prefix="/items"
)

@router.get("/")
async def get_items ():
  conn = connect()
  cursor = conn.cursor()
  query = """
SELECT id, name, description
FROM items
"""
  cursor.execute(query)
  response = cursor.fetchall()
  conn.close()
  return (Item(id=id, name=name, description=description) for (id, name, description) in response)