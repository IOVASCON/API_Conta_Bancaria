from fastapi import FastAPI
from app.controllers import account, auth, transaction
from app.database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(auth.router, prefix="/auth")
app.include_router(account.router, prefix="/accounts")
app.include_router(transaction.router, prefix="/transactions")
