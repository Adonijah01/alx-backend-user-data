#!/usr/bin/env python3
"""
filtered_logger module
"""

import re

def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specific fields in a log message using regex substitution.

    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all fields in the log line (message)

    Returns:
        String: Log message with specified fields obfuscated.
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']+', lambda x: x.group().split('=')[0] + '=' + redaction, message)

if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))

