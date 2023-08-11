#!/usr/bin/env python3
"""class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manage api authenticate"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return none"""
        if path is None:
            return True
        if exclude_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path in exclude_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """return none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return none"""
        return None
