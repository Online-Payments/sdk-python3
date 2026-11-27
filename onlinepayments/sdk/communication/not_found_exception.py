import copyreg


class NotFoundException(RuntimeError):
    """
    Indicates an exception that occurs when the requested resource is not found.
    In normal usage of the SDK, this exception should not occur, however it is possible.
    For example when path parameters are set with invalid values.
    """

    def __init__(self, exception: Exception, message: str):
        super().__init__(message)
        self.cause = exception
        self.__cause__ = exception

    def __reduce__(self):
        # Recreate the exception without calling __init__, so it can be pickled; the fields are restored from __dict__.
        return copyreg.__newobj__, (type(self), *self.args), self.__dict__
