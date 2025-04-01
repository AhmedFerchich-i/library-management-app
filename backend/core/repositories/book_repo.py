from abc import ABC,abstractmethod
from entities.book import Book
from typing import Optional,List
class BookRepo(ABC):
    @abstractmethod
    def save(self, book: Book) -> Book:
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def exists(self, title: str, author: str) -> bool:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass
    @abstractmethod
    def find_by_author(self,author:str)->List[Book]:
        pass
    @abstractmethod
    def fiind_all(self)->List[Book]:
        pass
