"""User Interface (CLI) - Skeleton."""
from typing import Optional

VALID_CHOICES = {"small", "medium", "large", "report", "off"}

def prompt_choice() -> str:
    """Ask user for a command/size and return the normalized choice."""
    # TODO
    raise NotImplementedError

def show_message(text: str) -> None:
    """Display a line to the user (kept separate for easy UI swaps)."""
    print(text)