"""
Custom exceptions used throughout the WindfallLab engine.
"""


class WindfallError(Exception):
    """Base class for all WindfallLab exceptions."""


class InsufficientCashError(WindfallError):
    """Raised when attempting to invest more cash than is available."""


class InvalidTransactionError(WindfallError):
    """Raised when a transaction contains invalid data."""
