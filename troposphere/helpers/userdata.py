#!/usr/bin/python

from troposphere import Base64, Join


def from_file(filepath, delimiter='', blanklines=False):
    """Imports userdata from a file.

    :type filepath: string

    :param filepath  The absolute path to the file.

    :type delimiter: string

    :param: delimiter  Delimiter to use with the troposphere.Join().

    :type blanklines: boolean

    :param blanklines  If blank lines shoud be ignored

    rtype: troposphere.Base64
    :return The base64 representation of the file.
    """
    data = []

    try:
        with open(filepath, 'r') as f:
            data.extend(line for line in f if not blanklines or line.strip('\n\r ') != '')
    except IOError:
        raise IOError(f'Error opening or reading file: {filepath}')

    return Base64(Join(delimiter, data))
