class CommunicationException(RuntimeError):
    """
    Indicates an exception regarding the communication with the Online Payments platform such as a connection exception.
    """

    def __init__(self, exception: Exception):
        super().__init__(exception)
        self.cause = exception
