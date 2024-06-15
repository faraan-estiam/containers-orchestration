from fastapi import FastAPI

#importing routers
import routers.router_items

#api init (launch with uvicorn main:api --reload)
api = FastAPI( 
  title="Watches API",
  redoc_url='/'
)

api.include_router(routers.router_items.router)