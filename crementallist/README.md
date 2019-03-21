# CrementalList

Extension of default list obj. Stores and preserves a boundwise bookmarking index. Whole
list can be passed between objects with bookmark. Carries functions to safely set ndx,
increment, decrement, and a crementer function that takes customizable keys to increment/
decrement.

##  Installation

```
pip install crementallist
```

## Usage

Regular startup

```python
from crementallist import CrementalList
crelist = CrementalList(['zero', 'one', 'two'])
crelist.ndx()           
    # returns 0 
crelist.active()        
    # returns 'zero'

crelist.increment()     
    # ndx = 1
crelist.increment()     
    # ndx = 2
crelist.active()        
    # returns 'two'

crelist.increment()     
    # tries to set +1 but not really because it'd be out of bounds so still 2
crelist.active()        
    # returns 'two'
```

```python
from crementallist import CrementalList
crelist = CrementalList(['zero', 'one', 'two'], raise_bounds_error=True)
crelist.set_ndx(7, raise_bounds_error=False)    # Set index to 7, suppress out of bounds errors

keys_to_send = ['-', '+']
crelist.crement(keys_to_send[0])    # Send decrementer key  
crelist.crement(keys_to_send[1])    # Send incrementer key 

crelist.increment()
```

## Features

* Non-obtrusive to list functionality
    * All enhancements are done without modifying original list object 

* Empty list tolerance
    * Cremental List Get functions simply return None if a list starts/becomes []
    
* 100% self-contained
    * Dependencies-schamendancies


## Functions

#####init(seq, increment_key='+', decrement_key='-', raise_bounds_error=False)
 - seq: 
    Mutable Sequence to track
 - increment_key: 
    Key used by crement() to increment bookmark index by one
 - decrement_key
    Key used by crement() to decrement bookmark index by one
 - raise_bounds_error:
    Optional attribute to raise errors on Out of Bounds bookmark index attempts

#####ndx()
Returns current active bookmark index, or None if list is []

#####active()
Get current active item, based off bookmark index, or None if list is []

#####set_ndx(new_ndx: int, raise_bounds_error: bool = None) -> None
Attempts to set active ndx. Negatives are treated as typical inverse list indexes. By
default, indexes over the limit are treated as [-1]
 - new_ndx:
    Desired bookmark index
 - raise_bounds_error:
    Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
    class-wide raise_bounds_error, but can be force set if needed

#####def crement(crementer_key, return_ndx=False, raise_bounds_error: bool = None) -> Optional[int]
Centralized function to call increment/decrement with a given key, crementer_key. Attempts
to use key, raises KeyError if does not match keys from init. Can return the new active ndx
 - crementer_key:
    Key to pass, from initialized incrementer/decrementer
 - return_ndx:
    Optional attribute to return newly set index
 - raise_bounds_error:
    Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
    class-wide raise_bounds_error, but can be force set if needed

#####increment(return_ndx=False, raise_bounds_error: bool = None) -> Optional[int]
Safe manual call to increment bookmark index by one
 - return_ndx:
    Optional attribute to return newly set index
 - raise_bounds_error:
    Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
    class-wide raise_bounds_error, but can be force set if needed

#####decrement(return_ndx=False, raise_bounds_error: bool = None) -> Optional[int]
Safe manual call to decrement bookmark index by one

 - return_ndx:
    Optional attribute to return newly set index
 - raise_bounds_error:
    Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
    class-wide raise_bounds_error, but can be force set if needed