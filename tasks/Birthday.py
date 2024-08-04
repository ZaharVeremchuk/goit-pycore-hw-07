from Field import Field
from datetime import datetime

# New class Birthday (MODULE 10)
class Birthday(Field):
    def __init__(self, date: str):
        if datetime.strptime(date, "%d.%m.%Y"):
            self.value = date
        else:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
         
    @property
    def value(self) -> str:
        return self.value
    
    @value.setter
    def value(self, value) -> None:
        self.value = value
        
    