#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########
# DEPENDS #
###########

import datetime

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
