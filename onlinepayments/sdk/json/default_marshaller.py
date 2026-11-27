from json import dumps, loads
from typing import Any

from .marshaller import Marshaller, T
from .marshaller_syntax_exception import MarshallerSyntaxException

from onlinepayments.sdk.domain.data_object import DataObject


class DefaultMarshaller(Marshaller):
    """
    Marshaller implementation based on json.
    """

    @staticmethod
    def instance() -> 'DefaultMarshaller':
        return _DEFAULT_MARSHALLER_INSTANCE

    def marshal(self, request_object: Any) -> str:
        if isinstance(request_object, DataObject):
            dictionary = request_object.to_dictionary()
            return dumps(dictionary,
                         default=lambda o: o.to_dictionary(),
                         separators=(",", ":"))
        else:
            return dumps(request_object,
                         default=lambda o: o.__dict__,
                         separators=(",", ":"))

    def unmarshal(self, response_json: str | bytes | None, type_class: type[T]) -> T | None:
        if not response_json:
            return None
        if issubclass(type_class, DataObject):
            try:
                result = type_class()
                result.from_dictionary(loads(response_json))
                return result
            except Exception as e:
                raise MarshallerSyntaxException(e) from e

        class Object:
            pass

        def convert_to_object(value):
            if isinstance(value, dict):
                o = Object()
                for key, item in value.items():
                    o.__dict__[key] = convert_to_object(item)
                return o
            if isinstance(value, list):
                return [convert_to_object(item) for item in value]
            return value

        try:
            return convert_to_object(loads(response_json))
        except ValueError as e:
            raise MarshallerSyntaxException(e) from e


_DEFAULT_MARSHALLER_INSTANCE = DefaultMarshaller()
