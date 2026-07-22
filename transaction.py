"""
Immutable transaction records for WindfallLab.

A Transaction represents a completed investment action.
Transactions never change once created.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class TransactionReason(Enum):
    """The reason a transaction occurred."""

    INITIAL_DEPLOYMENT = "Initial Deployment"
    SCHEDULED_TRANCHE = "Scheduled Tranche"
    DRAWDOWN_TRIGGER = "Drawdown Trigger"
    REBALANCE = "Rebalance"
    MANUAL = "Manual"


@dataclass(frozen=True, slots=True)
class Transaction:
    """
    Represents a completed investment transaction.

    Attributes
    ----------
    date
        The execution date.
    price
        Market price per share.
    amount
        Dollar amount invested.
    shares
        Shares purchased.
    reason
        Why the purchase occurred.
    note
        Optional human-readable explanation.
    """

    date: date
    price: float
    amount: float
    shares: float
    reason: TransactionReason
    note: str = ""
