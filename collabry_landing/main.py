import fastapi
from collabry_landing.router import router
from collabry_landing.database import db_create_email_table


app = fastapi.FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await db_create_email_table()
