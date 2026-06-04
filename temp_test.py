from core.security import hash_password
from core.security import verify_password

hashed = hash_password("password123")

print("Hash", hashed)

print(
    verify_password(
        "password123",
        hashed
    )
)

from core.security import create_access_token
from core.security import decode_access_token

token = create_access_token(
    {"sub": "test@email.com"}
)

print(token)

print(
    decode_access_token(token)
)

