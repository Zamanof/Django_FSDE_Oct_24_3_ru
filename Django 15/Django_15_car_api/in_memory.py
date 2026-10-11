from threading import Lock
from typing import Dict

from models import CarRead


_store: Dict[int, CarRead] = {
    1: CarRead(id=1, model="Corolla", manufacturer="Toyota", year=2020),
    2: CarRead(id=2, model="Camry", manufacturer="Toyota", year=2022),
    3: CarRead(id=3, model="Civic", manufacturer="Honda", year=2019),
    4: CarRead(id=4, model="Accord", manufacturer="Honda", year=2021),
    5: CarRead(id=5, model="Mustang", manufacturer="Ford", year=2023),
    6: CarRead(id=6, model="Focus", manufacturer="Ford", year=2018),
    7: CarRead(id=7, model="320i", manufacturer="BMW", year=2020),
    8: CarRead(id=8, model="X5", manufacturer="BMW", year=2022),
    9: CarRead(id=9, model="C200", manufacturer="Mercedes-Benz", year=2021),
    10: CarRead(id=10, model="A4", manufacturer="Audi", year=2019),
    11: CarRead(id=11, model="Golf", manufacturer="Volkswagen", year=2020),
    12: CarRead(id=12, model="Elantra", manufacturer="Hyundai", year=2023),
    13: CarRead(id=13, model="Sportage", manufacturer="Kia", year=2022),
    14: CarRead(id=14, model="Model 3", manufacturer="Tesla", year=2024),
    15: CarRead(id=15, model="Qashqai", manufacturer="Nissan", year=2021),
}
_next_id = 16
_lock: Lock = Lock()


# Race Condition
# Critical Section