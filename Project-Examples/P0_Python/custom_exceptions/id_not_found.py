"""This custom exception is used when you try to access an entity via a non-existent Id"""


class IdNotFound(Exception):
    pass
