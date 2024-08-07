from src.data import creature as data
from src.model.creature import Creature


def get_all() -> list[Creature]:
    """Return all creatures."""

    return data.get_all()


def get_one(name: str) -> Creature | None:
    """Return creature with specified name."""
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    """Add an creature."""
    return data.create(creature)


def modify(creature: Creature) -> Creature:
    """Partially modify an creature."""
    return data.modify(creature)


def replace(creature: Creature) -> Creature:
    """Completely replace an creature."""
    return data.replace(creature)


def delete(name: str) -> None:
    """Delete an creature; return None if it existsed."""
    return data.delete(name)
