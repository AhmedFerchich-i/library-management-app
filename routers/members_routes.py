from fastapi import APIRouter, Query
from typing import Optional

membersRouter = APIRouter(prefix="/members")

@membersRouter.get("/")
async def get_all_members( ):
    return {"message": "members list"}

@membersRouter.get("/{member_id}")
async def get_member_by_id(member_id: int):  # Added the 'member_id' parameter
    return {"message": f"member info for member ID {member_id}"}
@membersRouter.post('/')
async def create_new_member():
    return{"message":"member created"}
@membersRouter.delete('/{member_id}')
async def delete_member_by_id(member_id:int):
    return{"message":"member deleted"}