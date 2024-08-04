import re

class Record:
    def __init__(self, name: str):
        self.name = name
        self.phones = []
        self.birthday = None

    def __str__(self):
        if self.birthday is None:
            return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
        else:
            return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}, birthday: {self.birthday}"
    
    def add_phone(self, phone: str) -> None:
        if re.match("\d{10}", phone):
            self.phones.append(phone)
        else:
            print("Phone need to have 10")

    def edit_phone(self, old_phone: str, new_phone: str) -> str:
          for phone in self.phones:
                if phone == old_phone:
                    self.phones.remove(phone)  # Видаляємо старий номер
                    self.phones.append(new_phone)  # Додаємо новий номер

                      
    def find_phone(self, phone: str) -> str:
          for ph in self.phones:
                if ph == phone:
                    return phone
    
    def remove_phone(self, phone : str) -> None:
          for ph in self.phones:
                if ph == phone:
                      self.phones.remove(ph) 
    
    def add_birthday(self, birthday: str) -> str:
        self.birthday = birthday
        return "Birthday added"
        
            