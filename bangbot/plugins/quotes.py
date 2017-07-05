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

    @command(permission=None)
    def add(self, mask, target, args):
        """Add a quote

            %%add <quote>...
        """
        qfile = qfolder + target
        add_quote = ' '.join(args['<quote>'])
        try:
            with open(qfile, 'a') as f:
                f.write("{}\n".format(add_quote))
            with open(qfile, 'r') as f:
                for num, line in enumerate(f, 1):
                    if add_quote in line:
                        yield 'Added quote #{0}: {1}'.format(num, add_quote)
        except:
            yield 'Could not add quote.'


    @command(permission=None)
    def quote(self, mask, target, args):
        """If a specific number is given print that line, 0 for newest

            %%quote [<number>]
        """
        qfile = qfolder + target
        if args['<number>']:
            line_number = int(args['<number>'])
            try:
                with open(qfile, 'r') as f:
                    get_line = line_number - 1
                    try:
                        lines = f.readlines()
                        yield '{0}. {1}'.format(
                                line_number, str(lines[get_line])
                        )
                    except:
                        yield 'That quote does not exist'
            except FileNotFoundError:
                yield 'There are no quotes yet'
        else:
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

    @command(permission=None)
    def quotes(self, mask, target, args):
        """Print all quotes

            %%quotes
        """
        qfile = qfolder + target
        try:
            with open(qfile, 'r') as f:
                lines = f.readlines()
                for indx, line in enumerate(lines):
                    yield '{0}. {1}'.format(indx+1, line)
        except FileNotFoundError:
            yield 'There are no quotes yet'

    @command(permission='admin')
    def delete(self,mask,target,args):
        """Delete quote by number (Admin)

            %%delete <number>
        """
        qfile = qfolder + target
        delete_number = int(args['<number>'][0])
        infile = open(qfile, 'r')
        out = open(qfile + ".new", "w")
        for i, l in enumerate(infile, 1):
            if i != delete_number:
                out.write(l)
        infile.close()
        out.close()
        os.rename(qfile + ".new", qfile)
