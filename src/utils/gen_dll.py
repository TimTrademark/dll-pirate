import pefile
import os

def gen_def(dll_name: str):
    result = ""
    dll = pefile.PE(dll_name)
    dll_basename = os.path.splitext(dll_name)[0]
    result += "EXPORTS\n"
    for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
        if export.name:
            result += '{}={}.{} @{}\n'.format(export.name.decode(), dll_basename, export.name.decode(), export.ordinal)
    return result