from collections import UserDict
from datetime import datetime
from Record import Record
import re

class AddressBook(UserDict):

    def __str__(self) -> str:
        text = ""
        for record in self.data.values():
            text += f"{record} \n"
        return text
         
    
    def add_record(self, record: Record):
          self.data[record.name] = record

    def find(self, name: str) -> Record:
          return self.data.get(name)
    
    def delete(self, name: str) -> None:
          self.data.pop(name)
    
    def get_upcoming_birthdays(self) -> list:
                
        today = datetime.today().date()                                             # Create today date
        next_week_birthday = []
        pattern = "%d.%m.%Y"

        for name, record in self.data.items():
            if record.birthday is not None:                                         # Check if record has birthday
                birthday = re.sub(r'\b\d{4}\b', str(today.year), record.birthday)   # Change year of argument date to year today
                birthday = datetime.strptime(birthday, pattern).date()              # Convert str to date
                day_of_week = birthday.weekday()
                if 0 < (birthday - today).days <= 7:                                # If bigger than 0 and less or equal 7
                    if day_of_week == 6:                                            # If Sunday
                        self.move_notification(1)
                    elif day_of_week == 5:                                          # If Sutarday
                        self.move_notification(2)
                    new_dict = {name: birthday.strftime(pattern)}
                    next_week_birthday.append(new_dict)                             # Add to list dict
        return next_week_birthday
    
    # Method that replace date of birthday notification
    def move_notification(self, date: datetime, number: int) -> None:
         date += datetime.timedelta(days=number)

         