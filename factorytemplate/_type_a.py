from factorytemplate._z_documentation import TypeADoc as _TypeADoc


class TypeA(_TypeADoc):
    """
    Type A Configuration of Base engine.
    """

    def __init__(self, ):
        """init calls reset, a common clear and set function"""
        self.reset()

    def reset(self, ):
        """clear and set class attributes. External accessibility emulating a factory reset.
        use this if a new mem-unique object is not required, only fresh data points"""
        print("Type A Successfully built and returned")


class TypeAFactory:
    """Factory method to create new TypeB object"""

    @staticmethod
    def _return_type_a_object():
        new_obj = TypeA()
        return new_obj

    def new_type_a_object(self, ):
        return self._return_type_a_object()

