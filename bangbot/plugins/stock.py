# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import requests
import os

stocksfolder = 'extra/stocksfolder/'
if not os.path.exists(stocksfolder):
    os.makedirs(stocksfolder)


@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def setmystocks(self, mask, target, args):
        """Set your favorite crypto currencies for !cc @

            %%setmystocks <stocks>...
        """
        stocksfile = stocksfolder + target + '_' + mask.nick
        stocks = args['<stocks>']
        try:
            with open(stocksfile, 'w') as f:
                for stock in stocks:
                    f.write("{}\n".format(stock))
                yield 'Your favorite stocks are saved'
        except:
            yield 'Could not save your preferences.  Please contact the administrator'


    @command(permission=None, options_first=True)
    def stock(self, mask, target, args):
        """Get info on the requested stock ticker. Data from AlphaVantage

            %%stock <requestedStock>
        """
        stock_ticker = str(args['<requestedStock>'])
        if stock_ticker != '@':
            try:
                url = 'https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols=' + stock_ticker
                r = requests.get(url).json()['quoteResponse']['result'][0]
                if float(r['regularMarketChange']) < float(0):
                    change_sign = '↓'
                else:
                    change_sign = '↑'
                stock = r['symbol']
                stock_open = float(r['regularMarketOpen'])
                price = float(r['regularMarketPrice'])
                change = float(r['regularMarketChange'])
                change_pct = float(r['regularMarketChangePercent'])
                resp = '{} {}{:.2f} {:.2f} ({:+.2f}%) open: {:.2f}'.format(stock, change_sign, price, change, change_pct, stock_open)
                yield(resp)
            except: 
                yield('Stock not found')
        else:
            stocksfile = stocksfolder + target + '_' + mask.nick
            try:
                with open(stocksfile, 'r') as f:
                    stocks = f.read().splitlines()
                for stock_ticker in stocks:
                    try:
                        url = 'https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols=' + stock_ticker
                        r = requests.get(url).json()['quoteResponse']['result'][0]
                        if float(r['regularMarketChange']) < float(0):
                            change_sign = '↓'
                        else:
                            change_sign = '↑'
                        stock = r['symbol']
                        stock_open = float(r['regularMarketOpen'])
                        price = float(r['regularMarketPrice'])
                        change = float(r['regularMarketChange'])
                        change_pct = float(r['regularMarketChangePercent'])
                        resp = '{} {}{:.2f} {:.2f} ({:+.2f}%) open: {:.2f}'.format(stock, change_sign, price, change, change_pct, stock_open)
                        yield(resp)
                    except:
                        yield('Stock not found')
            except:
                yield('Try saving your favorites first with !setmycc')
