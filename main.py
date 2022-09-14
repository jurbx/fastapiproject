import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db.base import database
from endpoints import users, auth, products
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title='FastApiProject')
app.include_router(users.router, prefix='/api/users', tags=['users'])
app.include_router(auth.router, prefix='/api/auth', tags=['auth'])
app.include_router(products.router, prefix='/api/products', tags=['products'])

app.mount("/static", StaticFiles(directory="react/static"), name="static")

templates = Jinja2Templates(directory="react")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/{full_path:path}')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

