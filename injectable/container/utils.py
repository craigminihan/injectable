import sys
from os import DirEntry
from os.path import basename, dirname, splitext
from pathlib import Path
from typing import Optional, Union


def find_module_name(
    filepath: Union[DirEntry, str], innermost: bool = False
) -> Optional[str]:
    """
    Utility function to find the Python module name of a python file.

    :param filepath:
        The absolute filepath as a DirEntry object or path string.
    :param innermost:
        (default: False) By default the outermost possible module name is returned.
        When this flag is set to True, the first found, innermost possible module name
        is then returned without further looking.
    :return:
        The module name string or None if no module was found for the specified
        filepath.
    """
    print("\n---- find_module_name call start ----\n")
    if isinstance(filepath, DirEntry):
        filepath = filepath.path

    valid_module_name = None
    module_name = splitext(basename(filepath))[0]
    full_path = Path(dirname(filepath))
    raise_exception = None
    if (
        str(full_path)
        == "D:\\a\injectable\injectable\examples\cyclic_dependency\services"
    ):
        raise_exception = "barra barra a"
    elif (
        str(full_path)
        == "D:\a\injectable\injectable\examples\cyclic_dependency\services"
    ):
        raise_exception = "barra a"
    elif (
        str(full_path)
        == "D:\\a\\injectable\\injectable\\examples\\cyclic_dependency\\services"
    ):
        raise_exception = "full barra"
    elif (
        str(full_path)
        == "D:\\\\a\\\\injectable\\\\injectable\\\\examples\\\\cyclic_dependency\\\\services"
    ):
        raise_exception = "full double barra"
    print(f"sys.path={sys.path}")
    at_root = False
    i = 0
    while not at_root:
        print(f"loop_iteration={i}")
        print(f"module_name={module_name}")
        print(f"full_path={full_path}")
        if str(full_path) in sys.path:
            if innermost:
                return module_name
            else:
                valid_module_name = module_name
        module_name = f"{basename(full_path)}.{module_name}"
        at_root = full_path.parent == full_path.parent.parent
        print(f"at_root={at_root}")
        full_path = Path(full_path.parent)
    print("\n---- find_module_name call end ----\n")
    if raise_exception:
        raise RuntimeError(raise_exception)
    return valid_module_name
