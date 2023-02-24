"""Script for verifying that a message was signed by a given key."""
from pathlib import Path

from nacl.encoding import Encoder, RawEncoder
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError


def verify(
    signed_message: bytes,
    verify_key: VerifyKey,
    encoder: Encoder = RawEncoder,
) -> bool:
    """Verify a message with a given verification key."""
    try:
        verify_key.verify(signed_message, encoder=encoder)
        return True
    except BadSignatureError:
        return False


def verify_file(file_name: Path, public_key_file: Path) -> None:
    """Entrypoint to digital signature verification program."""

    # Read the file to verify
    signed_message = file_name.read_bytes()

    # Read the public key
    verify_key_bytes = public_key_file.read_bytes()
    verify_key = VerifyKey(verify_key_bytes)

    # Verify the message
    if verify(signed_message, verify_key):
        print("Signature is valid!")
    else:
        print("Signature is invalid!")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python verify.py <file_name> <public_key_file>")
        sys.exit(1)
    signed_file = Path(sys.argv[1])
    public_key_file = Path(sys.argv[2])
    verify_file(signed_file, public_key_file)
