from dataclasses import dataclass
from datetime import datetime
from typing import Literal
@dataclass
class Transactions():
    user_id:int
    copy_id:int
    time:datetime
    action:Literal['borrow','return']

    def __post_init__(self):
        if self.action  not in {'borrow','return'}:
            raise ValueError(f'invalid action : {self.action}')
