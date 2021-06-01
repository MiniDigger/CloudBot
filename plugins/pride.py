import asyncio

from cloudbot import hook

@asyncio.coroutine
@hook.command
def pride(action):
    action("June is LGBT Pride Month 2021! That is why there are rainbows. Join the celebration! See more: https://nationaltoday.com/pride-month/")
    
