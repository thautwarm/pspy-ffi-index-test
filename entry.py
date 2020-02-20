from typing import List
from purescripto.ffi_utilities import auto_link_repo


def solve(package_name: str, versions: List[int]):
    if package_name == 'prelude':
        repo = auto_link_repo(
            r"https://github.com/purescript-python/purescript-prelude.py")
        return repo.working_dir
    raise NotImplementedError
