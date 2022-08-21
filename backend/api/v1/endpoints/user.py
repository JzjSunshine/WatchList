from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.requests import Request

from backend.models import User
from backend.core import verify_password,create_access_token,deps
from backend.schemas import User_Pydantic,UserIn_Pydantic,Response200,Response400


user = APIRouter(tags=['用户相关'])



@user.get("/user",summary="当前用户")
async def usr_info(user_obj:User = Depends(deps.get_current_user)):
    """

    :param user_obj:
    :return:
    """
    return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))

@user.post("/user",summary="修改信息")
async def user_update(user_from:UserIn_Pydantic,user_obj:User = Depends(deps.get_current_user)):
    """
    修改当前用户的信息
    :param user_from:
    :param user_obj:
    :return:
    """
    user_from.username = user_obj.username
    user_from.password = user_obj.password
    if await User.filter(username=user_obj.username).update(**user_from.dict()):
        return Response200(data=await User_Pydantic.from_tortoise_orm(user_obj))
    return Response400(msg="用户信息更新失败")



