import gunicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 컨트롤 라우터 선언
from branch_crime_app import branch_crime_router 

#cors url
origins = [
    CORSMiddleware,
    "*",
    "http://localhost:5173",
    "https://crime-dash-board-client-deploy:80",
    "https://crime-dash-board-client-deploy:80/",
    "http://175.121.69.41:5173/",
    "https://www.crimedash.kr",
    "https://www.crimedash.kr/",
]

## docs 설명란
description = """
안녕하세요, 해당 페이지는 국내 범죄통계 대시보드 Api 문서입니다.

## 제공내용
현재는 **2023년 1~4 분기** ~ **2024년 1분기** 경찰청 분기별 범죄발생 통계에 대한 데이터만 제공하고 있습니다 .
향 후 지속적 업데이트 예정입니다.

## API 파라미터

**year** :  </br>
&nbsp; &nbsp; ■ 2024 </br>
&nbsp; &nbsp; ■ 2023

**branch** :  
&nbsp; &nbsp; ■ 2024년 : 1, <br/>
&nbsp; &nbsp; ■ 2023년 : 1,2,3,4  <br/>

**category** :  
&nbsp; &nbsp; ■ average  <br/>
&nbsp; &nbsp; ■ main <br/>
&nbsp; &nbsp; ■ sub <br/>

**subject** :  
&nbsp; &nbsp; ■ 발생건수 <br/>
&nbsp; &nbsp; ■ 검거인원 <br/>
&nbsp; &nbsp; ■ 발생대비 검거건수 <br/>
&nbsp; &nbsp; ■ 검거인원 <br/>
&nbsp; &nbsp; ■ 법인체 <br/>



"""

app = FastAPI(
    title="국내 범죄통계 API",
    description=description,
    version="0.0.1",
)

app.include_router(branch_crime_router.router)

#cors settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {'app' : 'main'}

if __name__ == "__main__":
    gunicorn.run("main:app", host='0.0.0.0', port=8892, reload=True)


