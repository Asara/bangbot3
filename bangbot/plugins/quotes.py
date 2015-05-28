# -*- coding: utf-8 -*-
from irc3.plugins.command import command
from random import randrange
import os
import irc3


qfolder = 'extra/quotesfolder/'
if not os.path.exists(qfolder):
    os.makedirs(qfolder)


@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @command(permission='view')
    def add(self, mask, target, args):
        """Add a quote

            %%add <quote>...
        """
        qfile = qfolder + target
        with open(quotesfile, 'a') as f:
            f.write("{}\n".format(' '.join(args['<quote>'])))


    @command(permission='view')
    def quote(self, mask, target, args):
        """If a specific number is given print that line, 0 for newest

            %%quote <number>
        """
        qfile = qfolder + target
        try:
            with open(qfile, 'r') as f:
                show_line = int(args['<number>'][0])
                get_line = show_line - 1
                try:
                    lines = f.readlines()
                    yield '{0}. {1}'.format(show_line, str(lines[get_line]))
                except:
                    yield 'That quote does not exist'
        except FileNotFoundError:
            yield 'There are no quotes yet'

    @command(permission='view')
    def rquote(self, mask, target, args):
        """Return a random quote

            %%rquote
        """
        qfile = qfolder + target
        try:
            with open(qfile, 'r') as f:
                lines = f.readlines()
                num_lines = len(lines)
                get_line = randrange(0, num_lines)
                show_line = get_line + 1
                line = lines[get_line]
                yield '{0}. {1}'.format(show_line, line)
        except FileNotFoundError:
            yield 'There are no quotes yet'
