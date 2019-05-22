# singleton
class Singleton(object):
    """pythonによるSingleton"""
    _instance = None
    def __new__(cls):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance
