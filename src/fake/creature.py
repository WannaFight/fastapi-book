from src.model.creature import Creature


_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    ),
    Creature(
        name="Bogfoot",
        aka="Yeti's cousin Eddie",
        country="US",
        area="*",
        description="Sasquatch",
    ),
]


def get_all() -> list[Creature]:
    """Return all creatures."""

    return _creatures


def get_one(name: str) -> Creature | None:
    """Return creature with specified name."""
    for creature in _creatures:
        if creature.name == name:
            return creature
    return None


def create(creature: Creature) -> Creature:
    """Add an creature."""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify an creature."""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace an creature."""
    return creature


def delete(name: str) -> None:
    """Delete an creature; return None if it existsed."""
    return None
