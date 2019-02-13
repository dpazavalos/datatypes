"""
Extension of default list obj. Adds an active index to use as a list's bookmark
Includes safeties for incrementing/decrementing
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

        self.ndx: int = 0
        """Active index"""

        self.active: any = None
        """Active item from given list, based on active index"""

        self.raise_bounds_error = raise_bounds_error
        """Raise IndexError if attempting to crement outside of current list bounds. Def False"""

        self._set_callables()

    # Public accessible functions

    def set_ndx(self, new_ndx: int) -> None:
        """Attempts to set active ndx.
        Raises a Value Error if given ndx is outside list ndx"""
        if self._is_loaded():
            if new_ndx < 0 or new_ndx > self.__len__():
                raise ValueError(f'new ndx is outside of list length 0-{self.__len__()}!')
            else:
                self.ndx = new_ndx
                self._set_callables()

    def crement(self, crementer, return_ndx=False) -> int:
        """Attempts to use cremementer key to call appropriate crementer function
        Optional return_ndx to return new ndx"""
        if self._is_loaded():
            if crementer not in self._menters:
                raise KeyError(f"Invalid crementer! \n {self._menters}")
            self._menters[crementer]()
            if return_ndx is True:
                return self.ndx

    def increment(self) -> None:
        """Call ndx_i if safe"""
        if self._is_loaded():
            if self.ndx + 1 < self.__len__():
                self._ndx_i()
            elif self.raise_bounds_error is True:
                raise IndexError("Attempted to increment above upper bound!")

    def decrement(self) -> None:
        """Call ndx_d if safe, """
        if self._is_loaded():
            if self.ndx - 1 >= 0:
                self._ndx_d()
            elif self.raise_bounds_error is True:
                raise IndexError("Attempted to decrement below lower bound!")

    # Actual incrementer/decrementer

    def _ndx_i(self) -> None:
        """Increment ndx +1, reset callables"""
        if self._is_loaded():
            self.ndx += 1
            self._set_callables()

    def _ndx_d(self):
        """Decrement ndx -1, reset callables"""
        if self._is_loaded():
            self.ndx -= 1
            self._set_callables()

    # Internal Get/Setters

    def _set_callables(self) -> None:
        """Sets callable values, based on active ndx"""
        if self._is_loaded():
            self.active = self._get_active()

    def _get_active(self) -> any:
        """Returns item from list using _get_active ndx"""
        if self._is_loaded():
            return self[self.ndx]

    # Internal Maintenance

    def _is_loaded(self) -> bool:
        """Used to prevent CrementalList functions if list is []
        Centralized call for _ensure_upper_bounded"""
        if self.__len__() == 0:
            self._deactivate_callables()
            return False
        self._ensure_upper_bounded()
        return True

    def _ensure_upper_bounded(self):
        """Ensures ndx is not overbounded due to reduced list length"""
        if self.ndx is not None and self.ndx >= self.__len__():
            self.ndx = self.ndx > self.__len__()

    def _deactivate_callables(self):
        """Used to disable callable attributes, if list becomes []"""
        self.ndx = None
        self.active = None
