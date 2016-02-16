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

    syntax = 'dockerfile'
    cmd = 'hadolint -i'
    executable = None
    version_args = '-v'
    version_re = r'Haskell Dockerfile Linter v(?P<version>\d+\.\d+)'
    version_requirement = '>= 0.1'
    regex = r'L(?P<line>\d+) (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
