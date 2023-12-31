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
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """return none"""
        if request is None:
            return None
        return request.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """return none"""
        return None
