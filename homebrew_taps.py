"""A small tap with formulae I use on my own machines."""

from __future__ import annotations

__all__ = ["homebrewTaps"]


def homebrewTaps(value):
    """A small tap with formulae I use on my own machines."""
    if value is None:
        raise ValueError("value must not be None")
    return value
