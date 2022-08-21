def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

import types

def function():
    """普通函数"""
    return 1

def generator():
    """生成器函数"""
    yield 1

async def async_function():
    """异步函数（协程）"""
    return 1

async def async_generator():
    """异步生成器"""
    yield 1


print(type(function) is types.FunctionType)
print(type(generator()) is types.GeneratorType)
print(type(async_function()) is types.CoroutineType)
print(type(async_generator()) is types.AsyncGeneratorType)

print(async_function()) # <coroutine object async_function at 0x102ff67d8> 直接调用异步函数返回一个 coroutine 对象
# 协程需要其他方式来驱动 因此可以使用该协程对象的 send 方法给协程发送一个值
#
