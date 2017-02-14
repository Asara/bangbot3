# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import datetime

line = ['   )     )     ) ',  '  ) \   ) \   ) \ ', ' / ) ( / ) ( / ) (',' \(_)/ \(_)/ \(_)/',]
@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def lit(self, mask, target, args):
        """ITS LITTY

            %%lit
        """
        cur = 0
        fin = 4
        while cur != fin:
            yield str(line[cur])
            cur += 1
