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

    no_results = "No results found."

    query = duckduckgo.query(text)

    if query.type == 'nothing':
        return no_results

    try:
        result = query.related[0]
    except KeyError:
        return no_results

    text = result.text
    url = result.url

    if not text:
        text = 'No description available.'
    else:
        text = formatting.truncate_str(text.replace('\n', ''), 150)

    return u'{} -- \x02{}'.format(url, text)
