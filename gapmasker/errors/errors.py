#!/usr/bin/env python

import os
import sys
__all__ = [
    'FileError',
    'DirectoryError',
    'OptionError',
    'RangeError',
    'filecheck',
    'filequit',
    'directorymake',
    'directorycheck',
    'directoryquit',
    'optioncheck',
    'rangecheck',
    ]

# Constants

POSINF = float('inf')
NEGINF = -POSINF


class FileError(Exception):

    """ Reporting when file errors occur """

    def __init__(self, filename=''):
        """ Store the file that gave the exception """

        self.value = filename

    def __str__(self):
        return 'Error opening file \'{0}\''.format(self.value)


class DirectoryError(FileError):

    """ Reporting when directory errors occur """

    def __str__(self):
        line1 = 'Error opening directory \'{0}\''.format(self.value)
        line2 = 'Directory doesn\'t exist'
        return '\n'.join((line1, line2))


class OptionError(Exception):

    """ Reports on disallowed options passed to functions """

    def __init__(self, option, choices):
        self.value = option
        self.choices = choices

    def __str__(self):
        return '\'{0}\' is not a valid option. Valid options are {1}'.format(self.value,
                self.choices)


class RangeError(Exception):

    """ Raise exception when number is outside a valid range """

    def __init__(
        self,
        n,
        lower,
        upper,
        ):
        self.value = n
        self.lower = lower
        self.upper = upper

    def __str__(self):

        return '\'{0}\' is outside the valid range {1} - {2}'.format(self.value,
                self.lower, self.upper)


def filecheck(filename):
    if not os.path.isfile(filename):
        raise FileError(filename)
    return filename


def filequit(filename):
    try:
        filecheck(filename)
    except FileError, e:
        print e
        sys.exit()


def directorycheck(directory):
    if not os.path.isdir(directory):
        raise DirectoryError(directory)
    return directory


def directoryquit(directory):
    try:
        if not os.path.isdir(directory):
            raise DirectoryError(directory)
    except DirectoryError, e:
        print e
        sys.exit()


def directorymake(directory, verbose=True):
    try:
        directorycheck(directory)
    except DirectoryError, e:
        if verbose:
            print e
            print 'Creating \'{0}\''.format(directory)
        os.makedirs(directory)
    return directorycheck(directory)


def optioncheck(option, choices):
    if option not in choices:
        raise OptionError(option, choices)
    return option


def rangecheck(n, lower, upper):
    if n < lower or n > upper:
        raise RangeError(n, lower, upper)
    return n
