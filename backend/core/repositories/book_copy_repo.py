from abc import ABC,abstractmethod
from entities.book_copy import BookCopy
class BookCopyRepo(ABC):
    @abstractmethod
    def get_condition_by_id(self,id:int)->str:
        pass
    @abstractmethod
    def is_available(self,id:int)->bool:
        pass
    @abstractmethod
    def remove_copy_by_id(self,id:int)->None:
        pass
    @abstractmethod
    def update_availability(self,id:int)->None:
        pass