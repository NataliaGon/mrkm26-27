from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization

alice_private_key = x25519.X25519PrivateKey.generate()
alice_public_key = alice_private_key.public_key()

print("Alice key pair generated")

bob_private_key = x25519.X25519PrivateKey.generate()
bob_public_key = bob_private_key.public_key()

print("Bob key pair generated")

alice_pub_bytes = alice_public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
bob_pub_bytes = bob_public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

print("\nPublic keys exchanged via network:")
print("Alice Public Key (hex):", alice_pub_bytes.hex())
print("Bob Public Key (hex):  ", bob_pub_bytes.hex())

alice_shared_secret = alice_private_key.exchange(bob_public_key)

print("\nAlice derived shared secret:")
print("Alice Secret (hex):", alice_shared_secret.hex())

bob_shared_secret = bob_private_key.exchange(alice_public_key)

print("\nBob derived shared secret:")
print("Bob Secret (hex):  ", bob_shared_secret.hex())

is_equal = (alice_shared_secret == bob_shared_secret)

print("\nComparison result:")
print("Shared secrets are equal:", is_equal)