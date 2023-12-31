from fastapi import FastAPI
from routes.items import router as items_router


app = FastAPI()


app.include_router(
    routes=items_router,
    prefix='/items',
)