from abc import ABC, abstractmethod

from exceptions.db_exceptions import ModelInstanceAlreadyExist
from db.sqlite_db import db

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
        Model.__init__(self, 'users')
        self.name = name
        self.email = email
        self.income = income
        self.attr_names = ["name", "email", "income"]
    
    def __repr__(self):
        return f"Model<{self.table_name}: {self.email}>"

    def save(self):
        try:
            db.insert_into_table(
                self.table_name, 
                self.attr_names, 
                [self.name, self.email, self.income]
            )
        except:
            raise ModelInstanceAlreadyExist
        
    @classmethod
    def get_all(cls):
        users_tuples = db.select_all_from('users', ["name", "email", "income"])
        for user_tuple in users_tuples:
            yield User(*user_tuple)

    @classmethod
    def get_one(cls):
        ...

    @classmethod
    def filter_by_email(cls):
        ...