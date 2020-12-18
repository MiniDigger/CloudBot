"""
duckduckgo.py

Gets DuckDuckGo Instant Answers

Created By:
    - Jacob Andersen <https://jacobandersen.dev/>

License:
    GNU General Public License (Version 3)
"""

import duckduckgo

from cloudbot import hook
from cloudbot.util import formatting

@hook.command('ddg', 'duckduckgo', 'g', 'google')
def search(text):
    """<query> -- Returns first DDG instant answer result for <query>."""
    return u'{}'.format(duckduckgo.get_zci(text))
