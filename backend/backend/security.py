from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


class Hasher:
    """Wrap the hashes functionalities."""
    @staticmethod
    def get_password_hash(pwd: str) -> str:
        return pwd_context.hash(pwd)

    @staticmethod
    def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
        return pwd_context.verify(plain_pwd, hashed_pwd)
