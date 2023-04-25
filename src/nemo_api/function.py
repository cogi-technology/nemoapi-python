import ujson as json, base64
from functools import singledispatch
from datetime import datetime
from decimal import Decimal
from types import GeneratorType

import logging
logger = logging.getLogger(__name__)
NoneType = type(None)

class Binary(bytes):
    @classmethod
    def fromstring(cls, data):
        return cls(base64.b64decode(data))

@singledispatch
def py2json(value):
    raise TypeError(("Can't serialise type: {0}."
                    " Add type {0} via decorator "
                     "@py2json.register({0}) ").format(type(value)))

@py2json.register(bytes)
def _(value):
    return value.decode()

@py2json.register(str)
@py2json.register(float)
@py2json.register(int)
@py2json.register(bool)
@py2json.register(NoneType)
def _(value):
    return value

@py2json.register(Decimal)
def _(value):
    return str(value)

@py2json.register(datetime)
def _(value: datetime):
    return value.isoformat()

@py2json.register(Binary)
def _(value):
    return {
        "type": "binary",
        "encoding": "base64",
        "data": base64.b64encode(value),
    }

@py2json.register(list)
@py2json.register(tuple)
@py2json.register(set)
@py2json.register(frozenset)
@py2json.register(GeneratorType)
def _(x):
    return [py2json(i) for i in x]

@py2json.register(dict)
def _(x):
    return {str(key): py2json(value) for key, value in x.items()}

def json_encode(data, default='', ensure_ascii: bool = False, **kargs) -> str:
    try:
        return json.dumps(py2json(data), ensure_ascii=ensure_ascii, **kargs)
    except Exception as e:
        logger.exception("%s %s", e, data)
        return default

def is_0x_prefixed(value: str) -> bool:
    if not isinstance(value, str):
        raise TypeError(
            "is_0x_prefixed requires text typed arguments. Got: {0}".format(repr(value))
        )
    return value.startswith("0x") or value.startswith("0X")
    
def parse_decimal(_value) -> Decimal:
    if isinstance(_value, Decimal):
        return _value
    elif isinstance(_value, float):
        return Decimal(value=str(_value))
    elif isinstance(_value, int):
        return Decimal(value=_value)
    elif isinstance(_value, str):
        if is_0x_prefixed(_value):
            return Decimal(value=int(_value, 16))
        return Decimal(value=_value)
    else:
        raise TypeError("Unsupported type.  Must be one of integer, float, or string")