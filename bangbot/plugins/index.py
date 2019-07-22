# -*- coding: utf-8 -*-
from irc3.plugins.command import command
from lxml import html
import irc3
import json
import requests

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def index(self, mask, target, args):
        """Get info on the requested stock index

            %%index <requestedIndex>
        """
        try:
            index = str(args['<requestedIndex>']).upper()
            page =  html.fromstring(requests.get(
                    'https://www.marketwatch.com/investing/index/' +
                    index 
                    ).content)
            index_name = str(page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/h1/text()')[0])
            value = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/h3/span/text()')[0])
            change_point = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/bg-quote/span[1]/text()')[0])
            change_percent = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/bg-quote/span[2]/text()')[0])
            
            yield(
                    index_name + ': ' + value + ' (' + change_point + '|' + change_percent + ')'
                )
        except:
            yield('Stock not found')
