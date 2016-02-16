# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import requests
import json
import re



@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None)
    def btc(self, mask, target, args):
        """BTC

            %%btc
        """
        r = requests.get('https://chain.so/api/v2/get_price/BTC/USD')
        a = {}
        for exchange in json.loads(r.text).get('data').get('prices'):
            a[exchange.get('exchange')] = exchange.get('price')
        yield ", ".join(["{}: {}".format(k,v) for k,v in a.items()])
