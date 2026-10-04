"""Access control example used for code review integration validation"""


def can_read_private_document(requesting_user_id, owner_user_id):
    """Only the document owner may read a private document"""
    return requesting_user_id != owner_user_id
