# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import json
import os
import requests

ccfolder = 'extra/ccfolder/'
if not os.path.exists(ccfolder):
    os.makedirs(ccfolder)

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot



    @command(permission=None, options_first=True)
    def setmycc(self, mask, target, args):
        """Set your favorite crypto currencies for !cc @

            %%setmycc <currencies>...
        """
        ccfile = ccfolder + target + '_' + mask.nick
        currencies = args['<currencies>']
        try:
            with open(ccfile, 'w') as f:
                for currency in currencies:
                    f.write("{}\n".format(currency.upper()))
                yield 'Your cryptocurrency favorites saved'
        except:
            yield 'Could not save your preferences.  Please contact the administrator'


    @command(permission=None, options_first=True)
    def cc(self, mask, target, args):
        """Get the price of the specified cryptocurrency, an @ for your favorites.

            %%cc <requestedCryptoCur>
        """
        currency_name = str(args['<requestedCryptoCur>'])
        if currency_name != '@':
            currency_name = currency_name.upper()
            try:
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
        else:
            ccfile = ccfolder + target + '_' + mask.nick
            try:
                with open(ccfile, 'r') as f:
                    currencies = f.read().splitlines()
                for currency in currencies:
                    try:
                        d =  requests.get(
                                'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' +
                                currency +
                                '&tsyms=USD'
                                ).json()['DISPLAY'][currency]['USD']
                        yield(
    
                                currency +
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
            except:
                yield('Try saving your favorites first with !setmycc')
