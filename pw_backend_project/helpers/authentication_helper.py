import bcrypt

from pw_backend_project.models import CustomUser

class AuthenticationHelper:
    def get_hashed_password(password: str):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def authenticate(user: CustomUser, password: str):
        return bcrypt.checkpw(password, user.passowrd)
