from dataclasses import dataclass



@dataclass
class Book:
    title:str
    author:str
    total_copies:int
    rented_copies:int
    def __post_init__(self):
        if self.total_copies < 0:
            raise ValueError("Total copies cannot be negative.")
        if self.rented_copies < 0:
            raise ValueError("Rented copies cannot be negative.")
        if self.rented_copies > self.total_copies:
            raise ValueError("Rented copies exceed total copies.")
    @property
    def available_copies(self) ->int:
        return self.total_copies-self.rented_copies
    @property
    def available(self) -> bool:
        return self.available_copies>0




    


    
