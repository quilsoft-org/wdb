from wdb import Wdb


class Pdb(Wdb):
    pass


def import_from_stdlib(name):
    """Copied from pdbpp https://bitbucket.org/antocuni/pdb"""
    import code  # arbitrary module which stays in the same dir as pdb
    import os
    import types

    stdlibdir, _ = os.path.split(code.__file__)
    pyfile = os.path.join(stdlibdir, name + ".py")
    result = types.ModuleType(name)
    exec(compile(open(pyfile).read(), pyfile, "exec"), result.__dict__)
    return result


old = import_from_stdlib("pdb")
