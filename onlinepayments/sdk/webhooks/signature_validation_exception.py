from typing import Optional


class SignatureValidationException(RuntimeError):
    """
    Represents an error while validating webhooks signatures.
    """

    def __init__(self, message: Optional[str] = None, cause: Optional[Exception] = None):
        if message and cause:
            super(SignatureValidationException, self).__init__(message, cause)
        elif message:
            super(SignatureValidationException, self).__init__(message)
        elif cause:
            super(SignatureValidationException, self).__init__(cause)
        else:
            super(SignatureValidationException, self).__init__()
