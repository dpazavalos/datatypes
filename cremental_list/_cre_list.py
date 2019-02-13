"""
Extension of default python list. Adds an active index to use as a list's bookmark
Includes bonds-wise safeties for incrementing/decrementing
"""


class CrementalList(list):
    """
    Extension of default list obj. Adds an active index to use as a list's bookmark
    ndx is currently active index
    active is currently active list item, based off ndx
    increment()/decrement() Safely increment/decrement ndx
    Safely increment/decrement by calling increment()/decrement(), or by sending key '+'/'-' to
    crement(['+' or '-']) can be used to call to increment()/decrement(). (Keys set in init)

    optional raise_bounds_error to raise IndexError if increment/decrement would exceed bounds,
    otherwise will simply not break past bounds
    """

    def __init__(self, seq, increment_key='+', decrement_key='-', raise_bounds_error=False):

        super().__init__(seq)
        self._menters: dict = {increment_key: self.increment,
                               decrement_key: self.decrement}
        """Using given incrementer and decrementer keys as calls for respective functions"""

        self._ndx: int = 0
        """Protected active index"""

        self._active: any = None
        """Protected active item from given list, based on active index"""

        self._raise_bounds_error = raise_bounds_error
        """Raise IndexError if attempting to ndx outside of current list bounds. Default False"""

        self._set_callables()

    # Public accessible functions

    def ndx(self):
        """Current index. If list is [], returns None"""
        if self._is_loaded():
            return self._ndx

    def active(self):
        """Active item by index. if list is [], returns None"""
        if self._is_loaded():
            return self._get_active()

    def set_ndx(self, new_ndx: int) -> None:
        """Attempts to set active ndx.
        Raises a Value Error if given ndx is outside list ndx"""
        if self._is_loaded():
            if new_ndx < 0:
                # todo add negative indexing
                if self._raise_bounds_error:
                    raise ValueError(f'new ndx is under 0!')
                else:
                    new_ndx = 0
            elif new_ndx >= self.__len__():
                if self._raise_bounds_error:
                    raise ValueError(f'new ndx is outside of list length 0-{self.__len__()}!')
                else:
                    new_ndx = self.__len__() - 1
            else:
                self._ndx = new_ndx
                self._set_callables()

    def crement(self, crementer_key, return_ndx=False) -> int:
        """Attempts to use cremementer key to call appropriate crementer function
        Optional return_ndx to return new ndx"""
        # todo return new active=False
        if self._is_loaded():
            if crementer_key not in self._menters:
                raise KeyError(f"Invalid crementer! \n {self._menters}")
            self._menters[crementer_key]()
            if return_ndx is True:
                return self._ndx

    def increment(self) -> None:
        """Call ndx_i if safe"""
        if self._is_loaded():
            if self._ndx + 1 < self.__len__():
                self._ndx_i()
            elif self._raise_bounds_error is True:
                raise IndexError("Attempted to increment above upper bound!")

    def decrement(self) -> None:
        """Call ndx_d if safe, """
        if self._is_loaded():
            if self._ndx - 1 >= 0:
                self._ndx_d()
            elif self._raise_bounds_error is True:
                raise IndexError("Attempted to decrement below lower bound!")

    # Actual incrementer/decrementer

    def _ndx_i(self) -> None:
        """Increment ndx +1, reset callables"""
        self._ndx += 1
        self._set_callables()

    def _ndx_d(self):
        """Decrement ndx -1, reset callables"""
        self._ndx -= 1
        self._set_callables()

    # Internal Get/Setters

    def _set_callables(self) -> None:
        """Sets callable values, based on active ndx"""
        if self._is_loaded():
            self._active = self._get_active()

    def _get_ndx(self)-> int:
        return self._ndx

    def _get_active(self) -> any:
        """Returns item from list using _get_active ndx"""
        return self[self._ndx]

    # Internal Maintenance

    def _is_loaded(self) -> bool:
        """Used to prevent CrementalList functions if list is []
        Centralized call for _ensure_bounded"""
        if self.__len__() == 0:
            self._deactivate_callables()
            return False
        self._ensure_bounded()
        return True

    def _ensure_bounded(self):
        """Ensures ndx is activated and not out of bounds"""
        if not self._ndx or self._ndx < 0:
            self._ndx = 0
        if self._ndx >= self.__len__():
            self._ndx = self.__len__() - 1

    def _deactivate_callables(self):
        """Used to disable callable attributes, if list becomes []"""
        self._ndx = None
        self._active = None
