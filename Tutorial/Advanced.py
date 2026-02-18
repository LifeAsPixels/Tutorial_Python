from dataclasses import dataclass, field
import weakref
from typing import TypeVar, Generic, Optional
import sys

class Interning:
    '''example class description'''
    value = 0

    def __init__(self):
        '''init descr'''
        self.name = 'main'
    
    @staticmethod  # This decorator tells Python to ignore the 'self' requirement
    def example1():
        '''example method descr'''
        # 1. Create two identical strings at RUNTIME (compiler can't predict this)
        # Using join or multiplication prevents the compiler from pre-interning them
        part1 = "Binary"
        part2 = "Search"
        
        str_a = part1 + part2          # Created at runtime
        str_b = "".join([part1, part2]) # Created at runtime
        
        # Check 1: Without interning
        print(f"Are they the same object? {str_a is str_b}") # Result: False
        
        # 2. Now, let's manually intern them
        interned_a = sys.intern(str_a)
        interned_b = sys.intern(str_b)
        
        # Check 2: With interning
        print(f"Are interned versions the same? {interned_a is interned_b}") # Result: True

    def example2(self):
        return 5
class Treerecord:
    '''
    A model class for btree records intended to be used with a 
    manager/controller class
    '''
    
    '''
    This tells Python to use a fixed-size array instead of a 
    dictionary with as a hashmap with variable width
    saves ~50-70% on memory cost
    '''
    __slots__ = ('key', 'left', 'right')
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

'''
This class model is a great example using weak references and 
@dataclass wrapper
    slots = true
        allows for a special syntax for using this class as a 
        model of a record for data to use a fixed-size array instead of a 
        dictionary

this IntStr line declares that when used a var will be either one
and it will stay the one it was declared as
'''
IntStr = TypeVar('IntStr', int, str)
# an alternate way to implement slots
@dataclass(slots=True)
class SomeDataRecord(Generic[IntStr]):
    '''
    A model class for linked list records intended to be used with a 
    manager/controller class
    this could be a singly or doubly linked list as an example of how an 
    attribute would be a ref to another record-object of the same type
    '''
    # any type
    key: any
    # any type default None
    value: any = None
    # this var will be int or str type and then stay that way 
    # or it defaults to None
    intra_system_same_type_var: Optional[IntStr] = None
    # this var is a weak reference to prevent the garbage collector from
    # counting this reference (counting it prevents it from mem deletion)
    _child_ref: weakref.ReferenceType = field(init=False, repr=False, default=None)
    # We use field(init=False) because we handle parent manually in __post_init__
    _parent_ref: weakref.ReferenceType = field(init=False, repr=False, default=None)

    def set_parent(self, record):
        if record is not None:
            self._parent_ref = weakref.ref(record)
        else:
            self._parent_ref = None

    def set_child(self, record):
        if record is not None:
            self._child_ref = weakref.ref(record)
        else:
            self._child_ref = None

    @property
    def parent(self):
        """Returns the actual object from the weak reference."""
        return self._parent_ref() if self._parent_ref else None

    @property
    def child(self):
        """Returns the actual object from the weak reference."""
        return self._child_ref() if self._child_ref else None

'''
    frozen=true
        makes the data structure immutable creating these effects

        Hashing: It automatically generates a __hash__ method, allowing you 
        to use your objects as keys in a dictionary or elements in a set.

        Comparison: It generates O(1) to O(n) comparison methods 
        (__eq__, __lt__) automatically based on the data fields.

        Memory: While it doesn't save as much as __slots__ on its own, you 
        can combine frozen=true with 'slots=True'
'''
@dataclass(frozen=True, slots=True)
class GeoLocation:
    latitude: float
    longitude: float
    label: str = "Unlabeled Point"