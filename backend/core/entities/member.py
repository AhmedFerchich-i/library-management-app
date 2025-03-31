from dataclasses import dataclass
from datetime import date
from typing import Literal
@dataclass
class Member():
    full_name:str
    email:str
    phone_number:str
    address:str
    join_date:date
    membership_type:Literal['standard','premium']

    def __post_init__(self):
        if self.membership_type not in ('standard', 'premium'):
             raise ValueError("Invalid membership type. Must be 'standard' or 'premium'.")


    @property
    def borrowing_book_limit(self)->int:
        return (10 if self.membership_type=='premium' else 5 )
    @property
    def loan_time(self)->int:
        return (30 if self.membership_type=='premium' else 15)