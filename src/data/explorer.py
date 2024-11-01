from sqlite3 import IntegrityError

from src.data.init import curs
from src.model.explorer import Explorer
from src.exceptions import Missing, Duplicate

curs.execute("""CREATE TABLE IF NOT EXISTS explorer(
             name text primary key,
             country text,
             description text)""")


def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])


def model_to_dict(explorer: Explorer) -> dict | None:
    return explorer.model_dump() if explorer else None


def get_one(name: str) -> Explorer:
    query = "SELECT * FROM explorer WHERE name = :name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    if not row:
        raise Missing(f"Explorer `{name}` not found")
    return row_to_model(row)


def get_all() -> list[Explorer]:
    query = "SELECT * FROM explorer"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    query = """INSERT INTO explorer (name, country, description)
               VALUES (:name, :country, :description)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(f"Creature `{explorer.name}` already existss")
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    query = """UPDATE explorer
               SET country=:country,
               name=:name
               description=:description
               WHERE name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(query, params)

    if curs.rowcount != 1:
        raise Missing(f"Explorer `{name}` not found")
    return get_one(explorer.name)


def delete(explorer: Explorer) -> bool:
    query = "DELETE FROM explorer WHERE name = :name"
    params = {"name": explorer.name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(f"Explorer `{explorer.name}` not found")
    return True
