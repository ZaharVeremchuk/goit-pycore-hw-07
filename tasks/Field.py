class Field:
    def __init__(self, field):
        self.value = field

    def __str__(self):
        return str(self.value)
    
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return f"Field value:{self.value}"