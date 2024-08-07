from src.model.explorer import Explorer
from src.data import explorer as data


def get_all() -> list[Explorer]:
    """Return all creatures."""

    return data.get_all()


def get_one(name: str) -> Explorer | None:
    """Return explorer with specified name."""
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    """Add an explorer."""
    return data.create(explorer)


def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer."""
    return data.modify(explorer)


def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer."""
    return data.replace(explorer)


def delete(name: str) -> None:
    """Delete an explorer; return None if it existsed."""
    return data.delete(name)
