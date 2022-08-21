from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from backend.models import User
from backend.core import verify_password,create_access_token,deps
from backend.schemas import (
    User_Pydantic,
    UserIn_Pydantic,
    Response200,
    Response400,
    ResponseToken
)

login = APIRouter(tags=['认证相关'])


@login.post("/login",summary="登陆")
async def user_login(form_data:OAuth2PasswordRequestForm = Depends()):
    """
    用户登陆
    :param request:
    :param form_data:
    :return:
    """
    print("="*50 + "登陆函数" + "="*50)
    # := 可在表达式内部为变量赋值。 它被昵称为“海象运算符”因为它很像是 海象的眼睛和长牙
    if user := await User.get(username=form_data.username):
        if verify_password(form_data.password,user.password):
            token = create_access_token({"sub":user.username})

            return ResponseToken(data={"token":f"bear {token}"},access_token=token)
        return Response400(msg="请求失败")

@login.put("/logout",summary="注销")
async def user_logout(request:Request,user:User = Depends(deps.get_current_user)):
    request.app.state.redis.delete(user.username)
    return Response200()


@login.post("/user",summary="用户注册")
async def user_create(user:UserIn_Pydantic):
    return Response200(
        data=await User_Pydantic.from_tortoise_orm(await User.create(**user.dict()))
    )

@login.post("/token")
async def login_for_access_token():
    print("="*50 + "token" + "="*50)
    return {}