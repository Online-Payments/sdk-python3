from abc import ABC, abstractmethod


class SecretKeyStore(ABC):
    """
    A store of secret keys. Implementations could store secret keys in a database, on disk, etc.
    """

    @abstractmethod
    def get_secret_key(self, key_id: str):
        """
        :return: The secret key for the given key ID. Never None.
        :raise: SecretKeyNotAvailableException: If the secret key for the given
         key ID is not available.
        """
