from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from src.exceptions import Duplicate, Missing
from src.model.explorer import Explorer
from src.service import explorer as service


router = APIRouter(prefix="/explorers")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Explorer | None:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=exc.msg)


@router.post("/")
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=exc.msg)


@router.patch("/")
def modify(explorer: Explorer) -> Explorer:
    try:
        return service.modify(explorer)
    except Missing as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=exc.msg)


@router.delete("/")
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=exc.msg)
