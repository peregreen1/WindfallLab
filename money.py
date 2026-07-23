"""
Utilities for working with monetary values in WindfallLab.

The project uses Decimal for all monetary calculations to ensure
deterministic and precise financial accounting.
"""

from __future__ import annotations

from decimal import Decimal


ZERO = Decimal("0")
ONE = Decimal("1")


def to_decimal(value: int | float | str | Decimal) -> Decimal:
    """
    Convert a numeric value to a Decimal.

    Floats are converted through their string representation to avoid
    binary floating-point artifacts.

    Parameters
    ----------
    value
        The value to convert.

    Returns
    -------
    Decimal
        The converted Decimal value.
    """
    if isinstance(value, Decimal):
        return value

    return Decimal(str(value))