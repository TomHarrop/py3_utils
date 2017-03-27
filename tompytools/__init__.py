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

def generate_message(message_text):
    """Format messages with date and time"""
    now = datetime.datetime.now().strftime('%a %b %d %H:%M:%S %Y')
    print('[ ', now, ' ]: ', message_text)


def flatten_list(l):
    """works like `unlist()` in R"""
    for x in l:
        if hasattr(x, '__iter__') and not isinstance(x, str):
            for y in flatten_list(x):
                yield y
        else:
            yield x


def touch(fname, mode=0o666, dir_fd=None, **kwargs):
    """Touch function for updating ruffus flag files"""
    flags = os.O_CREAT | os.O_APPEND
    with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
        os.utime(f.fileno() if os.utime in os.supports_fd else fname,
                 dir_fd=None if os.supports_fd else dir_fd, **kwargs)


def find_all(names, path):
    """Find all files in path that match names.

    Args:
        names: List of file names to match.
        path: String of path to search

    Returns:
        List of matched file names with path.
    """
    path_contents = [
        (dirpath, filenames) for dirpath, dirnames, filenames
        in os.walk(path, followlinks=True)]
    all_path_files = []
    for dirpath, filenames in path_contents:
        for filename in filenames:
            all_path_files.append(os.path.join(dirpath, filename))
    names_path_matches = []
    for file in all_path_files:
        if any([x in os.path.basename(file) for x in names]):
            names_path_matches.append(file)
    return(names_path_matches)
