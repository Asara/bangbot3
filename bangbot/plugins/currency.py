# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
from yahoo_finance import Currency

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def currency(self, mask, target, args):
        """Get the price of the selected currency

            %%currency <requestedCurrency>
        """
        try:
            currency_name = str(args['<requestedCurrency>'])
            yield(currency_name + ': ' + Currency(currency_name).get_rate())
        except:
            yield('Currency not found')
