"""
Extension of default list obj. Stores and preserves a boundwise bookmarking index. Whole
list can be passed between objects with bookmark.
"""
from typing import Optional


class CrementalList(list):
    """
    Extension of default list obj. Stores and preserves a boundwise bookmarking index. Whole
    list can be passed between objects with bookmark. Carries functions to safely set ndx,
    increment, decrement, and a crementer function that takes customizable keys to increment/
    decrement.
    """

    def __init__(self, seq, increment_key: any = '+', decrement_key: any = '-', raise_bounds_error=False):
        """
        Extension of default list obj. Stores and preserves a boundwise bookmarking index. Whole
        list can be passed between objects with bookmark. Carries functions to safely set ndx,
        increment, decrement, and a crementer function that takes customizable keys to increment/
        decrement.

        Args:
            seq:
                Mutable Sequence to track
            increment_key:
                Key used by crement() to increment bookmark index by one
            decrement_key:
                Key used by crement() to decrement bookmark index by one
            raise_bounds_error:
                Optional attribute to raise errors on Out of Bounds bookmark index attempts
        """

        super().__init__(seq)
        self._menters: dict = {increment_key: self._ndx_i,
                               decrement_key: self._ndx_d}
        """Using given incrementer and decrementer keys as calls for respective functions"""

        self._ndx: int = 0
        """Protected active index"""

        self._raise_bounds_error = raise_bounds_error
        """Raise IndexError if attempting to ndx outside of current list bounds. Default False"""

    # Public accessible functions

    def ndx(self) -> any:
        """
        Get current active bookmark index

        Returns:
                Active bookmark index, or None if len=0
        """
        if not self._is_loaded():
            return None
        return self._ndx

    def active(self):
        """
        Get current active item, based off bookmark index

        Returns:
                Active item, or None if len=0
        """
        if not self._is_loaded():
            return None
        return self._get_active()

    def set_ndx(self, new_ndx: int, raise_bounds_error: bool = None) -> None:
        """
        Attempts to set active ndx. Negatives are treated as typical inverse list indexes. By
        default, indexes over the limit are treated as [-1]

        Arguments:
            new_ndx:
                Desired bookmark index
            raise_bounds_error:
                Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
                class-wide raise_bounds_error, but can be force set if needed
        """
        if not self._is_loaded():
            return None

        if not raise_bounds_error:
            raise_bounds_error = self._raise_bounds_error

        # Fix possible negative passed ndx
        new_ndx = self._invert_negative(new_ndx)

        # Max length check
        if not self._in_bounds(new_ndx):
            if raise_bounds_error:
                raise IndexError(f'Given ndx is over list length!')
            new_ndx = self.__len__()-1

        self._set_ndx(new_ndx)

    def crement(self, crementer_key, return_ndx=False,
                raise_bounds_error: bool = None) -> Optional[int]:
        """
        Centralized function to call increment/decrement with a given key, crementer_key. Attempts
        to use key, raises KeyError if does not match keys from init. Can return the new active ndx

        Args:
            crementer_key:
                Key to pass, from initialized incrementer/decrementer
            return_ndx:
                Optional attribute to return newly set index
            raise_bounds_error:
                Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
                class-wide raise_bounds_error, but can be force set if needed

        Returns:
            Newly set bookmark index, if return_ndx
        """
        if not self._is_loaded():
            return None

        if not raise_bounds_error:
            raise_bounds_error = self._raise_bounds_error

        try:
            new_ndx = self._menters[crementer_key]()    # Regardless of return T/F, func has to run
            return new_ndx if return_ndx else None

        except KeyError:
            raise KeyError(f"Invalid crementer! \n {self._menters}")

        except IndexError as err:
            if raise_bounds_error:
                raise err

    def increment(self, return_ndx=False, raise_bounds_error: bool = None) -> Optional[int]:
        """
        Safe manual call to increment bookmark index by one

        Args:
            return_ndx:
                Optional attribute to return newly set index
            raise_bounds_error:
                Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
                class-wide raise_bounds_error, but can be force set if needed

        Returns:
            Newly set bookmark index, if return_ndx
        """
        if not self._is_loaded():
            return None

        if not raise_bounds_error:
            raise_bounds_error = self._raise_bounds_error

        try:
            new_ndx = self._ndx_i()                 # Regardless of return T/F, function has to run
            return new_ndx if return_ndx else None

        except IndexError as err:
            if raise_bounds_error is True:
                raise err

    def decrement(self, return_ndx=False, raise_bounds_error: bool = None) -> Optional[int]:
        """
        Safe manual call to decrement bookmark index by one

        Args:
            return_ndx:
                Optional attribute to return newly set index
            raise_bounds_error:
                Raises an Index Error if given ndx is outside list boundaries. Defaults to shadow
                class-wide raise_bounds_error, but can be force set if needed

        Returns:
            Newly set bookmark index, if return_ndx
        """
        if not self._is_loaded():
            return None

        if not raise_bounds_error:
            raise_bounds_error = self._raise_bounds_error

        try:
            new_ndx = self._ndx_d()                 # Regardless of return T/F, function has to run
            return new_ndx if return_ndx else None

        except IndexError as err:
            if raise_bounds_error is True:
                raise err

    # Actual incrementer/decrementer functions. Will always return or raise something

    def _ndx_i(self) -> int:
        """Increment ndx by 1, return new ndx. Raise ValueError if OoB"""
        if self._in_bounds(self._ndx + 1):
            self._ndx += 1
            return self._ndx
        raise IndexError("Attempted to increment above upper bound!")

    def _ndx_d(self):
        """Decrement ndx by 1, return new ndx. Raise ValueError if OoB"""
        if self._in_bounds(self._ndx + 1):
            self._ndx -= 1
            return self._ndx
        raise IndexError("Attempted to decrement below lower bound!")

    # Getters/setters. These do not run checks

    def _get_ndx(self)-> int:
        """Returns current active bookmark index. List is assumed active"""
        return self._ndx

    def _get_active(self) -> any:
        """Returns item from list using _get_active ndx. List is assumed active"""
        return self[self._ndx]

    def _set_ndx(self, new_ndx: int) -> None:
        """
        Sets _ndx to new_ndx. List is assumed active

        Args:
            new_ndx: Potential new bookmark index
        """
        self._ndx = new_ndx

    # Internal Maintenance, checks

    def _is_loaded(self) -> bool:
        """Used to prevent CrementalList functions if list is empty. All main functions call this"""
        if self.__len__() == 0:
            self._deactivate_callables()
            return False
        self._ensure_active()
        return True

    def _in_bounds(self, ndx: int) -> bool:
        """Internal check to ensure a potential ndx is within bounds

        Args:
            ndx: Potential new bookmark index
        """
        return 0 <= ndx < self.__len__()

    def _ensure_active(self):
        """Ensures _ndx is activated and within bounds. List is assumed active"""
        if not self._ndx or self._ndx < 0:
            self._ndx = 0
        if self._ndx >= self.__len__():
            self._ndx = self.__len__() - 1

    def _deactivate_callables(self):
        """Used to disable callable attributes, if list becomes []"""
        self._ndx = None

    def _invert_negative(self, integer: int) -> int:
        """
        Used to find equivalent inverse index item (-1 is last item, -3 is 3rd last etc). If a non-
        negative is passed, no work is done and the same number is returned

        Args:
            integer:
                Integer to find inverse of, against self's list.

        Returns:
                Positive list index (Not bound wise!)
        """
        return integer + self.__len__() if integer < 0 else integer
