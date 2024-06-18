class _Subscriptable:

    def __getitem__(self, sub):
        return None

_SubSingleton = _Subscriptable()

def TypeVar(new_type, *types):
    return None

class Any: pass
Optional = _SubSingleton
Tuple = _SubSingleton
List = _SubSingleton
Dict = _SubSingleton
DefaultDict = _SubSingleton

class Type: pass
AnyStr = TypeVar("AnyStr", str, bytes)

class Self: pass