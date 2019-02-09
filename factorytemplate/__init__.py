"""
Template for side load factories. factorytemplate.build points to assembled factory to reliably
build memory unique objects
"""
from factorytemplate import _type_a, _type_b, _z_documentation


class TypeADocumentation(_z_documentation.TypeADoc):
    """Externally referencable pointer to type A format documentation.  No functions
    If doc is properly built, no work needed here"""


class TypeBDocumentation(_z_documentation.TypeBDoc):
    """Externally referencable pointer to type B format documentation. No functions
    If doc is properly built, no work needed here"""


class _Factory(_type_a.TypeAFactory, _type_b.TypeBFactory):
    """Inheritor of type factories. Init by below 'build'"""


build = _Factory()
"""Actual importable factory"""
