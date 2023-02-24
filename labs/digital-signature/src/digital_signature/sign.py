"""Simple program to sign and verify a file."""
from pathlib import Path

from nacl.encoding import Encoder, RawEncoder
from nacl.signing import SigningKey


def sign(
    message: bytes, signing_key: SigningKey, encoder: Encoder = RawEncoder
) -> bytes:
    """Sign a message with a given signing key."""
    signed = signing_key.sign(message, encoder=encoder)
    return signed


def sign_file(file_name: Path) -> None:
    """Entrypoint to digital signature program."""
    # Generate a new signing key
    signing_key = SigningKey.generate()

    # Get the verification key (Public key)
    verify_key = signing_key.verify_key
    verify_key_bytes = verify_key.encode()

    # Read the file to sign
    message = file_name.read_bytes()

    # Sign the message
    signed_message = sign(message, signing_key)

    # Write the signed message to a file
    signed_file = Path(f"{file_name.stem}-signed{file_name.suffix}")
    signed_file.write_bytes(signed_message)

    # Write the public key to a file
    verify_key_file = file_name.with_suffix(".key")
    verify_key_file.write_bytes(verify_key_bytes)

    # Print the file names that were created
    print(f"Signed file: {signed_file}")
    print(f"Public key file: {verify_key_file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python sign.py <file_name>")
        sys.exit(1)
    path = Path(sys.argv[1])
    sign_file(path)
