"""Simple script for testing falcon algorithm of post-quantum cryptography."""
import falcon

def main():
    """Main function."""
    # Generate public and private keys for Falcon 512
    secret_key = falcon.SecretKey(512)
    public_key = falcon.PublicKey(secret_key)

    # Sign a message
    message = b'Hello World!'
    signature = secret_key.sign(message)
    print(signature)

    # Verify the signature
    assert public_key.verify(message, signature)
    print('Signature is valid!')


if __name__ == '__main__':
    main()
