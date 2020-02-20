from typing import List
from purescripto.ffi_utilities import auto_link_repo


def solve(package_name: str, versions: List[int]):
    if package_name == 'purescript-prelude':
        return auto_link_repo(
            r"https://github.com/purescript-python/purescript-prelude.py")
    raise NotImplementedError
