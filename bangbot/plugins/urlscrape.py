# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import re

@irc3.plugin
class Plugin(object):
    def __init__(self, bot):
        self.bot = bot

    @irc3.event(irc3.rfc.PRIVMSG)
    def scrape(self, mask, event, target, data):
        """Scrape text for urls"""
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
        for url in urls:
            print(str(url))
