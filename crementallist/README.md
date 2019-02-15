# Cremental List

Extension of default python list. Adds an active index to use as a list's bookmark
Includes bonds-wise safeties for incrementing/decrementing

##  Installation

```
pip install cremental_list
```

## Usage

Regular startup

```python
>>> from crementallist import CrementalList
>>> crelist = CrementalList(['zero', 'one', 'two'])
>>> crelist.ndx()
0
>>> crelist.active()
'zero'
>>> crelist.increment()
>>> crelist.increment()
>>> crelist.active()
'two'
>>> crelist.increment()
>>> crelist.active()
'two'
```

## Features

* Non-obtrusive to list functionality
    * All enhancements are done without modifying original list object 

* Empty list tolerance
    * All Cremental List functions simply return None if a list starts/becomes []
    
* 100% self-contained
    * Dependencies-schamendancies


## Functions

######init(seq, increment_key='+', decrement_key='-', raise_bounds_error=False)
seq: Default list argument. CrementalList({}) to build
increment_key: Default key used by crement to call increment()
decrement_key: Default key used by crement to call decrement()
raise_bounds_error: Raise IndexError if attempting to crement outside of current list bounds
                    Def False

######ndx()
Returns current tracking index int, within base list ndx range

#######active()
Returns active list item, based on self.ndx

######set_ndx(new_ndx: int) -> None
Attempts to set _get_active ndx.
()()If Raises a Value Error if given ndx is outside list ndx

######crement(crementer, return_value=False) -> Optional[int]:
Attempts to call appropriate function based off given crementer key
Attempts to set active ndx. Raises a Value Error if given ndx is outside list ndx

######increment()
Attempt to increment .ndx by 1, checking against current upper bound.
By default respects list bounds (will not over increment), but if raise_bounds_error is True,
raises IndexError

######decrement()
Attempt to decrement .ndx by 1, checking against current lower bound.
By default respects list bounds (will not over decrement), but if raise_bounds_error is True,
raises IndexError

## Todos
* Return_new_active option on increment/decrement
* Negative index acceptance in set_ndx
