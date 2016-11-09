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
