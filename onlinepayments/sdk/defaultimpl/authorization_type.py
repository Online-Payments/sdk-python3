class AuthorizationType:
    V1HMAC = "v1HMAC"
    AUTHORIZATION_TYPES = [V1HMAC]

    @staticmethod
    def get_authorization(name: str) -> str:
        for authType in AuthorizationType.AUTHORIZATION_TYPES:
            if authType.lower() == name.lower():
                return authType
        raise RuntimeError("Authorization '{}' not found".format(name))
