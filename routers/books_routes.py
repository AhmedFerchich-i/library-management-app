from fastapi import APIRouter, Query
from typing import Optional

booksRouter = APIRouter(prefix="/books")

@booksRouter.get("/")
async def get_all_books(
    author: Optional[str] = Query(None),
    available: Optional[bool] = Query(None)
):
    return {"message": "books list"}

@booksRouter.get("/{book_id}")
async def get_book_by_id(book_id: int):  # Added the 'book_id' parameter
    return {"message": f"Book info for book ID {book_id}"}
@booksRouter.post('/')
async def create_new_book():
    return{"message":"book created"}
@booksRouter.delete('/{book_id}')
async def delete_book_by_id(book_id:int):
    return{"message":"book deleted"}