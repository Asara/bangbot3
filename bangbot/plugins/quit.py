# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3


@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission='admin')
    def quit(self, mask, target, args):
        """Quit

            %%quit
        """
        yield 'Quitting'
        self.bot.loop.call_later(1, self.bot.quit)
        self.bot.loop.call_later(1, self.bot.loop.stop)
