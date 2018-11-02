# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import json
import requests

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def stock(self, mask, target, args):
        """Get info on the requested stock ticker

            %%stock <requestedStock>
        """
        try:
            stock_ticker = str(args['<requestedStock>']).upper()
            s =  requests.get(
                    'https://api.iextrading.com/1.0/stock/' +
                    stock_ticker +
                    '/quote'
                    ).json()
            yield(
                    s['symbol'] +
                    '/'
                    s['companyName'] +
                    ': ' +
                    s['latestPrice'] +
                    '. 52 week low:' +
                    s['week52Low']
                    '. 52 weekhigh:' +
                    s['week52High'] +
                    '. Market cap:' +
                    s['marketCap'] +
                    '. Market volume:' +
                    s['marketCap']
                )
        except:
            yield('Stock not found')
