# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3


@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission='view')
    def add(self, mask, target, args):
        """Add a quote

            %%add <message>...
        """
        yield ' '.join(args['<message>'])
