from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory ="templates/")
router = APIRouter()

# 회원 가입 form /users/form -> users/inserts.html
@router.get("/form")  
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={'request':request})

# 회원 가입 /users/insert -> users/login.html
@router.get("/insert")  
async def insert(request:Request):
    pass    # biz
    return templates.TemplateResponse(name="users/logins.html"
                                      , context={'request':request})

# 회원 리스트 /users/list -> users/lists.html
@router.get("/list")  
async def insert(request:Request):
    return templates.TemplateResponse(name="users/lists.html"
                                      , context={'request':request})

# 회원 상세정보 /users/read -> users/reads.html
# Path parameters : /users/read/id or /users/read/uniqe_name
@router.get("/read/{object_id}")  
async def insert(request:Request, object_id):
    return templates.TemplateResponse(name="users/reads.html"
                                      , context={'request':request})
