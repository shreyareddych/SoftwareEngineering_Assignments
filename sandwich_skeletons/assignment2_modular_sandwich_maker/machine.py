"""Sandwich machine core - Skeleton."""
from typing import Dict, Tuple
from . import data, inventory, payments  # if running as a package; adjust if running flat

class SandwichMachine:
    """Encapsulates state and behaviors for the sandwich maker."""

    def __init__(self, resources: Dict[str, int]):
        self.resources = resources

    def report(self) -> str:
        """Return a formatted resource report string."""
        # TODO
        raise NotImplementedError

    def can_make(self, size: str) -> Tuple[bool, str]:
        """Check if ingredients are sufficient for a given size."""
        # TODO
        raise NotImplementedError

    def make(self, size: str) -> None:
        """Consume ingredients for a given size and add money to resources."""
        # TODO
        raise NotImplementedError