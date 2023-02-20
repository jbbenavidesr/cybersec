from nacl.signing import SigningKey, VerifyKey


def main():
    # Generate a new signing key
    signing_key = SigningKey.generate()

    # Sign a message with the signing key
    signed = signing_key.sign(b"Message")

    # Obtain the verify key for a given signing key
    verify_key = signing_key.verify_key

    # Serialize the verify key to send it to a third party
    verify_key_bytes = verify_key.encode()

    # Create a verify key from the hex string
    verify_key = VerifyKey(verify_key_bytes)

    verify_key.verify(signed)

    print(signed.message)
    print(signed.signature)


if __name__ == "__main__":
    main()
