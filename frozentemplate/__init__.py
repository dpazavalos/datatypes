"""Emulation of 3.7 Dataclasses frozen attribute, with soft lock for immutability
Allows immutable dataclass style objects for pre 3.7 applications. Set and forget about constants
Once init completes, builtin setattr and delattr will throw a SyntaxError on attempted use

(freeze_post_init=False) disables auto-freeze. Call .freeze_now to manually lock class attributes
"""


class Frozen:
    """These should never change mid-run. Once init'd, _frozen prevents any attr changes"""

    _frozen = False

    def __init__(self, freeze_post_init=True):

        # Enable all class attributes. By default, _freeze enables and locks @end of init

        if freeze_post_init:
            self._frozen = True

    def freeze_now(self):
        self._frozen = True

    def __setattr__(self, item, value):
        """Pre 3.7 emulation of frozen dataclasses. Soft mutation prevention"""
        if self._frozen:
            raise SyntaxError("Consider Constants obj immutable, do not modify!")
        self.__dict__[item] = value

    def __delattr__(self, item):
            """Pre 3.7 emulation of frozen dataclasses. Soft mutation prevention"""
            if self._frozen:
                raise SyntaxError("Consider Constants obj immutable, do not modify!")
            del self.__dict__[item]

