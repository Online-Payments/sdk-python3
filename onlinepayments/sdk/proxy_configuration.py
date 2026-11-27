from collections.abc import Callable
from urllib.parse import quote, unquote, urlparse

from onlinepayments.sdk.log.obfuscation_rule import obfuscate_with_fixed_length


class ProxyConfiguration:
    """
    HTTP proxy configuration.

    Can be initialised directly from a host and port or can be constructed from a uri using fromuri
    """

    def __init__(self, host: str, port: int, scheme: str = "http", username: str | None = None, password: str | None = None):
        if not host:
            raise ValueError("host is required")
        if not port:
            raise ValueError("port is required")
        if port <= 0 or port > 65535:
            raise ValueError(f"""port "{port}" is invalid""")
        self.__scheme = scheme
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password

    @staticmethod
    def from_uri(uri: str, username: str | None = None, password: str | None = None) -> 'ProxyConfiguration':
        """
        Constructs a ProxyConfiguration from a URI; if username and/or password
        are given they will be used instead of corresponding data in the URI
        """
        parsed = urlparse(uri)
        if not parsed.scheme or not parsed.hostname:
            raise ValueError("proxy uri must contain a scheme and a host")
        scheme = parsed.scheme
        host = parsed.hostname
        port = parsed.port
        if username is None and parsed.username is not None:
            username = unquote(parsed.username)
        if password is None and parsed.password is not None:
            password = unquote(parsed.password)
        if port is None:
            if scheme == "http":
                port = 80
            elif scheme == "https":
                port = 443
            else:
                raise ValueError("unsupported scheme: " + scheme)
        return ProxyConfiguration(scheme=scheme,
                                  host=host,
                                  port=port,
                                  username=username,
                                  password=password)

    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str) -> None:
        self.__scheme = scheme

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str) -> None:
        self.__host = host

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int) -> None:
        self.__port = port

    @property
    def username(self) -> str | None:
        return self.__username

    @username.setter
    def username(self, username: str | None) -> None:
        self.__username = username

    @property
    def password(self) -> str | None:
        return self.__password

    @password.setter
    def password(self, password: str | None) -> None:
        self.__password = password

    def to_url(self) -> str:
        """
        Return a proxy URL in the form scheme://username:password@host:port
        or scheme://host:port if authentication is absent

        Supports HTTP Basic Auth
        """
        return self.__format(lambda password: quote(password, safe=""))

    def __str__(self):
        return self.__format(obfuscate_with_fixed_length(8))

    def __repr__(self):
        return f"ProxyConfiguration({self})"

    def __format(self, format_password: Callable[[str], str]) -> str:
        host = self.host
        if host and ":" in host and not host.startswith("["):
            host = f"[{host}]"
        if self.username is None or self.password is None:
            return f"{self.scheme}://{host}:{self.port}"
        return f"{self.scheme}://{quote(self.username, safe='')}:{format_password(self.password)}@{host}:{self.port}"
