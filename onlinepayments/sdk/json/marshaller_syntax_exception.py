class MarshallerSyntaxException(RuntimeError):
    """
    Thrown when a JSON string cannot be converted to a response object.
    """

    def __init__(self, cause: Exception | None = None):
        if cause:
            super().__init__(cause)
        else:
            super().__init__()
