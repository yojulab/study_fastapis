from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request, status
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 form /users/form -> users/inserts.html
@router.get("/form")  
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html"
                                      , context={'request':request})
from models.users import User
from database.connection import Database
_database = Database(User)

# 회원 가입 /users/insert -> users/login.html
@router.get("/insert")  
async def insert(request:Request):
    dict_params = dict(request.query_params)
    user = User(**dict_params)
    await _database.save(user)
    return templates.TemplateResponse(name="users/logins.html"
                                      , context={'request':request})

# 회원 가입 /users/insert -> users/login.html
@router.post("/insert")  
async def insert(request:Request, body: User):
    dict_params = dict(await request.form())
    await _database.save(dict_params)
    return templates.TemplateResponse(name="users/logins.html"
                                      , context={'request':request})

# 회원 리스트 /users/list -> users/lists.html
@router.get("/list")  
async def list(request:Request):
    user_list = await _database.get_all()
    return templates.TemplateResponse(name="users/lists.html"
                                      , context={'request':request
                                                 ,'users':user_list})

from beanie import PydanticObjectId
# 회원 상세정보 /users/read -> users/reads.html
# Path parameters : /users/read/id or /users/read/uniqe_name
@router.get("/read/{object_id}")  
async def read(request:Request, object_id:PydanticObjectId):
    user = await _database.get(object_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

    return templates.TemplateResponse(name="users/reads.html"
                                      , context={'request':request
                                                 ,'user':user})
