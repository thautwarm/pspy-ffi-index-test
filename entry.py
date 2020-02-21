from typing import List
from purescripto.ffi_utilities import auto_link_repo


_repo_link_map = {
    'prelude': r"https://github.com/purescript-python/purescript-prelude.py",
    'effect': r"https://github.com/purescript-python/purescript-effect.py",
}

def solve(package_name: str, versions: List[int]):
    repo_link = _repo_link_map.get(package_name)
    if repo_link:
        repo = auto_link_repo(repo_link)
        return repo.working_dir
    raise NotImplementedError("package {} is not supported by this mirror".format(package_name))
