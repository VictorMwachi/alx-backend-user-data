#!/usr/bin/env python3
"""class to manage the API authentication"""
from flask import request


class Auth:
    """manage api authenticate"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return none"""
        return None

    def authorization_header(self, request=None) -> str:
        """return none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return none"""
        return None
