from fastapi import APIRouter,Depends


login = APIRouter(tags=['认证相关'])


@login.post("/login",summary="登录")
async def user_login():
    return