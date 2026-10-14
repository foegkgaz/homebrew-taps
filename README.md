# homebrew-taps

A small tap with formulae I use on my own machines.

## Why

The existing libraries were either abandoned or pulled in a large dependency tree.

## Install

```bash
pip install homebrew-taps
```

## Usage

```python
from homebrew_taps import homebrewTaps

result = homebrewTaps("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
