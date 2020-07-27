from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, table_name):
        self.table_name = table_name

    def __str__(self):
        return f"Model<{self.table_name}>"

    def __repr__(self):
        return f"Model<{self.table_name}>"

    @abstractmethod
    def save(self):
        ...

class User(Model):
    def __init__(self, name, email, income):
        Model.__init__(self, 'user')
        self.name = name
        self.email = email
        self.income = income
    
    def save(self):
        ...