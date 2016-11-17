#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########
# DEPENDS #
###########

import datetime
import os

############
# PROVIDES #
############


# Format messages with date and time
def generate_message(message_text):
    now = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
    print('[ ', now, ' ]: ', message_text)


# flatten list cf. `unlist()` in R
def flatten_list(l):
    for x in l:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in flatten_list(x):
                yield y
        else:
            yield x


# touch function for updating ruffus flag files
def touch(fname, mode=0o666, dir_fd=None, **kwargs):
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
        os.utime(f.fileno() if os.utime in os.supports_fd else fname,
                 dir_fd=None if os.supports_fd else dir_fd, **kwargs)
