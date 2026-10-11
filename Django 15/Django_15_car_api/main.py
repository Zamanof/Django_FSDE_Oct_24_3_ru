from typing import List, Optional

from fastapi import FastAPI

from car_repository_service import _create_car, _get_car_by_id, _patch_car_by_id, _delete_car_by_id
from models import CarRead, CarCreate, CarUpdate
from in_memory import _store

app = FastAPI()


@app.post('/cars', response_model=CarRead, status_code=201)
async def create_car(payload: CarCreate):
    return _create_car(payload)

@app.get('/cars', response_model=List[CarRead], status_code=200)
async def get_cars(
        model:Optional[str]=None,
        manufacturer:Optional[str]=None,
        limit: int=100,
        offset: int=0
):
    items = list(_store.values())
    if model:
        items = [c for c in items if c.model.lower() == model.lower()]
    if manufacturer:
        items = [c for c in items if c.manufacturer.lower() == manufacturer.lower()]

    offset = (offset - 1) * limit
    return items[offset:offset + limit]

@app.get('/cars/{car_id}', response_model=CarRead, status_code=200)
async def get_car(car_id: int):
    return _get_car_by_id(car_id)

@app.patch('/cars/{car_id}', response_model=CarRead, status_code=200)
async def update_car(car_id: int, payload: CarUpdate):
    return _patch_car_by_id(car_id, payload)


@app.delete('/cars/{car_id}', status_code=200)
async def delete_car(car_id: int):
    _delete_car_by_id(car_id)
    return None


