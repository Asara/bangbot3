# -*- coding: utf-8 -*-
from irc3.plugins.command import command
from yahoo_earnings_calendar import YahooEarningsCalendar
from datetime import datetime
from lxml import html
import irc3
import os
import requests

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
                stock = r['symbol']
                yec = YahooEarningsCalendar(0.3)
                try:
                    next_er = datetime.utcfromtimestamp(yec.get_next_earnings_date(stock)).strftime('%m/%d/%Y')
                except:
                    next_er = 'N/A'
                stock_open = float(r['regularMarketOpen'])
                if 'postMarketPrice' in r:
                    if float(r['postMarketChange']) < float(0):
                        change_sign = '↓'
                    else:
                        change_sign = '↑'
                    price = float(r['postMarketPrice'])
                    stock_close = float(r['regularMarketPrice'])
                    change = float(r['postMarketChange'])
                    change_pct = float(r['postMarketChangePercent'])
                    resp = 'After Hours: {} {}{:.2f} {:.2f} ({:+.2f}%), open: {:.2f}, close: {:.2f}, next er: {}'.format(stock, change_sign, price, change, change_pct, stock_open, stock_close, next_er)
                else:
                    if float(r['regularMarketChange']) < float(0):
                        change_sign = '↓'
                    else:
                        change_sign = '↑'
                    price = float(r['regularMarketPrice'])
                    change = float(r['regularMarketChange'])
                    change_pct = float(r['regularMarketChangePercent'])
                    resp = '{} {}{:.2f} {:.2f} ({:+.2f}%) open: {:.2f}, next er: {}'.format(stock, change_sign, price, change, change_pct, stock_open, next_er)
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
                        stock = r['symbol']
                        yec = YahooEarningsCalendar(0.3)
                        try:
                            next_er = datetime.utcfromtimestamp(yec.get_next_earnings_date(stock)).strftime('%m/%d/%Y')
                        except:
                            next_er = 'N/A'
                        stock_open = float(r['regularMarketOpen'])
                        if 'postMarketPrice' in r:
                            if float(r['postMarketChange']) < float(0):
                                change_sign = '↓'
                            else:
                                change_sign = '↑'
                            price = float(r['postMarketPrice'])
                            stock_close = float(r['regularMarketPrice'])
                            change = float(r['postMarketChange'])
                            change_pct = float(r['postMarketChangePercent'])
                            resp = 'After Hours: {} {}{:.2f} {:.2f} ({:+.2f}%), open: {:.2f}, close: {:.2f}, next er: {}'.format(stock, change_sign, price, change, change_pct, stock_open, stock_close, next_er)
                        else:
                            if float(r['regularMarketChange']) < float(0):
                                change_sign = '↓'
                            else:
                                change_sign = '↑'
                            price = float(r['regularMarketPrice'])
                            change = float(r['regularMarketChange'])
                            change_pct = float(r['regularMarketChangePercent'])
                            resp = '{} {}{:.2f} {:.2f} ({:+.2f}%) open: {:.2f}, next er: {}'.format(stock, change_sign, price, change, change_pct, stock_open, next_er)
                        yield(resp)
                    except:
                        yield('Stock not found')
            except:
                yield('Try saving your favorites first with !setmycc')
