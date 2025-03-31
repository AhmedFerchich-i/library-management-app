from dataclasses import dataclass, field
from datetime import date
from typing import Literal, List
import re


StaffRole = Literal["librarian", "manager", "admin"]
StaffPermission = Literal["manage_books", "manage_members", "manage_staff"]

@dataclass
class Staff:
   
    
    full_name: str
    email: str
    phone_number: str
    role: StaffRole
    hire_date: date = date.today()
    
    is_active: bool = True
    permissions: List[StaffPermission] = field(default_factory=list)

    def __post_init__(self):
        if self.role not in {'librarian','manager','admin'}:
            raise ValueError(f'invalid role : {self.role}')
        permission_set={"manage_books", "manage_members", "manage_staff"}
        invalid_permissions=[permission for permission in self.permissions if permission not in permission_set]
        if invalid_permissions:
            raise ValueError(f'invalid permissions : {invalid_permissions}')
        

    @property
    def has_admin_privileges(self) -> bool:
        return self.role in {"manager", "admin"} 

    