# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import datetime


@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def time(self, mask, target, args):
        """Current time

            %%time [<offset>]
        """
        try:
            offset = int(args['<offset>'])
        except:
            offset = 0
        print(offset)
        output = datetime.datetime.utcnow()+datetime.timedelta(hours=offset)

        yield str(output.strftime("%H:%M"))
