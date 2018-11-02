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
    def cc(self, mask, target, args):
        """Get the price of the specified cryptocurrency

            %%cc <requestedCryptoCur>
        """
        try:
            currency_name = str(args['<requestedCryptoCur>']).upper()
            d =  requests.get(
                    'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' +
                    currency_name +
                    '&tsyms=USD'
                    ).json()['DISPLAY'][currency_name]['USD']
            yield(

                    currency_name +
                    ':' +
                    d['PRICE'] +
                    '. Market cap:' +
                    d['MKTCAP'] +
                    '. 24 Hour low:' +
                    d['LOW24HOUR'] +
                    '. 24 hour high:' +
                    d['HIGH24HOUR']
                )
        except:
            yield('Currency not found')
