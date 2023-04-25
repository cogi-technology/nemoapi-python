from typing import Union
from nacl.encoding import RawEncoder, HexEncoder, Base64Encoder
from hashlib import sha256 as hashlib_sha256

'''
ECDSA: secp256k1 Bitcoin
'''
from typing import Union
from coincurve.keys import PrivateKey, PublicKey

'''
EDDSA: Ed25519 sodium
'''
from nacl.signing import SigningKey, VerifyKey, SignedMessage
from nacl.bindings import crypto_sign_BYTES

def sha256(data: bytes) -> bytes:
    return hashlib_sha256(data).digest()

class ECDSA:
    prv: PrivateKey = None
    pub: PublicKey = None

    def __init__(self, prv: bytes = None, pub: bytes = None) -> None:
        if prv != None:
            self.prv = PrivateKey(prv)
            self.pub = self.prv.public_key.format(compressed=False)
            return
        if pub != None:
            self.pub = PublicKey(pub)
            return
        assert("Invalid prv, pub")

    @staticmethod
    def generate(encoder=RawEncoder) -> tuple:
        prv = PrivateKey()
        return (encoder.encode(prv.secret), encoder.encode(prv.public_key.format(compressed=False)))

    @staticmethod
    def from_prv(key: bytes):
        return ECDSA(key)
    
    @staticmethod
    def from_pub(key: bytes):
        return ECDSA(pub=key)
    
    def sign(self, data: bytes, encoder=RawEncoder) -> Union[bytes,str]:
        signature = self.prv.sign(data, hasher=sha256)
        return encoder.encode(signature)

    def verify(self, data: bytes, sig: bytes) -> bool:
        return self.pub.verify(sig, data, hasher=sha256)

class EDDSA:
    prv: SigningKey = None
    pub: VerifyKey = None

    def __init__(self, prv: bytes = None, pub: bytes = None) -> None:
        if prv != None:
            self.prv = SigningKey(prv)
            self.pub = self.prv.verify_key
            return
        if pub != None:
            self.pub = VerifyKey(pub)
            return
        assert("Invalid prv, pub")

    @staticmethod
    def generate(encoder=RawEncoder) -> tuple:
        prv = SigningKey.generate()
        return (encoder.encode(prv.__bytes__()), encoder.encode(prv.verify_key.__bytes__()))

    @staticmethod
    def from_prv(key: bytes):
        return EDDSA(key)
    
    @staticmethod
    def from_pub(key: bytes):
        return EDDSA(pub=key)
    
    def sign(self, data: bytes, encoder=RawEncoder) -> Union[bytes,str]:
        data = sha256(data)
        signature: SignedMessage = self.prv.sign(data)        
        return encoder.encode(signature.signature)

    def verify(self, data: bytes, sig: bytes) -> bool:
        data = sha256(data)
        return self.pub.verify(data, sig) != 0

'''
Cross EDDSA, ECDSA
'''
def verify(public_key: bytes, data: bytes, signature: bytes) -> bool:
    try:
        if len(signature) == crypto_sign_BYTES:
            return EDDSA.from_pub(public_key).verify(data, signature)
        return ECDSA.from_pub(public_key).verify(data, signature)
    except Exception as e:
        return False