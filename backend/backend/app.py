from fastapi import FastAPI

from backend.routes import auth, users

app = FastAPI()


@app.get('/health_check')
def health_check():
    return {'status': 'OK'}


app.include_router(users.router, tags=['users'])
app.include_router(auth.router, tags=['auth'])
