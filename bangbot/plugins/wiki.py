# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import wikipedia
import json
@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def wiki(self, mask, target, args):
        """Get the price of the specified cryptocurrency

            %%wiki <searchTerm>...
        """
        search = " ".join(args['<searchTerm>'])
        try:
            yield(wikipedia.summary(search, sentences=2))
            yield(wikipedia.page(search).url)
        except wikipedia.exceptions.DisambiguationError as dE:
            yield('Search term disambiguous, did you mean one of the following: ')
            yield(", ".join(dE.options[:5]))
        except wikipedia.exceptions.PageError as pE:
            yield(search + " not found.  Try another search")
