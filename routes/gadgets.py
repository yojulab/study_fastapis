from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.get("/buttons", response_class=HTMLResponse) # 펑션 호출 방식
async def buttons(request:Request):
    return templates.TemplateResponse(name="gadgets/buttons.html", context={'request':request})

from models.gadgets import Gadget
@router.get("/Cards", response_class=HTMLResponse)
# request = Request(query_parameters)
async def Cards(request:Request, gadget: Gadget):
    # request.query_params
    # QueryParams('name=gocolab&email=info%40gocolab.com')
    # dict(request.query_params)
    # {'name': 'gocolab', 'email': 'info@gocolab.com'}
    return templates.TemplateResponse(name="gadgets/Cards.html"
                                      , context={'request':request})

@router.post("/Cards", response_class=HTMLResponse)
async def Cards_post(request:Request
                     , gadget: Gadget):
    # request.query_params
    # QueryParams('')
    # await request.form()
    # FormData([('name', 'gocolab'), ('email', 'info@gocolab.com')])
    # dict(await request.form())
    # {'name': 'gocolab', 'email': 'info@gocolab.com'}
    # form_datas = await request.form()
    # dict(form_datas)
    return templates.TemplateResponse(name="gadgets/Cards.html"
                                      , context={'request':request})

@router.get("/colors", response_class=HTMLResponse)
async def colors(request:Request):
    return templates.TemplateResponse(name="gadgets/colors.html", context={'request':request})

@router.get("/container", response_class=HTMLResponse)
async def container(request:Request):
    return templates.TemplateResponse(name="gadgets/container.html", context={'request':request})
