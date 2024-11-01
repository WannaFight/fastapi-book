from sqlite3 import IntegrityError
from src.exceptions import Missing, Duplicate
from src.data.init import curs
from src.model.creature import Creature

curs.execute("""CREATE TABLE IF NOT EXISTS creature(
                name text primary key,
                description text,
                country text,
                area text,
                aka text)
             """)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name,
        description=description,
        country=country,
        area=area,
        aka=aka,
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def get_one(name: str) -> Creature:
    query = "SELECT * FROM creature WHERE name = :name"
    params = {"name": name}

    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all(name: str) -> list[Creature]:
    query = "SELECT * FROM creature"

    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature):
    query = """INSERT INTO creature VALUES
        (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    curs.execute(query, params)
    return get_one(creature.name)


def modify(creature: Creature):
    query = """
        UPDATE creature
        SET country=:country,
            name=:name,
            description=:description,
            area=:area,
            aka=:aka
        WHERE name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(query, params)
    return get_one(creature.name)


def replace(creature: Creature):
    return creature


def delete(creture: Creature) -> bool:
    query = "DELETE FROM creature WHERE name = :name"
    params = {"name": creture.name}
    res = curs.execute(query, params)
    return bool(res)
