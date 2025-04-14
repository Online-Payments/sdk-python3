class AuthorizationType:
    V1HMAC = "v1HMAC"
    AUTHORIZATION_TYPES = [V1HMAC]

    @staticmethod
    def get_authorization(name: str) -> str:
        if name in AuthorizationType.AUTHORIZATION_TYPES:
            return name
        else:
            raise ValueError("Authorization '{}' not found".format(name))
