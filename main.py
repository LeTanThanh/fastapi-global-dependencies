from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import Depends

from typing import Annotated

# Global Dependencies
async def verify_token(x_token: Annotated[str, Header()]):
  if x_token != "":
    raise HTTPException(
      status_code = 400,
      detail = "X-Token header invalid"
    )

async def verify_key(x_key: Annotated[str, Header()]):
  if x_key != "":
    raise HTTPException(
      status_code = 400,
      detail = "X-Key header invalid"
    )

app = FastAPI(
  dependencies = [
    Depends(verify_token),
    Depends(verify_key)
  ]
)

@app.get("/items")
async def read_items():
  return [
    {"item": "Portal Gun"},
    {"item": "Plumbus"}
  ]
