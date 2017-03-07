# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
from random import randint

line = [
	'_,-=._              /|_/|       >(\' )',
	'`-.}   `=._,.-=-._.,  @ @._,     / (',
	'   `._ _,-.   )      _,.-\'      /   `----/',
	'     `    G.m-"^m`m\'            \   ~=- /'
]

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None, options_first=True)
    def foxandgoose(self, mask, target, args):
        """lolololol

            %%foxandgoose
        """
        cur = 0
        fin = 4
        if randint(1,100) < 45:
	        while cur != fin:
	            yield str(line[cur])
	            cur += 1
        else:
          yield str('lol')
