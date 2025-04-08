# user_auth.py

def is_valid_login(email: str, password: str) -> bool:
    if not email or not password:
        return False
    if "@" not in email or len(password) < 6:
        return False
    return True


def generate_token(email: str) -> str:
    if not is_valid_login(email, "dummyPass"):
        raise ValueError("Invalid email format")
    return f"token_{email.replace('@', '_at_')}"


# test_user_auth.py
import unittest
from user_auth import is_valid_login, generate_token

class TestUserAuth(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(is_valid_login("user@example.com", "securePass"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_login("userexample.com", "securePass"))

    def test_short_password(self):
        self.assertFalse(is_valid_login("user@example.com", "123"))

    def test_empty_fields(self):
        self.assertFalse(is_valid_login("", ""))

    def test_token_generation_success(self):
        token = generate_token("user@example.com")
        self.assertEqual(token, "token_user_at_example.com")

    def test_token_generation_failure(self):
        with self.assertRaises(ValueError):
            generate_token("invalidemail.com")


if __name__ == '__main__':
    unittest.main()
