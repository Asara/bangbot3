# -*- coding: utf-8 -*-
import irc3
from irc3.plugins.command import command
from random import choice

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None)
    def flip(self, mask, target, args):
        """Flip a coin

            %%flip
        """
        yield choice(['Heads', 'Tails'])
