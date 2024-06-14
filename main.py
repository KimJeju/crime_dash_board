import gunicorn
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# 컨트롤 라우터 선언
from branch_crime_app import branch_crime_router 

# #cors url
# origins = [
#     CORSMiddleware,
#     "http://localhost",
#     "http://localhost/",
#     "http://localhost:5173",
#     "http://127.0.0.1/",

# ]


app = FastAPI()
app.include_router(branch_crime_router.router)

#cors settings
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get('/')
def home():
    return {'app' : 'main'}

if __name__ == "__main__":
    gunicorn.run("main:app", host='0.0.0.0', port=8892, reload=True)


