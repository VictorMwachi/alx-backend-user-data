#!/usr/bin/env python3
"""
0. Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, messageseparator: str):
    """that returns the log message obfuscated"""
