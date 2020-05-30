import sys

def caller_module(level=2):
    module_globals = sys._getframe(level).f_globals
    module_name = module_globals.get('__name__') or '__main__'
    module = sys.modules[module_name]

    print("Got module: ", module)
    return module

def caller_package(level=2):
    module = caller_module(level + 1)
    f = getattr(module, '__file__', '')
    if ('__init__.py' in f) or ('__init__$py' in f):  # empty at >>>
        # Module is a package
        print("Module is a package: ", module)
        return module
    # Go up one level to get package
    package_name = module.__name__.rsplit('.', 1)[0]

    print("Package name: ", package_name)
    return sys.modules[package_name]
