import asyncio

from cloudbot import hook

@asyncio.coroutine
@hook.command("no_eta", "eta")
def no_eta(action):
    action("There is no ETA (Estimated Time of Arrival)! Updates to Paper do not have any sort of estimate for when they release, ever. Any and all updates will arrive when they are ready, and the only thing to do is wait for them patiently along with everyone else.")
    
