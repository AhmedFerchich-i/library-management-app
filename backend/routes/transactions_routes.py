from fastapi import APIRouter,Query
from typing import Optional

transactionsRouter=APIRouter(prefix='/transactions')

@transactionsRouter.post('/rent/{book_id}')
async def rentBookById(book_id:int):
    return {'message':'book rented'}

@transactionsRouter.post('/return/{book_id}')
async def returnBookById(book_id:int):
    return {'message':'book returned'}

@transactionsRouter.get('/transactions/')
async def getTransactions(
    book_id:Optional[int]=Query(None),
    state:Optional[str]=Query(None),
    user_id:Optional[int]=Query(None)
    ):
    return{'message':'transactions returned'}