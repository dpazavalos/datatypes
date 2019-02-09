from factorytemplate._z_documentation import TypeBDoc as _TypeBDoc


class TypeB(_TypeBDoc):
    """
    Type B Configuration of Base engine; includes req argument
    """

    def __init__(self, arg):
        """init calls reset, a common clear and set function"""
        self.reset(arg)

    def reset(self, arg):
        """clear and set class attributes. External accessibility emulating a factory reset.
        use this if a new mem-unique object is not required, only fresh data points"""
        print(arg)


class TypeBFactory:
    """Factory method to create new TypeB object"""

    @staticmethod
    def _return_type_b_object(argument):
        new_obj = TypeB(arg=argument)
        return new_obj

    def new_type_b_object(self, type_b_argument):
        return self._return_type_b_object(argument=type_b_argument)
