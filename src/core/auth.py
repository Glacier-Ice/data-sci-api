import connexion
from connexion.exceptions import OAuthProblem
from connexion import request
import secrets
from flask import current_app


def generate_aipkey(length=64) -> str:
    """Generate a new LENGTH-string api-key."""
    return secrets.token_urlsafe(length)


def generate_apikey_record(uid, length=64) -> dict:
    """Generate a new api-key record from UID and LENGTH."""
    return {generate_aipkey(length=length): {"uid": uid}}


def verify_apikey(token, required_scopes):
    """Helper function to verify provided TOKEN with REQUIRED_SCOPES."""
    config = current_app.config
    TOKEN_DB = config["api_tokens"]
    info = TOKEN_DB.get(token, None)
    if not info:
        raise OAuthProblem("Invalid token provided, please authorize with CORRECT Api-key!")
    return info
