# coding: utf-8


from __future__ import absolute_import

from nemo_api.dsa import EDDSA, ECDSA, Base64Encoder, verify

def dsa(*args):
  try:
    return _dsa(*args)
  except Exception as e:
    return str(e)

def _dsa(algorithm, action, key: str=None, message: str=None, signature: str=None):
  o = EDDSA
  if algorithm == 'secp256k1':
    o = ECDSA
  if action == 'generate':
    (prv, pub) = o.generate(Base64Encoder)
    return "%s %s" % (prv.decode(), pub.decode())

  assert key != None
  assert message != None
  key = Base64Encoder.decode(key)
  message = Base64Encoder.decode(message)

  if action == 'sign':
    sig = o(key).sign(message, Base64Encoder)
    return "Signature: %s" % sig.decode()

  assert signature != None
  signature = Base64Encoder.decode(signature)
  if action == 'verify':
    return verify(key, message, signature)