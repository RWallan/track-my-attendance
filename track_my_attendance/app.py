from fastapi import FastAPI

from track_my_attendance.courses import router as courses_router

app = FastAPI()


@app.get('/health_check')
def health_check():
    return {'status': 'OK'}


app.include_router(courses_router)
