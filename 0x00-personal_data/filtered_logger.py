#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    """
    Replaces sensitive information in a message with a redacted value
    based on the list of fields to redact

    Args:
        fields: list of fields to redact
        redaction: the value to use for redaction
        message: the string message to filter
        separator: the separator to use between fields

    Returns:
        The filtered string message with redacted values
    """


    pattern = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

import logging


class RedactingFormatter(logging.Formatter):
    """ 
    Custom Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        # Use filter_datum to filter out sensitive fields in the log message
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)

if __name__ == '__main__':
    main()
