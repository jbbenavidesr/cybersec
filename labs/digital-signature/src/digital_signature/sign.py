"""Simple program to sign and verify a file."""
from pathlib import Path

from nacl.encoding import Encoder, RawEncoder
from nacl.signing import SigningKey


def sign(
    message: bytes, signing_key: SigningKey, encoder: Encoder = RawEncoder
) -> bytes:
    """Sign a message with a given signing key."""
    signed = signing_key.sign(message, encoder=encoder)
    return signed.signature


def sign_file(file_name: Path) -> None:
    """Entrypoint to digital signature program."""
    # Generate a new signing key
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key
    verify_key_bytes = verify_key.encode()

    with file_name.open("rb") as f:
        message = f.read()

    signed = sign(message, signing_key)

    output_file = file_name.with_suffix(".sig")
    verify_key_file = file_name.with_suffix(".key")

    with output_file.open("wb") as f:
        f.write(signed)

    with verify_key_file.open("wb") as f:
        f.write(verify_key_bytes)

    print(f"Signed file: {output_file}")
    print(f"Public key file: {verify_key_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python sign.py <file_name>")
        sys.exit(1)
    path = Path(sys.argv[1])
    sign_file(path)
