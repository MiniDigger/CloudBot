
import asyncio

from cloudbot import hook
from cloudbot.util import colors

@hook.on_start()
def create_rainbow_pride(bot):
  global rainbow_pride
  rainbow_pride = colors.parse("$(red)P$(orange)r$(yellow)i$(green)d$(blue)e $(teal)M$(purple)o$(red)n$(orange)t$(yellow)h $(green)2$(blue)0$(teal)2$(purple)1")

@asyncio.coroutine
@hook.command
def pride(action):
    action("June is {}! This is why there are rainbows. Join the celebration! See more: https://nationaltoday.com/pride-month/".format(rainbow_pride))
