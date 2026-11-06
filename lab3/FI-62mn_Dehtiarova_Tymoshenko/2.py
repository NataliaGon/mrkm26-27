from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.exceptions import InvalidSignature


private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

print("1. Key pair generated.")


message = "This is a test message for digital signature verification."
message = message.encode("utf-8")

print("\n2. Test message:")
print(message.decode("utf-8"))


signature = private_key.sign(message)

print("\n3. Digital signature created.")
print("Signature:", signature.hex())


print("\n4. Verification of the original message:")

try:
    public_key.verify(signature, message)
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")


modified_message = "This is a modified test message.".encode("utf-8")

print("\n5. Verification of the modified message:")

try:
    public_key.verify(signature, modified_message)
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid: message was modified.")


other_private_key = Ed25519PrivateKey.generate()
other_public_key = other_private_key.public_key()

print("\n6. Verification with another public key:")

try:
    other_public_key.verify(signature, message)
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid: another public key was used.")