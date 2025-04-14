from .body_obfuscator import BodyObfuscator
from .header_obfuscator import HeaderObfuscator
from .log_message import LogMessage


class ResponseLogMessage(LogMessage):
    """
    A utility class to build request log messages.
    """

    def __init__(self, request_id: str, status_code: int, duration: int = -1,
                 body_obfuscator: BodyObfuscator = BodyObfuscator.default_body_obfuscator(),
                 header_obfuscator: HeaderObfuscator = HeaderObfuscator.default_header_obfuscator()):
        super(ResponseLogMessage, self).__init__(request_id, body_obfuscator, header_obfuscator)
        self.__status_code = status_code
        self.__duration = duration

    def get_duration(self) -> int:
        return self.__duration

    def get_status_code(self) -> int:
        return self.__status_code

    def get_message(self) -> str:
        if self.__duration < 0:
            return "Incoming response (requestId='" + self.request_id + "'):\n" + \
                   "  status_code:  " + str(self.__status_code) + "\n" + \
                   "  headers:      " + self.headers + "\n" + \
                   "  content-type: " + self.empty_if_none(self.content_type) + "\n" + \
                   "  body:         " + self.empty_if_none(self.body)

        else:
            return "Incoming response (requestId='" + self.request_id + "', " + str(self.__duration) + " ms):\n" + \
                   "  status_code:  " + str(self.__status_code) + "\n" + \
                   "  headers:      " + self.headers + "\n" + \
                   "  content-type: " + self.empty_if_none(self.content_type) + "\n" + \
                   "  body:         " + self.empty_if_none(self.body)
