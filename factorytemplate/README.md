# Factory Template

Side loaded factory template, used to store and create unique memory ID objects

##  Usage

```python
from factorytemplate import build               # pointer to init'd factory object
from factorytemplate import TypeADocumentation  # Optional documentation for objects    

type_a_1: TypeADocumentation = build.new_type_a_object()
type_a_2: TypeADocumentation = build.new_type_a_object()
```
## Features

* Versitility
    * Dedicated dataclass objects, function classes, and sub types can all be integrated into the
    template 

* Flexibility
    * Self contained nature means package can be imported and moved across projects with minimal 
    issues

* Nonobtrusivity
    * set and forget, just call build.new_x_obj

## File roles

##### __init__.py

Contains 3 types of classes
* Importable documentation schematics
    * Used to import 
    * TypeADocumentation, TypeBDocumentation
    
* Inherit point for specific factories
    * Add new factories to Obj type inheretance
    * _Factory(TypeAFactory, TypeBFactory)
    
* Single init'd pointer to factory, to be imported
    * Called by higher class/object in need of unique data objects
    * factorytemplate.build = _Factory() 

##### _type_x_.py

Object specific files. contains 2 types of classes
* Object actual, contains all needed functions and variables
    * At this point, format depends entirely on needed use

* Object specific factory, with any needed setup or config required to prepare object for the 
'real world'
    * To be inhereted by __init__._Factory
    
##### _z_base_engine.py

* Optional baseline engine for data objects
    * Self contained, include all functions and documentation. Nothing but _type_x.py should import
    * Recommend one base_engine per package, either parallel or sub packages

##### _z_documentation

External documentation for specific data objects
* Separate file, so can be imported by _type_x.py and TypeXDocumentation pointer from __init__.py
