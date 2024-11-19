from crud import *


def check_token(session, token):
    user = ''
    if token:
        user = read_user_by_uuid(session, token)
    else:
        user = None
    return user
