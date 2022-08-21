from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """
    业务状态码
    """
    SUCCESS = 200
    FAIL = 400


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="业务状态码200请求成功，400请求失败")
    data: Any = Field(default=None, description="数据结果")
    msg: str = Field(default="请求成功", description="请求提示的msg")


class Response200(ResponseBasic):
    pass


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = Field(default="请求失败", description="请求提示的msg")

class ResponseToken(ResponseBasic):
    access_token: str
    token_type: str = Field(default="bearer")
