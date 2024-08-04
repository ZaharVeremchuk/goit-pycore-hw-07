from Field import Field

class Phone(Field):
    def __init__(self, phone_number):
        self.value = phone_number
    
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, phone_number):
        self.value = phone_number

    def __str__(self):
        return f"Phone number: {self.value}"