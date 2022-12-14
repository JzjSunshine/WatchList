"""
depends
"""
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import status
from fastapi.requests import Request
from jose import jwt,JWTError

from backend.models import User
from .config import settings

# 指定 token 的路径
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login") #指向 登陆

async def get_current_user(request:Request,token: str = Depends(oauth2_scheme)) -> User:
    """
    oauth2_scheme -> 从请求头中取到 Authorization 的value
    解析token 获取当前用户对象
    :param request:
    :param token: 登陆之后获取到的 token
    :return: 当前用户对象
    """
    print("="*20+"get_current_user"+"="*20)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        username: str = payload.get('sub',None)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await User.get(username=username)
    # redis
    # if await request.app.state.redis.get(user.username) is None:
    #     raise HTTPException(detail='redis 数据失效', status_code=status.HTTP_408_REQUEST_TIMEOUT)
    if user is None:
        raise credentials_exception
    return user