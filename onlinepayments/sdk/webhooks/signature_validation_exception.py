class SignatureValidationException(RuntimeError):
    """
    Represents an error while validating webhooks signatures.
    """

    def __init__(self, message: str | None = None, cause: Exception | None = None):
        if message and cause:
            super().__init__(message, cause)
        elif message:
            super().__init__(message)
        elif cause:
            super().__init__(cause)
        else:
            super().__init__()
