# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
from coinmarketcap import Market
from json import loads

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def cryptocur(self, mask, target, args):
        """Get the price of the specified cryptocurrency

            %%cryptocur <requestedCryptoCur>
        """
        try:
            curlookup = Market()
            cryptoCur= str(args['<requestedCryptoCur>'])
            yield(cryptoCur + ': ' + loads(curlookup.ticker(cryptoCur).decode("utf-8"))[0]["price_usd"])
        except:
            yield('Currency not found')
