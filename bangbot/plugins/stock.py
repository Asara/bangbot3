# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
from yahoo_finance import Share

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def stock(self, mask, target, args):
        """Get the stock price of your ticker

            %%stock <ticker>
        """
        try:
            ticker = str(args['<ticker>'])
            yield(ticker + ': ' + Share(ticker).get_price())
        except:
            yield('Ticker not found')
