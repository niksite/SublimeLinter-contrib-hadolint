#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Nikolay Panov
# Copyright (c) 2016 Nikolay Panov
#
# License: MIT
#

"""This module exports the Hadolint plugin class."""

from SublimeLinter.lint import Linter, util


class Hadolint(Linter):
    """Provides an interface to hadolint."""

    cmd = 'hadolint'
    regex = r'(.+)\:(?P<line>[^\s]+) (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    word_re = None
    defaults = {
        '--ignore:,+': '',
        'selector': 'source.dockerfile'
    }
