from typing import Literal
from dataclasses import dataclass
@dataclass
class BookCopy:
    book_id:int
    copy_identifier:int
    condition:Literal['new','like new','fair','poor','damaged','repaired']
    currently_rented:bool
    def __post_init__(self):
        valid_conditions = ["new", "like new", "fair", "poor", "damaged", "repaired"]
        if self.condition not in valid_conditions:
            raise ValueError(f"Invalid condition: {self.condition}")
    @property
    def needs_repair(self)->bool:
        return  self.condition in ['poor','damaged'] 