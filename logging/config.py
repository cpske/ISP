import logging

def config():
    """configure the logger"""
    root = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    root.addHandler(handler)
    root.setLevel(logging.DEBUG)
