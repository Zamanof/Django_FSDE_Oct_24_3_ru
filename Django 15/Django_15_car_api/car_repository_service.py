from http.client import HTTPException

from in_memory import _next_id, _lock, _store
from models import CarCreate, CarRead, CarUpdate


def _create_car(payload: CarCreate)->CarRead:
    global _next_id
    with _lock:
        cid = _next_id
        _next_id += 1
        car = CarRead(id=cid, **payload.model_dump())
        _store[cid] = car
        return car


def _get_car_by_id(car_id: int)->CarRead:
    car = _store.get(car_id)
    if not car:
        raise HTTPException(404, 'car not found')
    return car


def _get_cars():
    return list(_store.values())


def _delete_car_by_id(car_id: int)->None:
    with _lock:
        del _store[car_id]

def _patch_car_by_id(car_id: int, payload: CarUpdate)->CarRead:
    with _lock:
        car = _get_car_by_id(car_id)
        data = car.model_dump()
        updates = payload.model_dump(exclude_unset=True)
        data.update(updates)
        updated_car = CarRead(**data)
        _store[car_id] = updated_car
        return updated_car
