import asyncio

from cloudbot import hook

@asyncio.coroutine
@hook.command
def pride(action):
    action("June is LGBTQ Pride Month! That is why there are rainbows right now. Join the celebration! See more: https://nationaltoday.com/pride-month/")
    
