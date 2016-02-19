# -*- coding: utf-8 -*-
import irc3
from irc3.plugins.command import command
from random import randrange 

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission=None)
    def roll(self, mask, target, args):
        """Roll a sided dice (XdY+Z), 1d6+0 if no options given

            %%roll [<dice>]...
        """
        dice = ' '.join(args['<dice>'])
        original_roll = dice
        try:
            z = int(dice.split('+')[1])
            dice = dice.split('+')[0]
        except:
            z = 0

        try:
            (x, y) = dice.split('d')
            x = int(x)
            y = int(y)
        except:
            x = 1
            y = 6

        if (x > 1024) or (y > 1024) or (z > 1024):
            yield 'Limit for all numbers is 1024.  Sorry'

        else:
            roll_list= []
            for _ in range(x):
                roll_list.append(randrange(1,y))
            roll_total = sum(x for x in roll_list)
            modified_roll_total = roll_total + z
            yield '{}: {}'.format(original_roll, modified_roll_total)
