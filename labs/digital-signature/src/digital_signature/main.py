"""Simple program to sign and verify a file."""
from pathlib import Path

from nacl.encoding import Base64Encoder, Encoder, RawEncoder
from nacl.signing import SigningKey, VerifyKey


def sign(
    message: bytes, signing_key: SigningKey, encoder: Encoder = RawEncoder
) -> bytes:
    """Sign a message with a given signing key."""
    signed = signing_key.sign(message, encoder=encoder)
    return signed.signature


def verify(message: bytes, signature: bytes, verify_key: VerifyKey) -> bool:
    """Verify a message with a given verify key."""
    try:
        verify_key.verify(message, signature)
        return True
    except Exception:
        return False


def main(file_name: Path) -> None:
    """Entrypoint to digital signature program."""
    # Generate a new signing key
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key
    verify_key_bytes = verify_key.encode(encoder=Base64Encoder)

    with open(file_name, "rb") as f:
        message = f.read()

    signed = sign(message, signing_key, encoder=Base64Encoder)

    output_file_name = file_name.with_suffix(".sig")
    verivy_key_file_name = file_name.with_suffix(".key")

    with open(output_file_name, "wb") as f:
        f.write(signed)

    with open(verivy_key_file_name, "wb") as f:
        f.write(verify_key_bytes)

    print(f"Signed file: {output_file_name}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py <file_name>")
        sys.exit(1)
    path = Path(sys.argv[1])
    main(path)
