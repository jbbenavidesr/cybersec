"""Script for verifying that a message was signed by a given key."""
from pathlib import Path

from nacl.encoding import Encoder, RawEncoder
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError


def verify(
    message: bytes,
    signature: bytes,
    verify_key: VerifyKey,
    encoder: Encoder = RawEncoder,
) -> bool:
    """Verify a message with a given verify key."""
    try:
        verify_key.verify(message, signature, encoder=encoder)
        return True
    except BadSignatureError:
        return False


def verify_file(file_name: Path) -> None:
    """Entrypoint to digital signature verification program."""
    with file_name.open("rb") as f:
        message = f.read()

    verify_key_file = file_name.with_suffix(".key")
    with verify_key_file.open("rb") as f:
        verify_key_bytes = f.read()

    verify_key = VerifyKey(verify_key_bytes)

    signature_file = file_name.with_suffix(".sig")
    with signature_file.open("rb") as f:
        signature = f.read()

    if verify(message, signature, verify_key):
        print("Signature is valid!")
    else:
        print("Signature is invalid!")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python verify.py <file_name>")
        sys.exit(1)
    path = Path(sys.argv[1])
    verify_file(path)
