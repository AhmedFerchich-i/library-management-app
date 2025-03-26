from fastapi import APIRouter, Query
from typing import Optional

staffMemberRouter = APIRouter(prefix="/staff members")

@staffMemberRouter.get("/")
async def get_all_staff_members( ):
    return {"message": "staff members list"}

@staffMemberRouter.get("/{staff_member_id}")
async def get_staff_member_by_id(staff_member_id: int):  # Added the 'staff member_id' parameter
    return {"message": f"staff member info for staff member ID {staff_member_id}"}
@staffMemberRouter.post('/')
async def create_new_staff_member():
    return{"message":"staff member created"}
@staffMemberRouter.delete('/{staff member_id}')
async def delete_staff_member_by_id(staff_member_id:int):
    return{"message":"staff member deleted"}