class TaskNotFoundError(LookupError):
    """Raised when requested task does not exist"""


class StorageCorruptedError(Exception):
    """Raised when storage contains invalid JSON"""
