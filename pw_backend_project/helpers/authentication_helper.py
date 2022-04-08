import bcrypt

from pw_backend_project.models import CustomUser

class AuthenticationHelper:
    def get_hashed_password(self, password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def authenticate(self, user: CustomUser, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), user.passowrd)
