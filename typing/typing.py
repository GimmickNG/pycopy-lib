class _Subscriptable:

    def __getitem__(self, sub):
        return self.__class__

_SubSingleton = _Subscriptable()

def TypeVar(new_type, *types):
    return None

def NewType(new_type, base_type):
    return base_type

class Any: pass
Text = str
class NoReturn: pass
ClassVar = _SubSingleton
Union = _SubSingleton
Optional = _SubSingleton
Generic = _SubSingleton
Literal = _SubSingleton
TypedDict = _SubSingleton
Final = _SubSingleton
class Hashable: pass
class Awaitable: pass
class Coroutine: pass
class AsyncIterable: pass
class AsyncIterator: pass
class Iterable: pass
class Iterator: pass
class Reversible: pass
class Sized: pass
class Container: pass
class Collection: pass
Callable = _SubSingleton
AbstractSet = _SubSingleton
MutableSet = _SubSingleton
Mapping = _SubSingleton
MutableMapping = _SubSingleton
Sequence = _SubSingleton
MutableSequence = _SubSingleton
class ByteString: pass
Tuple = _SubSingleton
List = _SubSingleton
class Deque: pass
Set = _SubSingleton
FrozenSet = _SubSingleton
class MappingView: pass
class KeysView: pass
class ItemsView: pass
class ValuesView: pass
class ContextManager: pass
class AsyncContextManager: pass
Dict = _SubSingleton
DefaultDict = _SubSingleton
class Counter: pass
class ChainMap: pass
class Generator: pass
class AsyncGenerator: pass
class Type: pass
IO = _SubSingleton
TextIO = IO[str]
BinaryIO = IO[bytes]

AnyStr = TypeVar("AnyStr", str, bytes)

class NamedTuple:
    def __init__(self, *args):
        for key, index in self.__class__.__dict__.items():
            if isinstance(index, int):
                setattr(self, key, args[index])        
    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, ', '.join("{0}={1}".format(key, value) for key, value in self.__dict__.items()))

def cast(typ, val):
    return val


def _overload_dummy(*args, **kwds):
    """Helper for @overload to raise when called."""
    raise NotImplementedError(
        "You should not call an overloaded function. "
        "A series of @overload-decorated functions "
        "outside a stub module should always be followed "
        "by an implementation that is not @overload-ed."
    )


def overload(fun):
    return _overload_dummy
