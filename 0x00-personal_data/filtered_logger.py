#!/usr/bin/env python3
"""
0. Regex-ing
"""
import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, messageseparator: str) -> str:
    """that returns the log message obfuscated"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
