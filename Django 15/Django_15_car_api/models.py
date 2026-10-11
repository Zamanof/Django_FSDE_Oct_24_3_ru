from datetime import datetime

from pydantic import BaseModel, Field, field_validator
from pydantic_core import ValidationError


class Car(BaseModel):
    model: str = Field(min_length=1, max_length=100)
    manufacturer: str = Field(min_length=1, max_length=100)
    year: int

    @field_validator('year')
    @classmethod
    def validate_year(cls, value)-> int:
        if not (1885 <= value <= datetime.now().year):
            raise ValidationError('Invalid year')
        return value

class CarCreate(Car):
    pass

class CarUpdate(Car):
    pass

class CarRead(Car):
    id:int