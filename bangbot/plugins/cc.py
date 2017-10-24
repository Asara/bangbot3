# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
from coinmarketcap import Market
from json import loads

price_cheat_sheet = {
  "btc": "bitcoin",
  "bch": "bitcoin-cash",
  "btg": "bitcoin-gold",
  "eth": "ethereum",
  "xrp": "ripple",
  "ltc": "litecoin",
  "xmr": "monero"

}

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
            curlookup = Market()
            cryptoCur= str(args['<requestedCryptoCur>'])
            yield(price_cheat_sheet[cryptoCur] + ': ' + loads(curlookup.ticker(price_cheat_sheet[cryptoCur]).decode("utf-8"))[0]["price_usd"])
        except:
            yield('Currency not found')
