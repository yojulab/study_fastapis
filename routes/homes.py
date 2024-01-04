from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

from starlette.responses import HTMLResponse
from fastapi import Request
# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# /home/params_query -> /homes/parameters_query.html 호출
@router.get("/params_query")
async def home(request:Request):
    pass
    return templates.TemplateResponse(name="homes/parameters_query.html"
                                      , context={"request":request})

# /home
# @router.get("/", response_class=HTMLResponse)
# async def home():
#     # return {"message": "home World!"}
#     html = "<body> <h2>It's Home.</h2> </body>"
#     return html
@router.get("/")
async def root(request:Request):
    pass
    return templates.TemplateResponse(name="homes/standards.html"
                                      , context={"request":request})

# /home/list
# 어노테이션 (웹에서 업무(function) 호출)
@router.get("/list", response_class=HTMLResponse)  
async def home_list():
    # pass
    # return 0
    html = "<body> <h2>It's Home List.</h2> </body>"
    return html

