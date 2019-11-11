import jwt

class AuthService:
    def __init__(self):
        pass

    def details(self, auth_token: str) -> str:
        return jwt.decode(auth_token, verify=False)
