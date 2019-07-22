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
    def stock(self, mask, target, args):
        """Get info on the requested stock ticker

            %%stock <requestedStock>
        """
        try:
            stock_ticker = str(args['<requestedStock>']).upper()
            page =  html.fromstring(requests.get(
                    'https://www.marketwatch.com/investing/stock/' +
                    stock_ticker
                    ).content)
            market_name = str(page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/span[2]/text()')[0])
            ticker = str(page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/span[1]/text()')[0])
            company_name = str(page.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/h1/text()')[0])
            try:
                price = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/h3/bg-quote/text()')[0])
            except:
                price = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/h3/span/text()')[0])
            try:
                change_point = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/bg-quote/span[1]/bg-quote/text()')[0])
            except:
                change_point = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/bg-quote/span[1]/text()')[0])
            try:
                change_percent = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/bg-quote/span[2]/bg-quote/text()')[0])
            except:
                change_percent = str(page.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/bg-quote/span[2]/text()')[0])
            yield(
                    market_name + '/' + ticker + ' | ' + company_name +
                    ': $' +
                    price + '(' + change_point + ' | ' + change_percent + ')'
                )
        except:
            yield('Stock not found')
