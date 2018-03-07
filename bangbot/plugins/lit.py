# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import datetime

fire = [
    '   )     )     ) ',
    '  ) \   ) \   ) \ ',
    ' / ) ( / ) ( / ) (',
    ' \(_)/ \(_)/ \(_)/',
]

snake = [
    ' >---==',
    '      ==',
    '      =',
    '     ==',
    '    =====',
    '   =========="',

]
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
            yield str(fire[cur])
            cur += 1

    @command(permission=None, options_first=True)
    def hotsnake(self, mask, target, args):
        """SNEK

            %%hotsnake
        """
        cur = 0
        fin = 6
        while cur != fin:
            yield str(snake[cur])
            cur += 1
