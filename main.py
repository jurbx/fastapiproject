import uvicorn
from fastapi import FastAPI
from db.base import database
from endpoints import users, auth, jobs

app = FastAPI(title='FastApiProject')
app.include_router(users.router, prefix='api/users', tags=['users'])
app.include_router(auth.router, prefix='api/auth', tags=['auth'])
app.include_router(jobs.router, prefix='api/job', tags=['job'])


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

