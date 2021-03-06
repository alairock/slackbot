#!/usr/bin/env python

import sys
import logging
import logging.config
from smackbot import settings
from smackbot.bot import Bot


def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool')\
        .setLevel(logging.WARNING)
    bot = Bot()
    bot.run()


if __name__ == '__main__':
    main()
