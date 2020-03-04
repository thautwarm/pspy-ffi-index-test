This is a PureScript FFI provider mirror for the Python backend.

Making such a mirror is simple, by implementing following interfaces:
1. Providing an `entry.py` in the Git repo's root.
2. In `entry.py`, provide a function `solve(package_name: str, versions: List[int]) -> str`,

which takes

- the name of package.  
  e.g., for `purescript-prelude`, you'll receive `prelude`.

- the version parts
  
  e.g., for `v1.1.1`, you'll get `[1, 1, 1]`.

and return

- a URL of a Git repo providing the Python FFI files.

  e.g., for [purescript-console](https://github.com/purescript/purescript-console), we can make this [purescript-console.py](`https://github.com/purescript-python/purescript-console.py`) for former's Python FFI files).


## Update Mirror

`pspy --update` will automatically synchronize the mirror you selected in `pure-py.json`.