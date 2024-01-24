from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory ="templates/")
router = APIRouter()

# 회원 가입 form --users/form
@router.get("/form") 
async def inserts(request: Request) :
    return templates.TemplateResponse(name="users/inserts.html",
                                      context={"request":request})

@router.post("/insert") 
async def inserts(request: Request) :
    dict_details = dict(await request.form())
    print(dict_details)
    pass # biz
    return templates.TemplateResponse(name="users/logins.html",
                                      context={"request":request})
# 회원 리스트 /users/list
@router.post("/list") 
async def inserts(request: Request) :
    dict_details = dict(await request.form())
    print(dict_details)
    return templates.TemplateResponse(name="users/lists.html",
                                      context={"request":request})

# 회원 리스트 /users/list
@router.get("/list") 
async def inserts(request: Request) :
    print(dict(request.query_params))
    return templates.TemplateResponse(name="users/lists.html",
                                      context={"request":request})

# 회원 상세정보 /users/read <- 특정 사람에 대한 정보가 표현되어야 함.
# Path parameters : /users/read/id  or /users/read/unique_name  << 특정하기 위한 parameter는 unique해야 함. so 
@router.get("/read/{object_id}") # 궁금한 점 format을 써도 되는지?
async def inserts(request: Request, object_id) : # async def inserts(request: Request, object_id:str) << str을 붙이지 않은 것과 동일함
    dict_details = dict(request.query_params)
    print(dict_details)
    return templates.TemplateResponse(name="users/reads.html",
                                      context={"request":request})


@router.post("/updates/{object_id}") 
async def inserts(request: Request, object_id) :
    dict_details = dict(await request.form())
    print(dict_details)
    return templates.TemplateResponse(name="users/updates.html",
                                      context={"request":request})